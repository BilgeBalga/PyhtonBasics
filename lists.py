# message = 'Hello There. My name is Bilge Balga'.split()
# print(message[0]) => Hello gelir çünkü split bir listeye çevirir

'''my_list = [1,2,3]
my_list = ['bir', 2, True, 5.6]
print(my_list) '''

list1 = ['one', 'two', 'three'] 
list2 = ['four', 'five', 'six']

numbers = list1 + list2
print(numbers)
print(len(numbers)) #kaç eleman numbers

userA = ['Bilge', 19]
userB = ['Eylül', 19]
print(userA)
print(userB)

users = userA + userB # 3 indexli bir liste
print(users[1])

users = [userA, userB] # new list 1.öğe userA 2. öğe userB      # 1 indexli bir liste
print(users[1][1]) 
