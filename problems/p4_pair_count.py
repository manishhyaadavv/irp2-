def count_pairs(arr, k):
    count = 0
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == k:
                count += 1

    return count


n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(count_pairs(arr, k))