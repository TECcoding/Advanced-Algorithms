# type: ignore

from heapq import heappush, heappop


# Complexity: O(N log N)
def heap_sort(data):

    # Create the heap
    heap = []
    for elem in data:
        heappush(heap, elem)

    # Remove one element at a time from heap
    result = []
    while heap:
        result.append(heappop(heap))

    return result


if __name__ == "__main__":
    # heap = []
    # heappush(heap, 7)
    # print(heap)
    # heappush(heap, 3)
    # print(heap)
    # heappush(heap, 6)
    # print(heap)
    # heappush(heap, 2)
    # print(heap)
    # print(heappop(heap))
    # print(heap)
    # print(heappop(heap))
    # print(heap)
    # print(heappop(heap))
    # print(heap)
    # print(heappop(heap))
    # print(heap)
    print(heap_sort([7, 5, 8, 6, 10, 2, 4, 1]))

    