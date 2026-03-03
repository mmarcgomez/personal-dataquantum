import calendar
from calendar import month
from datetime import datetime, timedelta, date
import locale

from dateutil.relativedelta import relativedelta

#fecha = input('Dime una fecha (dd/mm/aaaa): ')

#fecha = datetime.strptime(fecha,'%d/%m/%Y')

undiamas = timedelta(days=1)

locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

# Obtiene todos los jueves del mes #################################################################
#**while fecha.strftime("%A").capitalize() != 'Jueves':
#    fecha = fecha + undiamas
#sietediasmas = timedelta(days=7)
#mes = fecha.month
#while fecha.month == mes:
#    print('Fecha: '+ fecha.strftime("%d %B %Y").upper())
#    fecha = fecha + sietediasmas
####################################################################################################
# Introducir un año, para cada uno de los meses del año, decir el último viernes de cada mes
anio = int(input("Introduce un año: "))

for mes in range(1, 13):

    # Obtener el último día del mes
    ultimo_dia = calendar.monthrange(anio, mes)[1]

    fecha = date(anio, mes, ultimo_dia)

    # Retroceder hasta que sea viernes
    while fecha.weekday() != 4:  # 4 = viernes
        fecha -= timedelta(days=1)

    print("Último viernes de", fecha.strftime("%B"), ":", fecha.strftime("%d/%m/%Y"))

def fechas (fecha2:date):
    for i in range (1,13):
        fecha2 = fecha2.replace(month=i)
        print(fecha2.strftime("%B").capitalize()+" "+
              ultimoViernes(fecha2).strftime())

def ultimoViernes(fecha:date):
    unmesmas = relativedelta(month=1.-1)
    undiamenos = timedelta(days=-1)
    fecha = fecha+unmesmas+undiamenos
    return fecha

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
    anno = int(input("Introduce un año: "))
    f= date(anno,1,1)
    fechas(f)