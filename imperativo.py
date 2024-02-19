from locale import setlocale, LC_ALL
from calendar import mdays, month_name


#Portugues do Brasil
setlocale(LC_ALL,'pt_BR')


#listar todos os meses do ano com 31 dias
print('Meses com 31 Dias')
for mes in range(1, 13):
    if mdays[mes] == 31:
        print(f'-{month_name[mes]}')