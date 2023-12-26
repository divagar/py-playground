def main():
    try:
        list = ["sleep", "code", "eat", "repeat"]
        listNoun = ["sleeping", "coding", "eating", "repeating"]

        #for
        print("-- for loop --")
        for el in list:
            print(el)

        #iter
        print("-- iter --")
        listIter = iter(list)
        print(next(listIter))
        print(next(listIter))
        print(next(listIter))
        print(next(listIter))
        with open("language/data.txt") as fp:
            for line in iter(fp.readline, ""):
                print(line)

        #range
        print("-- range --")
        for index in range(len(list)):
            print(index+1, list[index])

        #enumerate
        print("-- enumerate --")
        for index, el in enumerate(list, start=1):
            print(index, el)

        #zip
        print("-- zip --")
        for el in zip(list, listNoun):
            print(el)

        print("-- zip --")
        for el in zip(list, listNoun):
            print(el[0] + " noun is " + el[1])

        print("-- zip + enumerate--")
        for index, el in enumerate(zip(list, listNoun), start=1):
            print(index, el[0] + " noun is " + el[1])

    except Exception as e:
        print("Unknown error occurred ", e)
    finally:
        pass

if __name__ == "__main__":
    main()