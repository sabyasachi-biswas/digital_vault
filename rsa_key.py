import random

p=int(input())
q=int(input())
print("p and q are",p,q)
n=p*q
print("N is",n)
phi = (p-1)*(q-1)
print("phi is ",phi)


def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p
def is_coprime(x, y):
    if gcd(x, y) == 1:
        return x
list=[]
for i in range (2,phi):
    if is_coprime(i,phi) != None:
        list.append(is_coprime(i,phi))
print(list)
e=random.choice(list)
print("e is",e)
# for e in list:
for k in range (0,e):
    d=(1+(k*phi))/e
    if d.is_integer():
        print("d is",d)