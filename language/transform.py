def main():
    try:
        nums = [35, 78, 23, 21, 7, 0, 14, 83, 98, 60]

        #Reverse sorting
        print("Sorting reverse")
        nums = sorted(nums, reverse=True)
        print(nums)

        #sorting
        print("Sorting")
        nums = sorted(nums)
        print(nums)

        #filter
        def isEven(x):
            if x % 2 == 0:
                return True
            return False
        
        def isOdd(x):
            return not isEven(x)
        
        print("Even num filter")
        evenList = list(filter(isEven, nums))
        print(evenList)

        print("Odd num filter")
        oddList = list(filter(isOdd, nums))
        print(oddList)

        #map
        def giveGrade(x):
            if x >= 90:
                return "A"
            elif x < 90 and x >= 70:
                return "B"
            elif x < 70 and x >= 50:
                return "C"
            else:
                return "D"
        
        print("Grade mapping")
        gradeMap = list(map(giveGrade, nums))
        print(gradeMap)
    except Exception as e:
        print("unknown error occured ", e)
    finally:
        pass


main()
