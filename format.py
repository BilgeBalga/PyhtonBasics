name = 'Bilge'
surname = 'Balga'
age = 19

print('My name is {} {}'.format(name, surname))

print('My name is {1} {0}'.format(name, surname))# soyad başta ad sonda olur

print('My name is {s} {n}'.format(n=name, s=surname))

print("My name is {} {} and I am {} years old.".format(name, surname, age)) # tür dönüşümü yapılmasına ihtiyaç duyulmadı. age ='19'


result = 200 / 700
print('the result is {r:1.3}'.format(r=result)) 
#SAĞ:virgülden sonra 3 basamağı yazdırır. SOL:1karakterlik boşluk bırakır.

print(f"My name is {name} {surname} and I am {age} years old.")
#print("My name is {} {} and I am {} years old.".format(name, surname, age)) aynı

