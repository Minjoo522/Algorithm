import sys

input = sys.stdin.readline

N = int(input())
heap = [0]


def heap_push(item):
    heap.append(item)

    child = len(heap) - 1
    parent = child // 2

    while parent > 0 and heap[parent] < heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2


def heap_pop():
    if len(heap) == 1:
        print(0)
        return

    result = heap[1]  # 루트 저장
    heap[1] = heap[-1]  # 제일 마지막 값 루트에 저장
    heap.pop()

    parent = 1
    child = parent * 2  # 인덱스 0부터 시작하므로 +1, 우선 좌측을 기준

    while child < len(heap):
        if child + 1 < len(heap) and heap[child] < heap[child + 1]:
            child += 1  # 기준 우측으로 변경

        if child >= len(heap) or heap[parent] >= heap[child]:
            break

        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2

    print(result)


for _ in range(N):
    command = int(input())
    if command == 0:
        heap_pop()
    else:
        heap_push(command)
