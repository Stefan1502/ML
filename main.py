from selenium import webdriver
import time

import sqlite3
conn = sqlite3.connect('db.db')
c = conn.cursor()

c.execute("""CREATE TABLE score (
    home text,
    score1 integer,
    score2 integer,
    away text
    )""")
conn.commit()

chrome = webdriver.Chrome('./chromedriver')
chrome.get('https://www.rezultati.com/nogomet/engleska/premier-league/rezultati/')
time.sleep(2)

matches = chrome.find_elements_by_css_selector("[title^='Kliknite za detalje utakmice!']")

for txt in matches:
    el = (txt.text.split('\n'))
    c.execute("INSERT INTO score VALUES (?, ?, ?, ?)", (el[1], int(el[2]), int(el[4]), el[5]))
    conn.commit()

c.execute("SELECT * FROM score")
print(c.fetchall())

conn.close()
chrome.close()
