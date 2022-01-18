a=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
liste=[]
for i in a:
   if type(i)==list:
      for j in i:
         if type(j)==list:
            for k in j:
               liste.append(k)
         else:
            liste.append(j)
   else:  
      liste.append(i)          
print(liste)