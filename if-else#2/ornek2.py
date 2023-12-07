print("""
========== KULLANICI GIRISI ==========
""")
user_id = "mehmet"
user_password = "1234"

kullanici_id = input("kullanici adi giriniz: ")
kullanici_password = input("parola giriniz: ")

if user_id == kullanici_id and user_password != kullanici_password:
    print("parolaniz hatalidir...")
elif user_id != kullanici_id and user_password == kullanici_password:
    print("kullanici adiniz hatalidir.")
elif user_id != kullanici_id and user_password != kullanici_password:
    print("kullanici adiniz ve parolaniz hatalidir.")
else:
    print("giris basarili.")
