#!/usr/bin/env python
# coding: utf-8

# # Ejercicio 1 - Python
# 
# ## Contexto
# 
# El Informe Mundial de la Felicidad es una encuesta histórica sobre el estado de la felicidad global. El primer
# informe se publicó en 2012, el segundo en 2013, el tercero en 2015 y el cuarto en la actualización de 2016. El
# World Happiness 2017, que clasifica a 155 países según sus niveles de felicidad, se lanzó en las Naciones
# Unidas en un evento que celebra el día internacional de la felicidad el 20 de marzo. El informe continúa ganando
# reconocimiento mundial a medida que los gobiernos, las organizaciones y la sociedad civil utilizan cada vez más
# los indicadores de felicidad para informar de sus decisiones de formulación de políticas. Los principales
# expertos en todos los campos (economía, psicología, análisis de encuestas, estadísticas nacionales, salud,
# políticas públicas y más) describen cómo las mediciones de bienestar se pueden usar de manera efectiva para
# evaluar el progreso de las naciones.
# 
# ## Contenido
# 
# Los puntajes y clasificaciones de felicidad utilizan datos de la encuesta mundial Gallup. Las puntuaciones se basan en las respuestas a la pregunta principal de evaluación de la vida formulada en la encuesta. Esta pregunta, conocida como la escalera de Cantril, les pide a los encuestados que piensen en una escalera con la mejor vida posible para ellos con un 10 y la peor vida posible con un 0 y que califiquen sus propias vidas actuales en esa escala. Las puntuaciones provienen de muestras representativas a nivel nacional para los años 2013-2016 y utilizan los pesos de Gallup para hacer que las estimaciones sean representativas. Las columnas que siguen la puntuación de felicidad estiman el grado en que cada uno de los seis factores (producción económica, apoyo social, esperanza de vida, libertad, ausencia de corrupción y generosidad) contribuyen a que las evaluaciones de vida sean más altas en cada país que en la distopía, un país hipotético que tiene valores iguales a los promedios nacionales más bajos del mundo para cada uno de los seis factores. No tienen impacto en el puntaje total reportado para cada país, pero sí explican por qué algunos países tienen una clasificación más alta que otros.
# 
# ## ¿Qué es la distopía?
# 
# La distopía es un país imaginario que tiene las personas menos felices del mundo. El propósito de establecer la
# distopía es tener un punto de referencia con el que todos los países puedan ser comparados favorablemente
# (ningún país tiene un desempeño más pobre que la distopía) en términos de cada una de las seis variables
# clave, lo que permite que cada barra sea de ancho positivo. Las puntuaciones más bajas observadas para las
# seis variables clave, por lo tanto, caracterizan la distopía. La vida sería muy desagradable en un país con los
# ingresos más bajos del mundo, la esperanza de vida más baja, la generosidad más baja, la mayoría de la
# corrupción, la menor libertad y el menor apoyo social, en contraste con la utopía.

# ## Contenido
# 
# Los puntajes y clasificaciones de felicidad utilizan datos de la encuesta mundial Gallup. Las puntuaciones se
# basan en las respuestas a la pregunta principal de evaluación de la vida formulada en la encuesta. Esta
# pregunta, conocida como la escalera de Cantril, les pide a los encuestados que piensen en una escalera con la
# mejor vida posible para ellos con un 10 y la peor vida posible con un 0 y que califiquen sus propias vidas
# actuales en esa escala. Las puntuaciones provienen de muestras representativas a nivel nacional para los años
# 2013-2016 y utilizan los pesos de Gallup para hacer que las estimaciones sean representativas. Las columnas
# que siguen la puntuación de felicidad estiman el grado en que cada uno de los seis factores (producción
# económica, apoyo social, esperanza de vida, libertad, ausencia de corrupción y generosidad) contribuyen a que
# las evaluaciones de vida sean más altas en cada país que en la distopía, un país hipotético que tiene valores
# iguales a los promedios nacionales más bajos del mundo para cada uno de los seis factores. No tienen impacto
# en el puntaje total reportado para cada país, pero sí explican por qué algunos países tienen una clasificación
# más alta que otros.

# ## Se pide
# 
# Sobre los informes de felicidad de 2015 y 2016, realizar las siguientes exploraciones:
# 1. Cargar los dos CSV como datasets.
# 2. Identifica las columnas de ambos datasets: ¿hay diferencias entre ambos?
# 3. Une ambos dataframes, sin importar que los dos compartan las mismas diferencias.
# 4. Revisa el número de nulos que hay por cada columna, así como su porcentaje.
# 5. Cambia los valores nulos de las columnas "Lower Confidence Interval" y "Upper Confidence Interval" por
#     un número aleatorio entre el valor mínimo y máximo de la misma columna (un único número, no es
#     necesario uno diferente para cada fila con valor nulo).
# 6. Cambia los valores nulos de la columna "Standard Error" por su media al cuadrado.
# 7. Obtén un resumen estadístico del dataframe sin valores nulos.
# 8. Muestra de forma gráfica la relación entre la familia y la salud.
# 9. Muestra de forma gráfica la relación entre la puntuación de felicidad y la confianza (corrupción del
#     gobierno).
# 10. Muestra la matriz de correlación del daframe.
# 11. Tras unir los dataframes, los países aparecerán más de una vez. Muestra agrupado el dataframe por
#     país con el valor máximo de felicidad, sin importar el año.
#     ¿Tiene relación la felicidad con la generosidad? Muéstralo gráficamente a través de la puntuación de
#     libertad.
# 12. Muestra la distribución del grado de distopía en función de la región.

