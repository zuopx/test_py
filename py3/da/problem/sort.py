def mergesort(arr: list):

    def _merge(arr: list, head1: int, tail1: int, head2: int, tail2: int):
        tmp = []
        i, j = head1, head2
        while i < tail1 and j < tail2:
            if arr[i] > arr[j]:
                tmp.append(arr[j])
                j += 1
            else:
                tmp.append(arr[i])
                i += 1
        if i >= tail1:
            while j < tail2:
                tmp.append(arr[j])
                j += 1
        elif j >= tail2:
            while i < tail1:
                tmp.append(arr[i])
                i += 1

        i = 0
        for j in range(head1, tail1):
            arr[j] = tmp[i]
            i += 1
        for j in range(head2, tail2):
            arr[j] = tmp[i]
            i += 1

    def _mergesort(arr: list, head: int, tail: int):
        if tail - head > 1:
            median = (head + tail) // 2
            _mergesort(arr, head, median)
            _mergesort(arr, median, tail)
            _merge(arr, head, median, median, tail)

    _mergesort(arr, 0, len(arr))


def quicksort(arr: list):

    def _quicksort(arr: list, head: int, tail: int):
        if tail - head > 1:
            p = _get_pivot(arr, head, tail)
            m = _partition(arr, head, tail, p)
            _quicksort(arr, head, m)
            _quicksort(arr, m + 1, tail)

    def _partition(arr: list, head: int, tail: int, p: int):
        _swap(arr, tail - 1, p)
        m = head
        for i in range(head, tail):
            if arr[i] < arr[tail - 1]:
                _swap(arr, m, i)
                m += 1
        _swap(arr, m, tail - 1)
        return m

    def _get_pivot(arr: list, head: int, tail: int):
        return tail - 1

    def _swap(arr: list, i: int, j: int):
        if i != j:
            arr[i], arr[j] = arr[j], arr[i]

    _quicksort(arr, 0, len(arr))
