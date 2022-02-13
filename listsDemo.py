cars = ['BMW','MERCEDES','OPEL','MAZDA']
result = len(cars)

result = cars[0]
result = cars[3] #3yerine -1 de olur => mazda

cars[-1] = 'Toyota'
result = cars

result = 'MERCEDES' in cars #MERCEDES cars'ın bir elemanı mıdır içinde midir?

result = cars[-2]

result = cars[0:3] # 0dan 3ekadar git
result = cars[:3] # aynısı
result = cars[-2:] 

cars[-2:] = ['Toyota', 'Reno']
result = cars

result = cars + ['audi', 'nissan']

del cars[-1] #son elemanı siler
result = cars

result = cars[::-1] #tersten git

print(result)