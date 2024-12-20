def isPowerOfTwo(n: int) -> bool:
    start, end = 0, 32
    while start <= end:
        mid = (end - start) // 2 + start
        if n > 2**mid:
            start = mid + 1
        elif n < 2**mid:
            end = mid - 1
        else:
            return True
    return False
