import datetime
#para instalar pytz (manejo de horarios del mundo con python, fue "pip install pitz" en consola)
import pytz

#dt = datetime.datetime(2016,7,27,12,30,45,tzinfo = pytz.UTC)
#print(dt)

# dtUtcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dtUtcnow)

# dtMtn = datetime.datetime.now()
# dt_east = dtMtn.astimezone(pytz.timezone('America/Santiago'))
# print(dtMtn)

# imprime April 20, 2021
dtMtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
# print(dtMtn.strftime('%B %d, %Y'))

dtStr = 'July 26, 2016'
dt = datetime.datetime.strptime(dtStr, '%B %d, %Y')
print(dt)

#strftime transforma de datetime a String 
#strptime De String a datetime
#

# for tz in pytz.all_timezones:
#     print(tz)
# t  = datetime.time(1, 2, 3)
# print(t)
# d = datetime.date(2016,7,24)
# print(d)
#tday = datetime.date.today()
# print(tday.year)
# print(tday.day)
# #imprimir el día, lunes = 0 como en mi caso
# print(tday.weekday())
# #isoweekday retona lo mismo pero cuenta el lunes como 1
# print(tday.isoweekday())

#se le suman siete dias a la fecha que se obtiene
#tdelta = datetime.timedelta(days=7)
#print(tday + tdelta)
#se le restan 7 dias a la fecha que se obtiene
#print(tday - tdelta)
#saber cuanto queda para mi cumpleaños
#bday = datetime.date(2020, 2, 14)
#till_bday = tday - bday
#en segundos
# print (till_bday.total_seconds())

#datetime.time = horas, minutos, segundos, y microsegundos
#tday = datetime.time(9,30,45,100000)
#print(tday.microsecond)
# dt = datetime.datetime(2016,7,26,12,30,25,100000)

# # tdelta = datetime.timedelta(days = 7)

# # print(dt + tdelta)

# dtToday = datetime.datetime.today()
# dtNow = datetime.datetime.now()
# dtUtcnow = datetime.datetime.utcnow()
# print(dtToday,"\n",dtNow,"\n",dtUtcnow)
