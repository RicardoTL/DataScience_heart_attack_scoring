import cloudpickle
import pandas as pd
import numpy as np
from janitor import clean_names

#Carga de datos (como no es un proce bach no la necesitamos para la aplicacion)
'''
ruta_proyecto = 'C:/Users/Ricardo/Desktop/Portfolio/heart'

nombre_fichero_datos = 'validacion.csv' #Representa el nuevo fichero sobre el que aplicar el modelo.

ruta_completa = ruta_proyecto + '/02_Datos/02_Validacion/' + nombre_fichero_datos

df = pd.read_csv(ruta_completa,index_col=0)

df = clean_names(df) \
             .drop_duplicates() \
             .dropna(thresh=3)

df.rename(columns = {'cp':'chess_pain'
                    ,'trtbps':'blood_pressure'
                    ,'chol':'cholestoral'
                    ,'fbs':'fasting_blood_sugar'
                    ,'restecg':'electro_results'
                    ,'thalachh':'maximum_heart_rate'
                    ,'exng':'angina_induced'
                    ,'caa':'number_major_vessels'
                    }, inplace=True)

'''
#Variables finales (Nos sobra también)
'''
variables_finales = ['age',
 'chess_pain',
 'cholestoral',
 'maximum_heart_rate',
 'number_major_vessels',
 'oldpeak',
 'sex',
 'thall']
                     
df = df[variables_finales]

'''
def ejecutar(df):

    with open('pipe_ejecucion.pickle', mode='rb') as file:
        pipe_ejecucion = cloudpickle.load(file)

    scoring = pipe_ejecucion.predict_proba(df)[:, 1]

    return scoring