from codigo_de_ejecucion import *
import streamlit as st
from streamlit_echarts import st_echarts

#configuración página

st.set_page_config(
    page_title='Heart Analyzer',
    page_icon='imagen_logo.png',
    layout = 'wide'
    )

#sidebar:

with st.sidebar:
    st.image('imagen_principal.png')

    #imputs aplicacion
    age = st.number_input('Edad',1,120)
    chess_pain = st.radio('Intensida dolor de pecho',[0,1,2,3])
    cholestoral = st.slider('Nivel de colesterol',100,500)
    maximum_heart_rate = st.slider('Pulsaciones por minuto',50,250)
    number_major_vessels = st.radio('Vasos sanguineos mayores',[0,1,2,3,4,5])

    sex = st.radio('Sexo', ['Hombre', 'Mujer'])

    if sex == 'Hombre':
        sex_value = 0
    else:
        sex_value = 1

    #Datos conocidos (por simplificar)
    oldpeak = 3.2
    thall = 2

#main
st.title('¿QUÉ PROBABILIDAD TIENE DE SUFRIR UN ATAQUE DE CORAZÓN?')

#calcular
#Crear registro
registro = pd.DataFrame({'age': age,
                          'chess_pain':chess_pain,
                          'cholestoral':cholestoral,
                          'maximum_heart_rate':maximum_heart_rate,
                          'number_major_vessels':number_major_vessels,
                          'sex':sex_value,
                          'oldpeak':oldpeak,
                          'thall':thall,
                          },
                          index=[0])

#Calcular el riesgo



#Click boton:
if st.sidebar.button('Calcular'):
    resultado = ejecutar(registro)
    resultado_final = resultado[0]
    resultado_porcentual=resultado_final*100

    #st.write(resultado_final)
    #st.write(f'La probabilidad de sufrir un infarto es del : {resultado_porcentual:2f}%')

    if resultado_final < 0.5:
        st.markdown(
            f'''
            <h2 style="color: #42A5F5 ;">Tienes un riesgo bajo de sufrir un ataque cardíaco. Sigue manteniéndote saludable! {resultado_porcentual:.2f}%</h2>
            ''',
            unsafe_allow_html=True)
        
        st.image('corazon_ok.png')
    else:
        st.markdown(
            f'''
            <h2 style="color: #FFA726;">Es importante que consultes a un médico para evaluar tu salud cardíaca. Riesgo del {resultado_porcentual:.2f}%</h2>
            ''',
            unsafe_allow_html=True)
        
        st.image('corazon_ko.png')

#no click boton:
else:
    st.write('Define los parametros para clacular')
