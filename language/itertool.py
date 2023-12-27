import itertools

def main():
    try:
        nums = [10, 20, 30, 50, 60, 10, 30, 45, 67, 90]

        #count infinite iterator
        print("count infinite iterator")
        countIter = itertools.count(1000, 100)
        print(next(countIter))
        print(next(countIter))
        print(next(countIter))
        print(next(countIter))
        print(next(countIter))

        #cycle infinite iterator
        print("cycle infinite iterator")
        cycleIter = itertools.cycle(nums)
        print(next(cycleIter))
        print(next(cycleIter))
        print(next(cycleIter))
        print(next(cycleIter))
        print(next(cycleIter))

        #repeat infinite iterator
        print("repeat infinite iterator")
        repeatIter = itertools.repeat(1000, 5)
        print(next(repeatIter))
        print(next(repeatIter))
        print(next(repeatIter))
        print(next(repeatIter))
        print(next(repeatIter))

        #accumulate iterator
        print("accumulate iterator")
        accNums = list(itertools.accumulate(nums))
        print(nums)
        print(accNums)

        #chain iterator
        print("chain iterator")
        chain = list(itertools.chain("abc", "def"))
        print(chain)

        #drop while iterator
        print("drop while iterator")
        dropWhile = list(itertools.dropwhile(lambda x: x<50, nums))
        print(dropWhile)

        #take while iterator
        print("take while iterator")
        takeTill = list(itertools.takewhile(lambda x: x<50, nums))
        print(takeTill)

        #product iterator
        print("product iterator")
        product = list(itertools.product("ABCD", repeat=2))
        print(product)

        #permutations iterator
        print("permutations iterator")
        permutations = list(itertools.permutations("ABCD", 2))
        print(permutations)

        #combinations iterator
        print("combinations iterator")
        combinations = list(itertools.combinations("ABCD", 2))
        print(combinations)


    except Exception as e:
        print("unknown error occured ", e)
    finally:
        pass


main()
