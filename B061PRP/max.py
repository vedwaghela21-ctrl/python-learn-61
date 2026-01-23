def main():
    pre = [2,4,3,2,3,5,6,2]
    count = 0
    max = 0
    for i in range(0,len(pre),1):
        temp = pre[i]
        for j in range(i,len(pre),1):
            if pre[j]==temp:
                count+=1
        if max < count:
            max = count
        count = 0
    print("Maximum frequency is: ",max)

if __name__ == "__main__":
    main()