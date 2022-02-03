# with open("newfile.txt","r+",encoding="utf-8") as file :
#     file.seek(50)
#     file.write("denemeee")
# with open("newfile.txt","r+",encoding="utf-8") as file :
#     print(file.read())



# ************** SAYFA SONUNDA GÜNCELLEME *******************
# with open("newfile.txt","a",encoding="utf-8") as file :
#     file.write("\nEmel Turan")
# ************** SAYFA SONUNDA GÜNCELLEME *******************




# ************** SAYFA BAŞINDA GÜNCELLEME *******************
# with open("newfile.txt","r+",encoding="utf-8") as file :
#         content = file.read()
#         content = "Efe Turan\n" + content 
#         file.seek(0)
#         file.write(content)
# with open("newfile.txt","r+",encoding="utf-8") as file :
#         print(file.read())
# ************** SAYFA BAŞINDA GÜNCELLEME *******************





# ************** SAYFA ORTASINA GÜNCELLEME *******************
with open("newfile.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(4,"Yılmaz Aygün\n")
    file.seek(0)
    file.writelines(list)
   
with open("newfile.txt","r",encoding="utf-8") as file :
    print(file.read())

# ************** SAYFA ORTASINA GÜNCELLEME *******************
