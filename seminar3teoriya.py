#форматирование строк
'''''''''
a=int(input())
b=int(input())
S=a+b
print('sum of',a,'and',b,'is',S)
'''''''''
#str = 'Name {}, email {} , phone {}'.format(name,email,phone)
#str2 = 'Name %s, email %s, phone %s' %(name,email,phone)
#str3 = f'Name{name},email{email},Phone{phone}' #f-stroka
#for i in range(11):
#    print(f'{i} squarted is {i*i}')
'''''''''
import math
pi=math.pi
print(f'{pi:.34f}')
'''''''''
#работа c файлами
f = open('primer.txt','r')
print(f.read())


