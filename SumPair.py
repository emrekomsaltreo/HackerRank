def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            if (ar[i] + ar[j]) % k == 0 and i < j:
                print(ar[i], ar[j])
                count += 1
    return count

if __name__ == "__main__":
    arr = [1, 3, 2, 6, 1, 2]
    print(divisibleSumPairs(6, 3, arr)) # 3