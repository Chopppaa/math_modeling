a=int(input('vvedite 1 otrezok'))
b=int(input('vvedite 2 otrezok'))
c=int(input('vvedite 3 otrezok'))


if a<b+c and b<a+c and c<a+b:
    print('treugolnik suschestvuet')
elif a==b==c:
    print('treugolnik rawnostoronniy')
elif a==b or b==c or c==a:
    print('treugolnik rawnobedrenniy')
elif a!=b and a!=c or b!=c and b!=a or c!=a and c!=b:
    print('treugolnik raznostoronniy')
