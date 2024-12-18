def mySqrt(x: int) -> int:
    left, right = 0, x
    while left <= right:
        middle = (right - left) // 2 + left
        if middle**2 > x:
            right = middle - 1
        elif middle**2 < x:
            left = middle + 1
        else:
            return middle
    return right
