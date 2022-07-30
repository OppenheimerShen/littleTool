import random

first_round_list=list(range(1,34))
return_list=[]

for i in range (6):
   a=random.randint(1, len(first_round_list))
   return_list.append(first_round_list[a-1])
   del first_round_list[a-1]

for i in range(1):
   a=random.randint(1, 16)
   return_list.append(a)

print(return_list)