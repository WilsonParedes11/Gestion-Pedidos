#-----@Wilson11-----#

import mysql.connector


class Registro_Usuarios():

   def __init__(self):
      self.conexion = mysql.connector.connect(host='localhost',
                                             database='registro_usuarios',
                                             user='root',
                                             password='')
   
   def registra_usuario(self,nombre,password):
      cur = self.conexion.cursor()
      sql='''INSERT INTO usuarios (NOMBRE, PASSWORD) 
      VALUES ('{}','{}')'''.format(nombre,password)
      cur.execute(sql)
      self.conexion.commit()
      cur.close()

   def buscar_usuario(self,nombre):
      cur=self.conexion.cursor()
      sql='''SELECT * FROM usuarios WHERE NOMBRE = {}'''.format(nombre)
      cur.execute(sql)
      usuariox=cur.fetchall()
      cur.close()
      return usuariox

   def buscar_password(self,password):
      cur=self.conexion.cursor()
      sql='''SELECT * FROM usuarios WHERE PASSWORD = {}'''.format(password)
      cur.execute(sql)
      passwordx=cur.fetchall()
      cur.close()
      return passwordx



    
