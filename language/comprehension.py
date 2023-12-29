import collections

def main():
    try:
        nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 11, 22, 33, 44, 55, 66, 77, 88, 99]
        print("w/o List comprehension")
        isEven = lambda x: x%2 == 0
        isOdd = lambda x: not isEven(x)
        print(list(filter(isEven, nums)))
        print(list(filter(isOdd, nums)))
        print("w/ List comprehension")
        print([num for num in nums if num%2 == 0])
        print([num for num in nums if num%2 != 0])

        print("w/o Dict comprehension")
        evenOdd = collections.defaultdict(int)
        for num in nums:
            if(isEven(num)):
                evenOdd["even"] += 1
            if(isOdd(num)):
                evenOdd["odd"] += 1
        print(evenOdd)
        print("w/ Dict comprehension")
        #evenOdd = {"even": evenOdd["even"] +1 for num in nums if num%2 == 0}
        evenOdd = {"odd": evenOdd["odd"] +1 for num in nums if num%2 != 0}
        print(evenOdd)


    except Exception as e:
        print("unknown error occured ", e)
    finally:
        pass


main()
