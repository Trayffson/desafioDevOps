import datetime, logging
import json
from DAO.connect import connection

logging.basicConfig(filename='desafioElo.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(funcName)s => %(message)s')

db = connection()


def insert_mysql(data):
    print(data['versao'])
    try:

        with db.cursor() as cursor:

            sql = f"INSERT INTO deploy_api (componente, versao, responsavel ,status, data) VALUES ('{data['componente']}', '{data['versao']}', '{data['responsavel']}', '{data['status']}',  '{str(datetime.datetime.now())}')"

            cursor.execute(sql)

            db.commit()

    except Exception as e:
        logging.ERROR(f"Erro ao executar insert na base de dados {e}")


def get_dados():
    try:

        with db.cursor() as cursor:

            sql = f"SELECT * FROM deploy_api"

            cursor.execute(sql)

            return cursor.fetchall()

    except Exception as e:
        logging.ERROR(f"Erro ao consultar dados na base de dados {e}")
