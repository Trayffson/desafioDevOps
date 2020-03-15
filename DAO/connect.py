import os, logging
import pymysql

logging.basicConfig(filename='desafioElo.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(funcName)s => %(message)s')


def connection():

    try:
        connection = pymysql.connect(host='db',
                             user="root",
                             db='deploy',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
    except Exception as e: 
        logging.ERROR(f"Ocorreu um erro ao conectar no Mysql \n {e}")

    return connection