# ### 1. Cargar los dos CSV como datasets.

# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


datos_2015 = pd.read_csv('2015.csv')
datos_2016 = pd.read_csv('2016.csv')


# In[3]:


datos_2015


# In[4]:


datos_2016


# ### 2. Identifica las columnas de ambos datasets: ¿hay diferencias entre ambos?

# In[5]:


print (datos_2015.columns)
print (datos_2015.shape)


# In[6]:


print (datos_2016.columns)
print (datos_2016.shape)


# Los datos del 2015 tienen 'Standard Error', la cual no se incluye en los datos 2016 y este tiene 'Lower Confidence Interval', 'Upper Confidence Interval' que no son incluidos en 2015. En resumen, hay 11 columnas comunes y 3 distintas.

# ### 3. Une ambos dataframes, sin importar que los dos compartan las mismas diferencias.

# In[7]:


df = pd.concat([datos_2015, datos_2016], ignore_index=True, join='outer')

df


# ### 4. Revisa el número de nulos que hay por cada columna, así como su porcentaje.

# In[8]:


print("*Número de datos nulos por columna")
print(df.isnull().sum())
print(40*"-")
print("*Porcentaje de datos nulos por columna")
print(df.isnull().sum()/len(df)*100)


# ### 5. Cambia los valores nulos de las columnas "Lower Confidence Interval" y "Upper Confidence Interval" por un número aleatorio entre el valor mínimo y máximo de la misma columna (un único número, no es necesario uno diferente para cada fila con valor nulo)

# In[9]:


print ("*El valor mínimo de Lower Confidence Interval es ", df['Lower Confidence Interval'].min(),'\n')
print ("*El valor máximo de Lower Confidence Interval es ", df['Lower Confidence Interval'].max(),'\n')
print ("*El valor mínimo de Upper Confidence Interval es ", df['Upper Confidence Interval'].min(),'\n')
print ("*El valor máximo de Upper Confidence Interval es ", df['Upper Confidence Interval'].max(),'\n')


# In[10]:


def funcion(df):
    df_min = df.min()
    df_max = df.max()
    valor_aleatorio = np.random.uniform(df_min, df_max)
    return (valor_aleatorio) 


# In[11]:


numero_aleatorio_1 = funcion(df['Lower Confidence Interval'])
numero_aleatorio_2 = funcion(df['Upper Confidence Interval'])


# In[12]:


df['Lower Confidence Interval'] = df['Lower Confidence Interval'].fillna(numero_aleatorio_1)
df['Upper Confidence Interval'] = df['Upper Confidence Interval'].fillna(numero_aleatorio_2)


# In[13]:


print ('Sustituimos los valores nulos de ambas columnas con valores aleatorios entre el mínimo y el máximo')
df[['Lower Confidence Interval', 'Upper Confidence Interval']]


# ### 6. Cambia los valores nulos de la columna "Standard Error" por su media al cuadrado

# In[14]:


print('Media de la columna Standard Error', round(df['Standard Error'].mean(),3))


# In[15]:


df['Standard Error'] = df['Standard Error'].fillna(round(df['Standard Error'].mean()**2,4))
df['Standard Error']


# ### 7. Obtén un resumen estadístico del dataframe sin valores nulos.

# In[16]:


print("*CANTIDAD de datos nulos por columna en el dataframe")
print(df.isnull().sum())


# In[17]:


df.describe()


# ### 8. Muestra de forma gráfica la relación entre la familia y la salud.

# In[18]:


import seaborn as sns


# In[19]:


Familia_salud = ['Family','Health (Life Expectancy)']
datos_fs = df[Familia_salud]
datos_fs


# In[20]:


sns.lmplot(x='Family', y = 'Health (Life Expectancy)', data = df)


# ### 9. Muestra de forma gráfica la relación entre la puntuación de felicidad y la confianza (corrupción del gobierno).

# In[21]:


sns.lmplot(x="Happiness Score", y = 'Trust (Government Corruption)', data = df)


# ### 10. Muestra la matriz de correlación del dataframe

# In[22]:


sns.heatmap(df.corr(), cmap='Blues')


# ### 11. Tras unir los dataframes, los países aparecerán más de una vez. Muestra agrupado el dataframe por país con el valor máximo de felicidad, sin importar el año.

# In[23]:


df = df.sort_values(['Country', 'Happiness Score',])
df


# ### 12. Muestra la distribución del grado de distopía en función de la región.

# In[24]:


from matplotlib import pyplot as plt


# In[25]:


sns.boxplot(x='Region', y='Dystopia Residual', data=df)
plt.xticks(rotation=90)


# In[ ]:




