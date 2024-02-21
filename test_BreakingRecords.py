def test_breakingRecords():
    # Test case 1: Scores in ascending order
    scores = [1, 2, 3, 4, 5]
    assert breakingRecords(scores) == (4, 0)

    # Test case 2: Scores in descending order
    scores = [5, 4, 3, 2, 1]
    assert breakingRecords(scores) == (0, 4)

    # Test case 3: Scores with repeated maximum and minimum values
    scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    assert breakingRecords(scores) == (2, 4)

    # Test case 4: Scores with no records broken
    scores = [10, 20, 30, 40, 50]
    assert breakingRecords(scores) == (0, 0)

    # Test case 5: Scores with only one element
    scores = [10]
    assert breakingRecords(scores) == (0, 0)

    print("All test cases pass")

if __name__ == '__main__':
    arr = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    length = len(arr)

    print(breakingRecords(arr))
    test_breakingRecords()