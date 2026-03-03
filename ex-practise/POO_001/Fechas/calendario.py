import calendar
import locale

locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

anyio = int(input("Intduce el año: "))
mes = int(input("Introduce el mes: "))

print(calendar.month(anyio,mes))

