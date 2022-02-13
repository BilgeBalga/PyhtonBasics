# x = 5
# y = 10
# z = 20

x, y, z = 5, 16, 20

# x,y = y,x

y += 5  #x = x + 5
y -= 5  #x = x - 5
y *= 5  #x = x * 5
y /= 5  #x = x / 5
y %= 5  #x = x % 5 sadece tam kısmını istiyorsan // koy
y **= 5 #y üssü 5


values = 1,2,3,4,5
print(values)
print(type(values))

x, y, *z = values

print(x,y,z)

print(z[0]) #z dizi oldu list oldu.