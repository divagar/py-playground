def main():
    try:
        list = [0, 1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
        #'any' built-in function
        print(any(list))

        #'all' built-in function
        print(all(list))

        #'min' built-in function
        print(min(list))

        #'max' built-in function
        print(max(list))

        #'sum' built-in function
        print(sum(list))

        #'any' - user defined function
        ret = False
        for el in list:
            if el:
                ret = True
                break
        print(ret)

        #'all' - user defined function
        ret = True
        for el in list:
            if not el:
                ret = False
                break
        print(ret)

        #'min' - user defined function
        ret = list[0]
        for i in range(len(list)-1):
            if ret > list[i+1]:
                ret = list[i+1]
        print(ret)

        #'max' - user defined function
        ret = list[0]
        for i in range(len(list)-1):
            if ret < list[i+1]:
                ret = list[i+1]
        print(ret)

        #'sum' - user defined function
        ret = 0
        for ele in list:
            ret += ele
        print(ret)

    except Exception as e:
        print("Unknown error occurred ", e)
    finally:
        pass

if __name__ == "__main__":
    main()