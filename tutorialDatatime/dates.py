import datetime

# t = datetime.time(1, 2, 3)
# print(t)
# d = datetime.date(2016,7,24)
# print(d)
tday = datetime.date.today()
# print(tday.year)
# print(tday.day)
# #imprimir el día, lunes = 0 como en mi caso
# print(tday.weekday())
# #isoweekday retona lo mismo pero cuenta el lunes como 1
# print(tday.isoweekday())

#se le suman siete dias a la fecha que se obtiene
tdelta = datetime.timedelta(days=7)
#print(tday + tdelta)
#se le restan 7 dias a la fecha que se obtiene
#print(tday - tdelta)
#saber cuanto queda para mi cumpleaños
bday = datetime.date(2020, 2, 14)
till_bday = tday - bday
print (till_bday)
