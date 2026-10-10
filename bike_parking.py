try:
    n=int(input())
    if(n>0):
        if(n<=2):
            print(100*n)
        elif(n>=3 and n<=5):
            print(200+(n-2)*50)
        else:
            print(350+(n-5)*25)
    else:
        print("Invalid input")
except:
    print("Invalid input")
    