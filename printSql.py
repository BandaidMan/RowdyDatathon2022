# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import psycopg2
import pandas as pd
import numpy as np

conn = psycopg2.connect("dbname=nchsDB user=postgres password=gpPassword")
cur = conn.cursor()

x = cur.execute('''SELECT dt_year, am_birthweight, am_birthweight3, dt_dob, id FROM "USA"."natalityConf"
WHERE am_birthweight3='1' AND am_birthweight<>'9999'
ORDER BY dt_year ASC LIMIT 5;''')

rows = cur.fetchall()

print(rows)









