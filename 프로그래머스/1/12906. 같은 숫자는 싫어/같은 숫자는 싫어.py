def solution(arr):
    answer = []
    prev = -1
    for i in range(len(arr)):
        if prev != arr[i]:
            answer.append(arr[i])
            prev = arr[i]
    return answer