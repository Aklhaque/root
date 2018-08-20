n=int(input("no:"))
root=1
dif=root*root-n
dif=abs(dif)
while(dif>=0.000001):
    root=(root+(n/root))/2
    dif=root*root-n
    print("yur root:",root)
    dif=abs(dif)
else:
    print(root)
