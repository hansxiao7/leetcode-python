import heapq


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        minHeap = []
        maxHeap = []
        result = []
        for i in range(k):
            pushVal(maxHeap, minHeap, nums[i])
        result.append(median(maxHeap, minHeap, k))

        for i in range(k, len(nums)):
            removeVal = nums[i - k]
            if not delete(maxHeap, -removeVal):
                delete(minHeap, removeVal)

            pushVal(maxHeap, minHeap, nums[i])

            result.append(median(maxHeap, minHeap, k))

        return result


def delete(heap, val):
    for i in range(len(heap)):
        if heap[i] == val:
            heap.remove(val)
            heapq.heapify(heap)
            return True
    return False


def pushVal(maxHeap, minHeap, val):
    if len(minHeap) == 0:
        heapq.heappush(minHeap, val)
    elif len(minHeap) > len(maxHeap):
        if val <= minHeap[0]:
            heapq.heappush(maxHeap, -val)
        else:
            heapq.heappush(minHeap, val)
            temp = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -temp)
    else:
        if val >= -maxHeap[0]:
            heapq.heappush(minHeap, val)
        else:
            heapq.heappush(maxHeap, -val)
            temp = heapq.heappop(maxHeap)
            heapq.heappush(minHeap, -temp)


def median(maxHeap, minHeap, k):
    if k % 2 == 0:
        return (-maxHeap[0] + minHeap[0]) / 2.0
    else:
        return minHeap[0]