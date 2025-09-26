a=['1','1']
n=int(input('Введите до какого числа нужно '))
for i in range(1,n-1):
    a.append(str(int(a[i-1])+int(a[i])))
print(' '.join(a))