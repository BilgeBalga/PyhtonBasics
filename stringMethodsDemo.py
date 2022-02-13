website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

message = ' Hello World '
message = message.strip() #boşluk karakterlerini sildi
print(message)
#soldaki boşluk karakterlerini silmek istersen .lstrip()
#sağdaki boşluk karakterlerini silmek istersen .rstrip()

# website = website.lstrip('/:pth') 
# print(website)

result = 'www.sadikturan.com'.strip('w.moc')
print(result)

course = course.lower() #hepsini küçük harfe çevirir
print(course)

website = website.count('a') # kaç tane a karakteri kullanılmış
print(website)
        #website = website.count('www',0,10) #0. index ile 10. index arasında kaç tane kullanılmıştır.

'''sonuc = website.startswith('www') '''
#website ifadesi www ile başlıyor mu? Evet => True
#print(sonuc)

#sonuc2 = website.endswith('com')
#com ile bitiyor mu

#website içerisinde com var mı?
#result = website.find('com')

'''website = website.find('com',0,10)'''
#website içerisinde 0ile 10.index arasında com var mı?
#sağdan da aramaya başlayabilir website.rfind()
#website = website.index('com') find ile aynı rindex olarak da kullanılabilir
'''find ile index farkı= İNDEXTE aranan şey o arandığı yerde yok ise hata döndürür. '''

'''course = course.isalpha() #course içerisindeki karakterler alfabetik mi? '''


#deneme = '123'.isdigit() #sayılar alfabetik mi sırayla mı 

# result = 'Contents'.center(50,'*')
# print(result)
# result = 'Contents'.ljust(50,'*') #contents sola yaslar sağına yıldız ekler

 
bosluk = course.replace(' ', '-') #boşluk karakterlerinin yerine - ekler (' ','-',5) sadece 5karakteri değiştirir
print(bosluk)

#bosluk = course.replace(' ', '') # boşlukları siler

degistir = 'Hello World'.replace('World', 'There') 
print(degistir)

ayırma = course.split(' ') #boşluk karakterlerinden ayırdı
print(ayırma)
print(ayırma[2])