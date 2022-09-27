import os

import pymysql


class ColumbiaStudentResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        # usr = os.environ.get("dbuser")
        # pw = os.environ.get("dbpw")
        # hst = os.environ.get("dbhost")

        conn = pymysql.connect(
            # user=usr,
            # password=pw,
            # host=hst,
            user="admin",
            password="team_lol",
            host="database-lol.chy7cu9rusdl.us-east-2.rds.amazonaws.com",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        # print(conn)
        return conn


    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM f22_databases.columbia_students where guid=%s";
        conn = ColumbiaStudentResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

