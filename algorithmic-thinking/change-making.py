'''
Change making problem
    - find min number of coins from a set of denomination that add up to give a amount of money
    - ex: denomination are 1p, 2p, 5p, 10p, 20p, 50p and etc
    - ex: 24p -> 20p + 2p + 2p
    - ex: 1.63p -> 1rp + 50p + 10p + 2p + 1p
'''

def makeChange1(target):
    deno = [200, 100, 50, 20, 10, 5, 2, 1]
    out = []

    while target != 0:
        for d in deno:
            num = target % d
            if(num == target):
                continue
            else:
                for x in range((target // d)):
                    out.append(d)
                target = num
    print(out)
    return out

def makeChange2(target):
    deno = [200, 100, 50, 20, 10, 5, 2, 1]
    out = []

    for d in deno:
        if target >= d:
            target -= d
            out.append(d)
    print(out)
    return out

def main():
    try:
        print("First solution")
        makeChange1(224)

        print("Second solution")
        makeChange2(224)

    except Exception as e:
        print("Unknown error occurred. ", e)
    finally:
        print("Done")

if __name__ == "__main__":
    main()