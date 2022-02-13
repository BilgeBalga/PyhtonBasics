import abc


website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

print(len(course)) #kaç karakter olduğu

# www karakterlerini alın
print(website[7:10])

#com karakterlerini alın
print(website[22:25])
length = len(website)
print(website[length-3:length])

#course içerisinden ilk 15 ve son 15 karakterlerini alın
print(course[0:15])
print(course[:15])
result = course[-15:]

# course karakterlerini tersten yazdırma
print(course[::-1])


s = '12345' * 5
print(s[::5]) # 5 karakterde bir al 11111

#hello world ifadesindeki w harfini W ile değiştir
s = 'Hello World' 
s = s[0:6] + 'W' + s[-4:]

print(s)
s.replace('w','W') # w gördüğün yeri W yap


# 'abc' ifadesini yan yana 3 defa yazdırın.
ornek = 'abc ' * 3
print(ornek)
