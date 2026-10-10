n=int(input("Enter number of transactions: "))
p=set()
previous_timestamp=0
for i in range(n):
    sender,receiver,timestamp,amount=input("Enter sender,receiver,timestamp,amount: ").split(" ")
    time=int(timestamp)
    if(sender,receiver) in p:
        print("Duplicate transaction")
        break
    else:
        p.add((sender,receiver))
    if(i>0):
        if(time-previous_timestamp>60):
            print("fraud transaction")
            break
    else:
        previous_timestamp=time
else:
    print("valid transaction")

# p=78.999
# print('{:.2f}'.format(p))