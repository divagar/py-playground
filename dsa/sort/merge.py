
def mergeSort(data):
    if(len(data) > 1):
        size = len(data)//2
        first = data[:size]
        second = data[size:]
        mergeSort(first)
        mergeSort(second)

        i = j = k = 0
        while i < len(first) and j < len(second):
            if(first[i] < second[j]):
                data[k] = first[i]
                i += 1
            else:
                data[k] = second[j]
                j += 1
            k += 1

        while i < len(first):
            data[k] = first[i]
            i += 1
            k += 1
        while j < len(second):
            data[k] = second[j]
            j += 1
            k += 1


data = [24, 35, 64, 11, 6, 1, 26, 2, 0]
print(data)
print("Merge Sort")
mergeSort(data)
print(data)
