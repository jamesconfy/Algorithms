class BinarySearch(object):
    def __init__(self, arr) -> None:
        self.arr = arr
        self.arr.sort()

    def binarySearch(self, target=0):
        start = 0
        end = len(self.arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if self.arr[mid] == target:
                return mid + 1
            elif self.arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def binSearch(self, target):
        start = 0
        end = len(self.arr) - 1
        while (end - start) > 1:
            mid = start + (end - start) // 2
            if self.arr[mid] <= target:
                start = mid
            else:
                end = mid

        if self.arr[start] == target:
            return start + 1
        if self.arr[end] == target:
            return end - 1
        return -1

    def __floor(self, target):
        start = 0
        end = len(self.arr)
        while (end-start>1):
            mid = start+(end-start)//2
            if self.arr[mid] <= target:
                start = mid
            else:
                end = mid
        return self.arr[start]

    def floor(self, target):
        if target < self.arr[0]:
            return -1
        # Observe boundaries
        return self.__floor(target)

    def getRightPosition(self, start, end, target):
        while end - start > 1:
            mid = start + (end - start) // 2
            if self.arr[mid] <= target:
                start = mid
            else:
                end = mid

        return start

    def getLeftPosition(self, start, end, target):
        while end - start > 1:
            mid = start + (end - start) // 2
            if self.arr[mid] >= target:
                end = mid
            else:
                start = mid

        return end

    def countDuplicate(self, target):
        left = self.getLeftPosition(-1, len(self.arr) - 1, target)
        right = self.getRightPosition(0, len(self.arr), target)

        print(left, right)
        if self.arr[left] == target and target == self.arr[right]:
            return right - left + 1
        return 0

if __name__ == "__main__":
    a = [1, 3, 4, 5, 6, 7, 7, 7, 7, 7, 11, 12, 23, 34, 51, 53, 55, 61, 70, 72]
    val = 8
    binary1 = BinarySearch(a)
    print(binary1.binarySearch(val))
    print(binary1.binSearch(val))
    print(binary1.floor(val))
    print(binary1.countDuplicate(1))
