import random
random_numbers=[]
for i in range(20):
 a=random.randint(1,100);
 random_numbers.append(a)
print(random_numbers)
statistics=[]
average=statistics.mean(random_numbers)
print("Average of the list elements:{average}")
