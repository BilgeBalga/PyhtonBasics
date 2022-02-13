numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val5 = numbers[3:6] #3-6 arası . dahil

numbers[4] = 40
print(numbers)

numbers.append(49) # en sona 49u ekler
print(numbers) 

numbers.insert(3,78) # istediğin konuma eklemek için insert. 3. indexe 78 eklenir
print(numbers)
#sondan bir önceye numbers.insert(-1, 30)

numbers.pop() # en sondaki elemanı siler
numbers.pop(0) # 0.indexteki elemanı siler

numbers.remove(49) # silmek istediğin karakteri vererek siler.

numbers.sort() #liste sayısal büyüklük olarak sıralanır
letters.sort() #alfabeye göre sıralar

numbers.reverse() # listeyi tam tersine çevirir
letters.reverse() # Zden Aya sıralar

print(len(numbers)) #11
print(len(letters)) #7

print(numbers.count(10)) #numbers üzerinde 10 kaç tane var =>2
print(letters.count('a')) #letters üzerinde a kaç tane var =>2

numbers.clear() # tüm elemanları siler.

#list method in python araştır.


val1 = min(numbers)
val2 = max(numbers) 
val3 = min(letters)
val4 = max(letters)
print(val1)
print(val2)
print(val3)
print(val4)

