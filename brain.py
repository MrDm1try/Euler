def b(p):a=[0]*30000;i=0;c=list(p);_b(a,i,c)
def _b(a,i,c):
 while c:
  g=c[0]
  if g=='>':i+=1
  elif g=='<':i-=1
  elif g=='+':a[i]+=1
  elif g=='-':a[i]-=1
  elif g=='.':print(chr(a[i]),end='')
  elif g==',':a[i]=int(input())
  elif g=='[':
   f=0;n=0
   for j in range(1,len(c)):
    if c[j]=='[':n+=1
    elif c[j]==']':
     if n:n-=1
     else:f=j;break
   while a[i]:_b(a,i,c[1:f])
   del c[:f]
  del c[0]