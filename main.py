
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)





    #######################################
###########   DF museos     #################
    #######################################

data_frame_museos = pd.read_csv('museos_datosabiertos.csv', header = 0, usecols = ['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'categoria', 'provincia', 'localidad', 'nombre', 'direccion', 'CP',  'telefono', 'Mail', 'Web']) 



# renombrar las columnas par anomrlalizar al momento de concat()
data_frame_museos.rename(columns = {'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento': 'id_departamento', 'categoria':'categoría', 'provincia':'provincia', 'localidad':'localidad', 'nombre':'nombre', 'direccion':'domicilio', 'CP':'código_postal', 'telefono':'número_teléfono', 'Mail':'mail', 'Web':'web'}, inplace = True)












    #######################################
###########   DF cines     #################
    #######################################

data_frame_cines = pd.read_csv('cine.csv', header = 0) 

data_frame_cines = pd.read_csv('cine.csv', header = 0, usecols = ['Cod_Loc', 'IdProvincia', 'IdDepartamento', 
       'Categoría', 'Provincia', 'Localidad', 'Nombre', 'Dirección', 'CP',  'Teléfono', 'Mail', 'Web']) 

data_frame_cines.rename(columns = {'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento': 'id_departamento', 'Categoría':'categoría', 'Provincia':'provincia', 'Localidad':'localidad', 'Nombre':'nombre', 'Dirección':'domicilio', 'CP':'código_postal', 'Teléfono':'número_teléfono', 'Mail':'mail', 'Web':'web'}, inplace = True)










    #######################################
###########   DF bibliotecas     #################
    #######################################

data_frame_bibliotecas = pd.read_csv('biblioteca_popular.csv', header = 0) 

data_frame_bibliotecas = pd.read_csv('biblioteca_popular.csv', header = 0, usecols = ['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Categoría', 'Provincia', 'Localidad', 'Nombre', 'Domicilio', 'CP',  'Teléfono', 'Mail', 'Web']) 

# renombrar las columnas par anomrlalizar al momento de concat()
data_frame_bibliotecas.rename(columns = {'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento': 'id_departamento', 'Categoría':'categoría', 'Provincia':'provincia', 'Localidad':'localidad', 'Nombre':'nombre', 'Domicilio':'domicilio', 'CP':'código_postal', 'Teléfono':'número_teléfono', 'Mail':'mail', 'Web':'web'}, inplace = True)










dataFrame_1_normalizado = pd.concat([data_frame_museos, data_frame_cines], axis = 0)
dataFrame_2_normalizado = pd.concat([dataFrame_1_normalizado, data_frame_bibliotecas], axis = 0)

  
print(dataFrame_2_normalizado.head(10))
print("-1- ")
print(dataFrame_2_normalizado.tail(10))
print("-2- ")
print(dataFrame_2_normalizado.columns)
#print(data_frame_bibliotecas)

dataFrame_2_normalizado.to_csv('./dataFrame_2_normalizado.csv', index=False)
 

print("--- ")
#df = pd.DataFrame({'name' : ['User 1', 'User 2', 'User 3']})
#print(df)
## df.to_sql('users', con=engine)
#data_frame_museos.to_sql('userss', con=engine)
#print(engine.execute("SELECT provincia FROM userss WHERE provincia == 'Chubut'").fetchall())




      
"""


['Cod_Loc', 'IdProvincia', 'IdDepartamento', 
       'categoria', 'provincia', 'localidad', 'nombre',
       'direccion', 'CP',  'telefono', 'Mail', 'Web']




cod_localidad
id_provincia
id_departamento
categoría
provincia
localidad
nombre
domicilio
código_postal
número_teléfono
mail
web





1 - extraer csv y hacerlos archivos en local folder
2 - leer esos csv y hacer folders donde van a estar
3 - hacer tabla normal
4 - hacer tabla cantidades, son 3 tablas
5 - hacer tabla cines
6 - crear DB, conectarse a DB
7 - insertarle tablas a DB
8 - armar proyecto en -env
9 - logear todo lo que se pueda
10 - el main.py lo que tiene que hacer es correr todas las anteriores cosas; sería solo para crear y guardar la data; programa para usarse de a una sola vez



"""


      