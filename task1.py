
def append_two_list(l1,l2):
    for index,item in enumerate(l2):
        if(index%2!=0):
            l1.append(l2[index])
    print(l1)

list_a=[1,2,3,4,5,6]
list_b=[10,20,30,40,50,60]
# list_b=[item for item in range(1,70)  if item % 2 == 0 if item % 5==0]
# list_a=[ items for items in range (1,len(list_b))]
# list = [x for index , x in enumerate(list_b) if ind % 2!=0]
print(list_a)
print(list_b)
append_two_list(list_a,list_b)

