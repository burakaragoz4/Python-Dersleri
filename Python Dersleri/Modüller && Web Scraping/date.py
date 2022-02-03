from datetime import datetime, timedelta

# result = dir(datetime)
# result = dir(datetime.datetime)
# result = dir(datetime.date)

simdi = datetime.now()
# simdi = datetime.today()
# # print(simdi)

# result = datetime.now()
# result = simdi.year
# result = simdi.month
# result = simdi.day
# result = simdi.hour
# result = simdi.minute
# result = simdi.second

# result = datetime.ctime(simdi)
# result = datetime.strftime(simdi, "%Y") #YIL BİLGİSİ
# #result = datetime.strftime(simdi, "%X") #SAAT BİLGİSİ
# #result = datetime.strftime(simdi, "%d") #GÜN BİLGİSİ
# #result = datetime.strftime(simdi, "%A") #GÜN BİLGİSİ YAZI
# #result = datetime.strftime(simdi, "%B") #AY BİLGİSİ
# result = datetime.strftime(simdi,"%X %d %B %Y")
# print(result)

t = "27 April 2021 hour 10:12:30"
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year

birthday = datetime(1999,2,9,12,30,10)

result = datetime.timestamp(birthday) # saniye
result = datetime.fromtimestamp(result) #saniye to datetime
result = datetime.fromtimestamp(0)

result = simdi - birthday #timedelta 

#result = result.days
#result = result.seconds
# result = result.microseconds

result = simdi + timedelta(days = 10)

print(result)



# gun, ay, yil = t.split()
# print(gun)
# print(ay)
# print(yil)
