'''
Merge sort algo - Divide and conquer strategy
- mergeSort(data, l, r)
    if l > r
        return
    m = (l+r)/2
    mergeSort(data, l , m)
    mergeSort(data, m+1, r)
    merge(data, l, m, r)
'''

def mergeSort(data):
    dataLen = len(data)
    if dataLen > 1:
        # find the mid index of data list and build left/right data list
        midIndex = int(dataLen/2)    
        LData = data[:midIndex]
        RData = data[midIndex:]
        
        # sort the left/right data list
        mergeSort(LData)
        mergeSort(RData)
        
        # merge the left/right data list
        LDataIndex = 0
        RDataIndex = 0
        dataIndex = 0
        
        # loop over both left/right, compare and insert to data list
        while (LDataIndex < len(LData) and RDataIndex < len(RData)):
            if (LData[LDataIndex] < RData[RDataIndex]):
                data[dataIndex] = LData[LDataIndex]
                dataIndex += 1
                LDataIndex += 1
            else:
                data[dataIndex] = RData[RDataIndex]
                dataIndex += 1
                RDataIndex += 1
        
        #copy the rest of the left data to data list
        while LDataIndex < len(LData):
            data[dataIndex] = LData[LDataIndex]
            dataIndex += 1
            LDataIndex += 1
        
        #copy the rest of the right data to data list
        while RDataIndex < len(RData):
            data[dataIndex] = RData[RDataIndex]
            dataIndex += 1
            RDataIndex += 1 
        
    return data

items = [529, 25, -19, 42, -59, 2, 99, 1]
print("Input list : ", items)
items = mergeSort(items)
print("Sorted list : ", items)
