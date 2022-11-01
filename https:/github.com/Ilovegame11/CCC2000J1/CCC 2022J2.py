x = []
c = []
count = 0
z = int(input())
for i in range(z*2):
    x1 = int(input())
    x.append(x1)
for i in range(0,z*2,2):
    c.append(x[i]*5-x[i+1]*3)
for i in range(len(c)):
    if c[i]>40:
        count+=1
if count == z:
    print(str(z)+'+')
else:
    print(count)
