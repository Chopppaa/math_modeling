a=int(input())
b=int(input())

if b==0 :
   print('chisla ne delyatsa')
elif a % b ==0:
    print(a/b)
else:
    print(a//b,',', a%b)