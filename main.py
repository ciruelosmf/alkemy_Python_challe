
import pandas as pd

data_frame_museos = pd.read_csv('museos_datosabiertos.csv', header = 0, usecols = ['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'categoria', 'provincia', 'localidad', 'nombre', 'direccion', 'CP',  'telefono', 'Mail', 'Web']) 






data_frame_cines = pd.read_csv('cine.csv', header = 0) 

data_frame_cines = pd.read_csv('cine.csv', header = 0, usecols = ['Cod_Loc', 'IdProvincia', 'IdDepartamento', 
       'Categoría', 'Provincia', 'Localidad', 'Nombre', 'Dirección', 'CP',  'Teléfono', 'Mail', 'Web']) 







data_frame_bibliotecas = pd.read_csv('biblioteca_popular.csv', header = 0, usecols = ['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Categoría', 'Provincia', 'Localidad', 'Nombre', 'Domicilio', 'CP',  'Teléfono', 'Mail', 'Web']) 



data_frame_bibliotecas = pd.read_csv('biblioteca_popular.csv', header = 0) 



#data_frame_museos_cat = pd.read_csv('museos_datosabiertos.csv', header = 0, usecols = ['categoria']) 
#data_frame_cines_cat = pd.read_csv('cine.csv', header = 0, usecols = ['Categoria']) 
#data_frame_bibliotecascat = pd.read_csv('biblioteca_popular.csv', header = 0, usecols = ['categoria']) 


  
print(data_frame_museos.columns)
print(data_frame_cines.columns)
print("--- ")
print(data_frame_bibliotecas.columns)
#print(data_frame_bibliotecas)



      
"""


['Cod_Loc', 'IdProvincia', 'IdDepartamento', 
       'categoria', 'provincia', 'localidad', 'nombre',
       'direccion', 'CP',  'telefono', 'Mail', 'Web']




Cod_Loc
IdProvincia
IdDepartamento
categoria
provincia
localidad
nombre
direccion
CP
telefono
Mail
Web


"""


      