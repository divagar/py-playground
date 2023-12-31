'''
Selection Sort
    - Find the min val in the list and replace with first element in the list
    - Find the second min val in the list and replace with second element in the list
    - Repeat the same pattern
'''
def selectionSort(data):
    for i in range(len(data)-1):
        minIndex = i
        for j in range(i+1, len(data)):
            if(data[minIndex] > data[j]):
                minIndex = j
   
        data[i], data[minIndex] = data[minIndex], data[i]
    return data

def main():
    ret = []
    try:               
        data = [35, 63, 62, 2, 6, 14, 67, 86]
        print("\n Input ", data)
        ret = selectionSort(data)
    except Exception as e:
        print("Unknown error occurred. ", e)
    finally:
        print("\n Final response ", ret)
        print("Done")

if __name__ == "__main__":
    main()