#-----------------------------------------------------------------------------------------
# @Autor: Aurélien Vannieuwenhuyze
# @Empresa: Junior Makers Place
# @Libro
# @Capítulo: 03 - Estadísticas para comprender los datos
#
# Módulos necesarios:
#   PANDAS 0.24.2
#   NUMPY 1.16.3
#   JMPEstadísticas (copiar el archivo dentro de su proyecto al mismo nivel que este archivo)
#
# Para instalar un módulo:
#   Haga clic en el menú File > Settings > Project:nombre_del_proyecto > Project interpreter > botón +
#   Introduzca el nombre del módulo en la zona de búsqueda situada en la parte superior izquierda
#   Elegir la versión en la parte inferior derecha
#   Haga clic en el botón install situado en la parte inferior izquierda
#-----------------------------------------------------------------------------------------

import pandas as pnd
import JMPEstadisticas as jmp
import numpy as np

#--- CREACION DE UN DATAFRAME ----
df= pnd.read_csv("datasetnotas.csv" , header=0 , sep=";")
calificaciones=list(df["informatique"])
observaciones = pnd.DataFrame({'NOTAS': calificaciones})

#--- ANALISIS DE UNA CARACTERISTICA ---
stats = jmp.JMPEstadisticas(observaciones['NOTAS'])
stats.analisisCaracteristica()