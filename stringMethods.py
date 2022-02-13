message = ' Hello There. My name is Bilge'

#message = message.upper() #message değişkeninde bulunan sonucun hepsini BÜYÜK harfe çevirir.

#message = message.lower() #message değişkeninde bulunan sonucun hepsini KÜÇÜK harfe çevirir.

#message = message.title() #Her kelimenin BAŞ harfi BÜYÜK harfe çevrili

#message = message.capitalize() #sadece ilk kelimenin ilk harfini büyük harf yapar  

message = message.strip() #baştaki boşluk karakteri gider.

'''message = message.split() '''
 # her bir kelime boşluk karakterlerinden itibaren bölünür
#çıktısı şöyle => ['Hello', 'There', 'My', 'name', 'is', 'bilge',]
 

print(message[0]) # hello gelir split sayesinde.

#message = message.split('.') #noktalardan ayırır.

#message = ' '.join(message) #parça parça olan kelimeleri birleştirip aralara boşluk ekler. '*' yıldız ekler.

#index = message.find('Bilge') # message içinde bilge var mı 
#isFound = message.startswith('H') #H ile mi başlıyor True bilgisi gelir

#isFound = message.endswith('n') n ile mi bitiyor

#message = message.replace('bilge','eylül') # cümle içerisinde bilgeyi bulur yerine eylül yazar

#message = message.center(100) 100 karakterlik bir bilgi içerisine alır
#message = message.center(50, '*')  sağına soluna ekler
print(message)


#STRİNG METODLARIN DAHA FAZLASINA ULAŞ GOOGLE string methods pyhton yaz. incele