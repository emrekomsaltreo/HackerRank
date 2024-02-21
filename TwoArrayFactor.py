def getTotalX(a, b):
    min_value, max_value = min(a), max(b)
    value = 0
    for k in range(min_value, max_value + 1):
        if all((k%i == 0) for i in a): 
            if all((i%k == 0) for i in b):
                value += 1
    
    return value

if __name__ == "__main__":
    a = [2, 6]
    b = [24, 36]

    print(getTotalX(a, b))