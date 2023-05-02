def reverseList(head: []) -> list:
    if len(head) == 0:
        return []

    answer = []
    times = len(head)

    for i in range(times):
        current_max = head[0]

        for j in range(1, len(head)):
            if current_max < head[j]:
                current_max = head[j]

        answer.append(current_max)
        head.remove(current_max)

    return answer


head = [int(i) for i in input().split()]
print(reverseList(head))


