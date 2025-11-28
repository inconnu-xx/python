#STRİNG (metinsel veriyi tutan kavram)
print("hello cruel world!")
#print fonksiyondur. string iki tırnak icine yazılır. kilimede tek tırnak yoksa tek tırnak icine de yazılır.
#illa tek tırnak kullanacaksak \ (ters slash) kullanırız. kendinden sonraki karakterin işlevini yok sayar.
#"""""" üç tırnağın icine ne yazarsak cıktıyı aynı şekilde verir. \n enter dir, \t tab dır yani bosluk.
#-------
#değişken, mesajımızı makinenin aklında tutmasını sağlar.
not1 = "merhaba"
not2 = "dunya"
print(not1 + not2)
print(not1 + " " + not2)
#bosluk birakmak icin " " yazarız, bu boşluk ta bir stringdir.
#stringlerde toplama işlemi yanyana yazmak anlamına gelir
#carpma işlemi de yanyana yazar
print(not1 * 5)
#-------
# bir stringin icindeki belirli bir harfi elde etmek icin 
print(not1[0])
# yazılımda saymaya 0 dan baslarız, 0, birinci harf olan m dir
print(not1[-1])
#-1 sondan birinci karakteri döndürür
#-------
# belirli bir kısmı yazdırmak icin
print(not1[0:4])
# sıfırıncı ile dördüncü karakterin arasını yazdırır. birinci sınır dahil, ikinca sınır dahil değil!
#-------
print(not1[::2])
# ilk parametreyi ve ikinci parametreyi boş bırakırsak, ilki en başı ikinciyi en sonu olarak alır.
# sona da iki yazarsak kelimeyi iki iki yazdırır. 2 yerine birşey yazmazsak defauld olarak 1 kabul eder.
#-------
# eğer son parametreyi -1 yaparsak, tersten yazdırır. çünkü varsayılan değerlerin yeri değişir.
print(not1[::-1])
#-------
# string metodları
print(not2.upper())  
#büyük harf metodu. tek sefer icin büyütür yani yeni metini büyük yazar. kalıcı olması icin bunu yeni değişkene atayın.
print(not2)
buyuk = not2.upper() #artık kalıcı büyük olur
print(buyuk)
print(buyuk.lower()) #büyük olan yazıyı kücültür
print(buyuk.capitalize()) #ilk harfi büyütür
print(not1.startswith("m")) #kelime m ile mi başlıyor. örn. a ile başlayanları bulmak icin.
print(not1.endswith("m")) #kelime m ile mi bitiyor
print(len(not1)) #kelimem kac harfli. (saymaya sıfırdan baslar)
print(len(not1 + not2)) #örn.
#-------
# f string 
#stringin icine değer (değisken) gömmeye yarar. string içinde python kodu çalıştırarak dinamik metin yazmanın en temiz hali.
#parantezin icine, iki tırnağın dısına f yazarız ve değer gireceğimiz yere {} küme parantezi yazariz.
yas = 23
meslek = "tüccar"
print(f"{yas} yaşındayım, {meslek} olarak calişiyorum.")
#-------
#minik motive konuşması
# şuana kadar ögrendiklerinizi mutlaka yazarak ve uygulayarak deneyin. bunlar sıkıcı ama en temel bilgiler.
#tam oturtulmadan üstten gecilirse ilerde en basit kodu anlamadığınız icin oturup bir köşede ağlamanız olası bir durumdur.
#şuan bu bilgiler ile ekrana birşeyler yazdırmak dışında pek birşey yapamasakta döngülere geldiğimizde daha eğlenceli
#hale gelecektir ve birşeyler ortaya cıkınca dahada motive olacaksınız.

#--------------------------------------------------------------------

#İNTEGER, FLOAT. (tam sayı, ondalık sayı)
#integer ve float tipleri tırnak icinde yazmaya gerek yoktur cünku makine sayılarla calişir ve sayının sayı olduğunu anlar.

sayi1 = 3
sayi2 = 2.7

print(sayi1)

#type fonksiyonu, değerin tipini gösterir. (int, float, str)
print(type(sayi1))

#5 üzeri 100 sonucu bulmak icin (kuvvet alma)
uzeri = 5 ** 100
print(uzeri)

#bölme işlemi icni
bolu = 30 / 8
print(bolu)

#---------

#MATEMATİKSEL İŞLEMLER (integer ve floatta calişir)

#toplama "+"
print(7 + 3)
print(7 + 3.5)

#cıkartma "-"
print(7 - 3)
print(7 - 3.5)

#carpma "*"
print(7 * 3)
print(7 * 3.5)

#bolme "/"
print(7 / 3)
print(7 / 3.5)

#tamsayı bolme "//"
print(7 // 3)
print(7 // 3.5)

#kuvvet alma "**"
print(7 ** 3)
print(7 ** 3.5)

#mutlak değer "abs"
print(abs(-12))
print(abs(-12.5))

#yuvarlama "round"
print(22/7) #kusuratlı böler
print(round(22/7)) #hangi tam sayıya yakınsa ona yuvarlar

print(5.8625485215565) #kusuratlı yazar
print(round(5.8625485215565)) #angi tam sayıya yakınsa ona yuvarlar

#kac basamak yazdırmak istersek ikinci parametre olarak girelim
print(round(5.8625485215565, 5)) #tam sayıdan sonraki 5 basamagida yazdırır. basamakları da yuvarlar örn. 879 = 88

#----------

#İSLEM ÖNCELİĞİ
#günlük hayattaki gibi önce parantez ici sonra carpma ve bölme sonra toplama ve cıkarma. örn.
print(3 * 5 + 6)
print(3 + 5 * 6)
print((3 + 2) * 4 + 3)

#---------

#KARŞILAŞTIRMA OPERATÖRLERİ

karsilastir1 = 5
karsilastir2 = 10

#esit mi (2 degeri vardır, true, false)
print(karsilastir1 == karsilastir2)

#esit degil mi (true, false)
print(karsilastir1 != karsilastir2)

#kucuk mu (true, false)
print(karsilastir1 < karsilastir2)

#buyukmu (true, false)
print(karsilastir1 > karsilastir2)

#kucuk esittir (true, false)
print(karsilastir1 <= karsilastir2)

#buyuk esittir (true, false)
print(karsilastir1 >= karsilastir2)

#-------

#int fonksiyonu, sayıya cevrilebilecek degerleri sayıya cevirir.

yuz1 = "100"
yuz2 = 100

print(int(yuz1) == yuz2)
print(str(yuz2) == yuz1)

#normalde int ve str esit değildir, bu örnekte esitliyoruz
#(int, sayıyının sadece tam kısmını alır, ondalık kısmı yoksayar)
#int fonk. tersi str fonk. tur, değeri stringi cevirir

#bunları güzel tekrar yapmak ve oturtmak gerekir

#------------------------------------------------



