n = int(input())
a = input().split()
Unique_id=[]
Duplicate_id=[]
for i in a:
  if i not in Unique_id:
    Unique_id.append(i)
  else:
    Duplicate_id.append(i)
print(*Unique_id)    
