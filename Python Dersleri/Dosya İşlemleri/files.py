# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi, dosya_erişme_modu).
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# ****** "w": (Write) yazma modu. Dosya konumda oluşturur.  
#        Dosyayı Konumda Oluşturur
#       Dosya içeriğini siler ve yeniden ekleme yapar


# file = open("newfile.txt","w")
# file = open("C:/Users/karag/OneDrive/Masaüstü/newfile.txt","w")
# file.close()

# file = open("newfile.txt","w",encoding="utf-8")
# file.write("Burak Karagöz")
# file.close()

# ****** "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# file = open("newfile.txt","a",encoding="utf-8")
# file.write("\nBurak Karagöz")
# file.close()


# ****** "x": (Create) Oluşturma. Dosya zaten varsa hata verir.
# file = open("newfile2.txt","x",encoding="utf-8")

# "r": (Read) okuma. Dosya konumda yoksa hata verir.
# file = open("newfile.txt","r",encoding="utf-8")
# print(file.read())
