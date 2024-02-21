def migratoryBirds(arr):
    bird_count = [0, 0, 0, 0, 0]
    for bird in arr:
        bird_count[bird-1] += 1
    return bird_count.index(max(bird_count)) + 1


if __name__ == 'main':
    arr=[1, 4, 4, 4, 5, 3]
    print(migratoryBirds(arr)) # 4