def refund(oneLiter, biggerOneLiter):
    return ((oneLiter*.1)+(biggerOneLiter*.25))

def main():
    print("Refund calculator")
    print("How many 1 liter bottles are you returning?")
    oneLiter = input()
    while float(oneLiter) < 0:
        print("Please type a positive number:")
        oneLiter = input()

    print("How many bottles bigger than 1 liter are you returning?")
    biggerOneLiter = input()
    
    while float(oneLiter) < 0:
        print("Please type a positive number:")
        biggerOneLiter = input()
    #format to show 2 decimals
    print("The total refund is: ","{:.2f}".format(refund(float(oneLiter),float(biggerOneLiter))))

main()
    



