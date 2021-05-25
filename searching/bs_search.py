# Binary Search - recursive and iterative algorithm


def bs_search_rec(arr, left, right, value):

	if right > left:
		mid = left + (right - 1) // 2

		if arr[mid] == value:
			return mid
		elif arr[mid] > value:
			return bs_search_rec(arr, left, mid - 1, value)
		else:
			return bs_search_rec(arr, mid + 1, right, value)
	else:
		return -1


def bs_search_iter(arr, left, right, value):

	while left <= right:
		mid = left + (right - 1) // 2

		if arr[mid] == value:
			return mid
		elif arr[mid] < value:
			left = mid + 1
		else:
			right = mid - 1

	return -1
