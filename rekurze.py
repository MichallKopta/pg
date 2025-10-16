def faktorial(n):
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n-1)

def for_faktorial(n):
    result = 1
    for i in range(n):
        result *= n
        n-=1
    return result

        
        

if __name__ == "__main__":
    #print(faktorial(0))
    #print(faktorial(1))
    #print(faktorial(5))
    #print(faktorial(100))
    print(for_faktorial(10))