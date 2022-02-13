#key - value

# 41 => kocaeli  34 => istanbul

# sehirler = ['kocaeli', 'istanbul']
# plakalar = [41,34]

# print(plakalar[sehirler.index('kocaeli')])
# print(plakalar[sehirler.index('istanbul')])

#print(plakalar['kocaeli']) =>41
#print(plakalar['istanbul']) =>34


''' plakalar = {'key' : 'value' } '''
# plakalar = {'kocaeli' : 41, 'istanbul' : 34 }

# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

# plakalar['ankara'] = 6
# print(plakalar['ankara'])
# print(plakalar)

# plakalar['kocaeli'] = 'new key'


users = {
    'sadikturan' : {
        'age' : 36,
        'roles' : ['user'],
        'email' : 'sadik@gmail.com',
        'phone' : '123456'
    },
    'cınarturan' : {
        'age' : 2,
        'roles' : ['user','admin'],
        'email' : 'cınar@gmail.com',
        'phone' : '234567'
    },
}
print(users['cınarturan']['roles'][0])