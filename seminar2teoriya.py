"""""""""
def sub(a,b):
    print(a-b)
sub(a-b)

def sub(a,b):
    return(a-b)
s=sub(a-b)
print(sub())
""" " "


'''''''''''
#строки
s="Hello world"
a=s[0:5] #Hello
a=s[0:7:3] # шаг 3
print(s[2]+s[4]+s[3]+' '+s[6:])
m=s.split(' ') #['My','name','is','Mary']=A
print(m)
print(' '.join(m))
print(''.join(m))
st='redgreenred'
st=st.find('green') #3 rfind-последнее
f='sdfgkhsdgfsdua'
f.replace('g','G')
c=f.count('a')
'''''''''

'''''''''''
#Массивы
#a=[]
#a=list() - пустые массивы
a =[]
a.append('f') #dobavlenie elementa
b=[]
n=int(input())
for i in range(n):
    b.append(input())
print(b)
N=[0]*5
#for a in N:
    #print(a)

#enumerate - разбивает на 2 массива индексы и элементы
#for i,e in enumerate(N):
    #print(i,e)

#zip
#for x,y zip(s,m)
    #print(x,y)

#pop-удаляет последний элемент и возвращаем значение

#pop(index)-по индексу

#insert(index, element)

#extend
'''''''''''




s=int(input())
a=[]
for i in range(s):
    a.append(input())
n=input('Что найти ')
col=0
v=0
for u in range(s):
    if a[u]==n:
        print(u)
        break

