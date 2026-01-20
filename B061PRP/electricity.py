def main():
    units = int(input("Enter the units of electricity used: "))
    
    if (units <= 100): 
        print("Bill is 100rs")
        
    elif (units > 100 and units < 200):
        
        bill = 100 + 2 * (units - 100) 
        print("Bill is", bill)
        
    elif (units == 200):
        print("Bill is Rs.300")
        
    else:
        
        bill = 300 + 3 * (units - 200)
        print("Bill is:", bill)


if __name__ == "__main__":
    main()