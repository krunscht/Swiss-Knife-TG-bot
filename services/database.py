import psycopg2
from psycopg2 import Error
import configparser

config = configparser.ConfigParser()
config.read("bot_config.ini")

try:
    DB_NAME = config["db"]["DB_NAME"]
    DB_USER = config["db"]["DB_USER"]
    DB_PASSWORD = config["db"]["DB_PASSWORD"]
    DB_HOST = config["db"]["DB_HOST"]
    DB_PORT = config["db"]["DB_PORT"]
except KeyError:
    print("Ошибка: не найдены настройки БД в файле bot_config.ini")
    DB_NAME = "postgres"
    DB_USER = "postgres"
    DB_PASSWORD = ""
    DB_HOST = "localhost"
    DB_PORT = "5432"

def _get_connection():
    try:
        return psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
    except Error as e:
        print(f"Ошибка подключения к БД: {e}")
        return None

def init_db():
    conn = _get_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS user_logs (
                        id SERIAL PRIMARY KEY,
                        user_id BIGINT NOT NULL,
                        command TEXT NOT NULL,
                        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                ''')
                conn.commit()
                print("[DB] Таблица проверена/создана.")
        except Error as e:
            print(f"Ошибка при создании таблицы: {e}")
        finally:
            conn.close()

def _save_log(user_id, command):
    conn = _get_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO user_logs (user_id, command) VALUES (%s, %s)",
                    (user_id, command)
                )
                conn.commit()
        except Error as e:
            print(f"Ошибка при записи: {e}")
        finally:
            conn.close()

def log_to_db(func):
    def wrapper(message):
        _save_log(message.chat.id, message.text)
        return func(message)
    return wrapper