import psycopg2
import os


class Database:

    def __init__(self):
        self.db_host = "localhost"
        self.db_port = 5432
        self.db_name = "sharebook"
        self.db_user = "emre"
        self.db_pass = "emre6549"
    
    def getDatabaseInstance(self):
    
        return psycopg2.connect(dbname=self.db_name, user=self.db_user, host=self.db_host, password=self.db_pass, port=self.db_port)
