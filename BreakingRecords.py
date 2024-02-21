def breakingRecords(scores):
    min_score = scores[0]
    max_score = scores[0]
    min_count = 0
    max_count = 0
    for score in scores[1: -1]:
        if score < min_score:
            min_score = score
            min_count += 1
        if score > max_score:
            max_score = score
            max_count += 1
    return max_count, min_count


if __name__ == '__main__':
    arr = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    length = len(arr)

    print(breakingRecords(arr))

    