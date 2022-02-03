import os
import datetime

# result = dir(os)
# result = os.name

# DİZİN DEĞİŞTİRME
#os.chdir('C:\\')
# os.chdir('..')
# os.chdir('..')
# os.chdir('..')
# os.chdir('..')
# os.chdir('../..')

# KLASÖR OLUŞTURMA
#os.mkdir("new directory")
#os.makedirs("new directory/yeniklasör")

# ETKİN DİZİNİ ÖĞRENME
# result = os.getcwd()

# LİSTELEME
# result = os.listdir()
# result = os.listdir('C:\\') # C Dizinindekileri göstermeye yarar
# for dosya in os.listdir():
#     if (dosya.endswith(".py")):
#         print(dosya)
result = os.stat("newfile.txt")
#result = result.st_size/1024
result = datetime.datetime.fromtimestamp(result.st_ctime)
print(result)