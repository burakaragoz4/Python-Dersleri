# error handling => Hata Yönetimi 

# try:   
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(f"Cevap: {x/y}")
# except (ZeroDivisionError,ValueError) as e :
#     print("Yanlış Değer Girdiniz.")
#     print
# except ZeroDivisionError:
#     print("Y İçin Sıfır Girilemez.")
# except ValueError:
#     print("X ve Y İçin Sayısal Değer Girmelisiniz.")
while True:
    try:   
        x = int(input("x: "))
        y = int(input("y: "))
        print(f"Cevap: {x/y}")
    except:
        print("Yanlış Değer Girdiniz.")
    else:
        print("Herşey Yolunda")
        break
    finally:
        print("Try except sonlandı...")