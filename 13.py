a=[1,1,2,3,4,3,0,0]
for i in a:
    if a.count(i)>1:
        a.remove(i)
        print(a)
