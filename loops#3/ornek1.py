sys_user_id = "mehmetkr"
sys_user_password = "3445"
giris_hakki = 3

while True:
    user_id = input("kullanici adinizi giriniz: ")
    user_password = input("parolanizi giriniz: ")

    if (user_id == sys_user_id and user_password != sys_user_password):
        print("Parolaniz hatalidir...")
        giris_hakki -= 1
    elif (user_id != sys_user_id and user_password == sys_user_password):
        print("Kullanici adiniz hatalidir...")
        giris_hakki -= 1
    elif (user_id != sys_user_id and user_password != sys_user_password):
        print("Kullanici adiniz ve parolaniz hatalidir...")
        giris_hakki -= 1
    else:
        print("Giris basarilidir...")
        break
    if (giris_hakki == 0):
        print("Giris hakkiniz kalmamistir...")
        break
