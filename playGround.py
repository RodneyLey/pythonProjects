#loops
count = 0
while count < 10:
    print (count)
    count  += 1

print ("End")


for x in range(10):
    print (x)
#enumerate = meaning ==> to give a number to a list
items = [1,2,3,4]
for  item in enumerate(items):
    print(item)

#break & continue
#continue skips  that particular item,
#break call off the whole loop 
items = [1,2,3,4]
for index, item in enumerate(items):
    if index == 1:
        continue
    print(index,item)
