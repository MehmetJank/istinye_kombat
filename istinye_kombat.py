#İstinye Üniversitesi BIL101 Temel Programlama 1 (Python) mini proje 2.
#"BIL101_Temel_Programlama_1_MP2.pdf" yönergesine göre yazılmıştır.

from random import randint, choice  

# Burada koduma güzellik katsın diye ASCII art ekledim.
print("""
╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗  ╔╦╗╔═╗  ╔╦╗╦ ╦╔═╗  
║║║║╣ ║  ║  ║ ║║║║║╣    ║ ║ ║   ║ ╠═╣║╣   
╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝   ╩ ╚═╝   ╩ ╩ ╩╚═╝  
╦╔═╗╔╦╗╦╔╗╔╦ ╦╔═╗  ╦╔═╔═╗╔╦╗╔╗ ╔═╗╔╦╗     
║╚═╗ ║ ║║║║╚╦╝║╣   ╠╩╗║ ║║║║╠╩╗╠═╣ ║      
╩╚═╝ ╩ ╩╝╚╝ ╩ ╚═╝  ╩ ╩╚═╝╩ ╩╚═╝╩ ╩ ╩      """)

def game_start():  # <-- Oyunun tamamını içeren fonksiyon:
    hyphen = 15 * "-"
    user_1 = str(input(f"{hyphen} İlk Kahraman {hyphen} \n Lütfen kahramanınızın adını yazın: "))
    user_2 = str(input(f"{hyphen} İkinci Kahraman {hyphen} \n Lütfen kahramanınızın adını yazın: "))

    while user_1 == user_2:  # <-- Burada while kullanarak kullanıcıların aynı isimleri almamalarını sağladım.
        print(user_1, "alındı, lütfen başka bir isim seçin!")
        user_2 = str(input(f"{hyphen} İkinci Kahraman {hyphen} \n Lütfen kahramanınızın adını yazın: "))
    user_list = [user_1, user_2]
    starting_user = str(choice(user_list))  # <-- Bir üst satırda oluşturduğumuz kullamnıcıları barındıran
    # listeden %50 şansla ilk başlayacak oyuncuyu seçiyoruz.

    if starting_user == user_2:  # <-- Kullanicilari değiştirdim bkz. 47.satır
        temp = user_2
        user_2 = user_1
        user_1 = temp
    else:
        pass
    print(f"\n\nYazı tura sonucu: {starting_user} önce başlar.")

    user_1_len = len(user_1)
    user_2_len = len(user_2)
    user_1_health = 100
    user_2_health = 100

    print('{}:\n{}'.format(user_1, 2 * user_1_len * '-'))  #<-- Kullanıcıların canlarının yazdırılıdığı kısım
    print('HP[{}]:{}\n'.format(user_1_health, user_1_health // 2 * '|'))
    print('{}:\n{}'.format(user_2, 2 * user_2_len * '-'))
    print('HP[{}]:{}\n'.format(user_2_health, user_2_health // 2 * '|'))

    while not user_1_health < 1 and not user_2_health < 1: #<-- Oyunu döngüye soktuğum kısım.
        print(10*"-",user_1,"Saldır!",10*"-")
        attack_strength = int(input(f'{user_1} Saldırı büyüklüğünüzü 1 ile 50 arasında seçin: '))
        while attack_strength <= 0 or attack_strength > 50:
            print('Saldırı büyüklüğü 1 ile 50 arasında olmalıdır.')
            attack_strength = int(input(f'{user_1} Saldırı büyüklüğünüzü 1 ile 50 arasında seçin: '))

        percentage = randint(1, 100)              #<-- Vurma şansını randint ile hesapladım allta 100den çıkardım.
        attack_accuracy = 100 - attack_strength
                                                #<-- Kodumu kısa tutmak için sürekli user_1 saldırtırdım ve
        if percentage < attack_accuracy:        # kullanıcıları sürekli değiştirdim bkz. 60.satır.
            print(f'{user_1}: {attack_strength} kadar hasar verdi:\n\n')        
            user_2_health -= attack_strength
        else:
            print(f'"Ooopsy! {user_1} saldırıyı kaçırdı.\n\n')
        if user_1_health <= 0:              # <-- Canlar 0 dan aşağı inerse eksi göstermemek için sıfıra eşitledim.
            user_1_health = 0
        if user_2_health <= 0:
            user_2_health = 0
        print('{}:\n{}'.format(user_1, 2 * user_1_len * '-'))
        print('HP[{}]:{}'.format(user_1_health, user_1_health // 2 * '|'))
        print('{}:\n{}'.format(user_2, 2 * user_2_len * '-'))
        print('HP[{}]:{}'.format(user_2_health, user_2_health // 2 * '|'))
        temp = user_2  
        user_2 = user_1
        user_1 = temp
        
        tmp = user_2_health               # <-- Canlar da aynı userlar gibi değişiyor.
        user_2_health = user_1_health
        user_1_health = tmp
        hashtag = 50*("#")
        if user_2_health <= 0:
            print(hashtag,user_1,"Kazandı",hashtag)          #<-- Kimin kazandığını çıktı olarak verdim.
        elif user_1_health <= 0:
            print(hashtag,user_2,"Kazandı",hashtag)

    while user_1_health == 0 or user_2_health == 0:           #<-- Kullanıcılardan birinin canı sıfıra eşitlendiğinde oyun yeniden oynayıp oynamamak istediklerini soracaktır.  
        soru = input("Bir tur daha oynamak ister misiniz (E/H)? : ")
        if soru.lower() == "e":
            game_start()
            break
        elif soru.lower() == "h":
            print("Oynadığınız için teşekkürler! Tekrar görüşürüz!")
            break
        else:
            print(f'{soru}: tanınmayan opsiyon tekrar deneyin.')

def first_Start():          #<-- oyunu ilk kez başlatmamı sağlayan fonksiyon :D.
    for i in range(1): 
        i += 1
        game_start()

first_Start()

