"""i=0
while(True):

    if i+1<5:
        i = i + 1
        continue
    print (i, end=" ")
    if(i==44):
        break
    i=i+1"""

while(True):
    i = int(input("enter a number\n"))
    if(i<=100):
        print("please enter a number greater than 100\n")
        continue
    else:
        break
print("Congrats!!, you have entered a number greater than 100\n")