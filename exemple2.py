# -*- coding: utf-8 -*-
"""
Created on Sat May 12 09:34:35 2018

@author: ASUS
"""

import sqlite3
sqlite_DB='my_basedonnee.sqlite' # le nom de la base
table1='T_Etudiant' # le nom de la table1
table2='T_filiere' # le nom de la table2
attr1='id' #le nom de l'attribut1
type_attribut1='INTEGER' #le type de l'attribut INTERGER, TEXT, NULL, REAL, BLOB
attr2='libelle' #le nom de l'attribut2
type_attribut2='TEXT' 
attr3='Faculté' #le nom de l'attribut3
type_attribut3='TEXT'
#connexion à la BD
conn=sqlite3.connect(sqlite_DB)
c=conn.cursor()
#Création de la table1 avec un seul attribut
def create():
    #Création de la table2 avec un  attribut PRIMARY KEY
    c.execute('CREATE TABLE if not exists {t} ({a} {ty} PRIMARY KEY)'\
              .format(t=table2, a=attr1,ty=type_attribut1))
    c.execute('CREATE TABLE if not exists {t} ({a} {ty} PRIMARY KEY)'\
              .format(t=table1, a=attr1,ty=type_attribut1))
#create()
#**********************************************************
#Suppression des tables:
def supp_T_Etudiant():
    c.execute('drop table T_Etudiant')
def supp_T_filiere():
    c.execute('drop table T_filiere')
# Ajouter une conne2 et une colonne 3 à la table2
def maj_table():
    c.execute("ALTER TABLE {t} ADD COLUMN '{aj1}' {ty1}"\
              .format(t=table2, aj1=attr2, ty1=type_attribut2))
    
 # Ajouter une  colonne 3 à la table2                 

    c.execute("ALTER TABLE {t} ADD COLUMN '{aj1}' {ty1}"\
              .format(t=table2, aj1=attr3, ty1=type_attribut3))
              
        
#supp_T_Etudiant()
#supp_T_filiere() 
#maj_table()
def delete():
    c.execute("delete from {T}".format(T=table2))
#delete()
#*********************************************************
#insertion des valeurs:
def insertion():
    try:
        c.execute("insert into {t}({V0},{V1},{V2}) values (1,'Bigdata','ESSAI')".\
                  format(t=table2,V0=attr1, V1=attr2, V2=attr3))
           
        #c.execute("insert OR IGNORE INTO {t}({V0},{V1},{V2}) values (1,'Bigdata','Dauphine')".\
           #format(t=table2,V0=attr1, V1=attr2, V2=attr3))
        c.execute("insert into {t}({V0},{V1},{V2}) values (2,'BD','ESSAI')".\
                  format(t=table2,V0=attr1, V1=attr2, V2=attr3))
           
        c.execute("insert into {t}({V0},{V1},{V2}) values (3,'Anglais','ESSAI')".\
                  format(t=table2,V0=attr1, V1=attr2, V2=attr3))
           
        c.execute("insert into {t}({V0},{V1},{V2}) values (4,'Maths','ESSAI')".\
                  format(t=table2,V0=attr1, V1=attr2, V2=attr3))
           
    except sqlite3.IntegrityError:
        print("ERROR/ ID already exists in PRIMARY KEY column {0}".format(attr1))
    
#remplacer Essai du premier tuple par Insat
def maj_donnee():
    c.execute("update {t} set {V2}=('insat') where {V0}=(1)".format(t=table2,V2=attr3,V0=attr1))
        
#insertion()
#maj_donnee()
#*******************************************************
#sélectionner seulement deux tuples dont l'école='ESSAI'
def selection1():
    c.execute('SELECT * FROM {t}  WHERE {a2}="ESSAI" LIMIT 2'.\
              format(t=table2, a2=attr3))
    lignes=c.fetchall()
    print('1):', lignes)
    #afficher le tuple dont la clé est égale à 3, sinon écrire 'il n'existe pas':
def selection2():
    constante=5
    c.execute('SELECT * FROM {t}  WHERE {a1}={a2}'.format(a1=attr1,a2=constante, t=table2))
    ligne=c.fetchone()
    if ligne:
        print('2):{}'.format(ligne))
    else:
        print('{} n\'existe pas '.format(constante))
            
#selection1()
#selection2()
#*************************************************
def info():
    c.execute('PRAGMA TABLE_INFO({})'.format(table2))
#collect names in a list
    names=[tup for tup in c.fetchall()]
    print(names)
#info()
#**************************************************
def infoprime():
    print(c.execute('PRAGMA TABLE_INFO({})'.format(table2)).fetchall())
#collect names in a list
    #names=[tup for tup in c.fetchall()]
    #print(names)
#infoprime()    
#mettrela base de données dans un fichier CSV
import pandas as pd
def to_csv():
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    
    tables=c.fetchall()
    print (tables)
    for table_name in tables:
        table_name=table_name[0]
        table=pd.read_sql_query("SELECT * from %s" %table_name,conn)
        print(table)
        table.to_csv(table_name+'1.csv',index_label='index')
        
#to_csv()
def to_csvbis():
    tables=(c.execute("SELECT name FROM sqlite_master WHERE type='table'")).fetchone()
    print (tables)

    for table_name in tables:
        table_name=table_name[0]
        table=pd.read_sql_query("SELECT * from T_filiere",conn)
        print(table)
        table.to_csv(table_name+'.csv',index_label='index')
    
#to_csvbis()        
        
conn.commit()   
c.close()
conn.close()
