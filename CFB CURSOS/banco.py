import sqlite3
from sqlite3 import Error
import os

pastaApp = os.path.dirname(__file__)
nomeBanco = pastaApp+ "\\cliente.db"

def conexaoBanco():
    con=None
    try:
        con=sqlite3.connect(nomeBanco)
    except Error as ex:
        print(ex)
    return con

def dql(query): #select
    vcon=conexaoBanco()
    c=vcon.cursor()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res

def dml(query): #insert, update, delete
    vcon=conexaoBanco()
    c=vcon.cursor()
    c.execute(query)
    res = c.fetchall()
    vcon.commit()
    vcon.close()
    return res
        
    
