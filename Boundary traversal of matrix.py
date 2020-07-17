#code
for _ in range(int(input())):
    m,n=map(int,input().split())
    k=list(map(int,input().split()))
    a=[]
    b=[]
    p=0
    for i in range(m):
        for j in range(n):
            a.append(k[p])
            p+=1
        b.append(a)
        a=[]
    res=[]
    if(b):
        if b[0]:
            res+=b.pop(0)
        if b and b[0]:
            for i in b:
                res.append(i.pop())
        if b and b[-1]:
            res+=b.pop()[::-1]
        if b and b[0]:
            for i in b[::-1]:
                res.append(i.pop(0))
    print(*res)
