'''
Linear Search
'''
def linearSearch(data, searchFor):
    for i, item in enumerate(data):
        if item == searchFor:
            return i
    return -1

def main():
    try:
        data = [35, 63, 62, 2, 6, 14, 67, 86]
        searchFor = 0
        ret = linearSearch(data, searchFor)
        if(ret != -1):
            print(f"Item {searchFor} found at the index {ret}")
        else:
            print(f"Oops, not able to find the element {searchFor} in the list")
    except Exception as e:
        print("Unknown error occurred. ", e)
    finally:
        print("Done")

if __name__ == "__main__":
    main()