def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        if sum(s[i:i+m]) == d:
            count += 1
    return count

if __name__ == 'main':
    arr = [2, 2, 1, 3, 2]
    print(birthday(arr, 4, 2))