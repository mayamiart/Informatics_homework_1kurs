def factorize(x):
    s=[]
    c=0
    for i in range(1,x+1):
        if x%i==0:
            for y in range(len(s)):
                if s[y]==i or s[y]==x//i:
                    c+=1
            if c>1:
                break
            s.append(i)
            s.append(x // i)
            print(i, x//i)
g=int(input())
factorize(g)