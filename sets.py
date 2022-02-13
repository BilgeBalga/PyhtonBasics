fruits = {'orange', 'apple', 'banana'} 

# print(fruits[0]) #indekslenemez

for x in fruits: # x içine fruits kopyaladı ve liste olarak yaptı
    print(x)

fruits.add('cherry')   
fruits.update(['mango','grape']) #rastgele koyar. apple eklemeye çalışırsan tekrar eklenmez.

print(fruits)

# myList = [1,2,5,4,4,2,1]
# print(myList)
# print(set(myList)) #tekrarlayan elemanları liste içerisinden çıkarır => çıktı => {1,2,4,5}


fruits.remove('mango') # mangoyu siler

fruits.discard('apple') # apple siler

fruits.clear() # tüm elemanlar silinir.

#fruits.pop() #normalde son elemanı siliyor ama fruit listelenmemiş olduğu için hangisini sileceği belli olmaz.



