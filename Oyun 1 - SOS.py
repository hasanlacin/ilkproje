# Önce ekrana oyun tahtası olarak şu şekli bastıracak
#               ---  ---  ---
#               ---  ---  ---
#               ---  ---  ---
# Sonra oyun başlar. Önce 1.oyuncu (O), sonra 2.oyuncu (X) hamle yapar.
# "1.oyuncu oynuyor : O"
# "yukarıdan aşağıya [1,2,3]:"
# "soldan sağa [1,2,3]:
# şeklinde iki defa sorarak oyuncunun hangi kareyi işaretlemek istediği alınır.
# O kare dolu ise, "Burası doludur, başka bir yer dene" uyarısı verecek.
# Kare müsait ise sıradaki oyuncunun işaretini bu kareye yerleştirecek
# Ardından tahtayı tekrar ekrana basacak ve sonraki hamle için yine başa dönecek.
# Soldan sağa veya yukarıdan aşağıya kendi harflerini doldurabilen oyuncu oyunu kazanır.
# "1.OYUNCU KAZANDI!..."
# Tahta dolduğu halde kimse kazanmaz ise "KİMSE KAZANAMADI" diyerek oyunu bitirecek.


tahta = ["---", "---", "---"]


for a in tahta:
    print(*tahta)


sayac = 0
while True:
    sayac = sayac + 1

    if(sayac % 2 == 0):
        print("Sıra 1.oyuncuda (S)")
    else:
        print("Sıra 2. oyuncuda(O)")

    if(sayac != 1):
        kelime = input("")
        if(kelime == "ç"):
            quit()











