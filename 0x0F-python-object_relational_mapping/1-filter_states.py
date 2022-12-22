#!/usr/bin/python3

""" Lists all states from database hbtn_0e_0_usa starting with N """

import MySQLdb

from sys import argv

if __name__ == "__main__":

        db = MySQLdb.connect(host="localhost",port=3306,
                                              user=argv[1],
                                             passwd=argv[2],
                                              db=argv[3])

            cursor = db.cursor()

                cursor.execute("SELECT * FROM states")

                    for data in cursor.fetchall():

                                if data[1][0] == 'N':

                                                print(data)

                                                    cursor.close()

                                                        db.close()
