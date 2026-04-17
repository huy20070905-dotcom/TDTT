a=input()
a+=" "
c=""
i=0
while(i<len(a)-1):
  dem=1
  k=i
  if(a[i]==a[i+1]):
   for j in range(i,len(a)-1):
    
    if(a[j]==a[j+1]):
      dem+=1
    else:
      
      break
    k=j+1
  
    
  i=k
  if(i==len(a)-1 and a[i]==' '):
    dem-=1
  c+=chr(dem+48)+a[i]
  i=i+1
  
print(c)