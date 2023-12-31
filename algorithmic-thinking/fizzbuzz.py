'''
Fizz Buzz problem
    - count 1 to 100
    - replace multiples of 3 by 'fizz'
    - replace multiples of 5 by 'buzz'
    - replace multiples of 3 and 5 by 'fizzbuzz'
'''
def main():
    game = {k:None for k in range(1, 101)}
    try:
        for i in range(1, 101):
            if(i%3 == 0 and i%5 == 0):
                game[i] = "fizzbuzz"
            elif(i%3 == 0):
                game[i] = "fizz"
            elif(i%5 == 0):
                game[i] = "buzz"
    except Exception as e:
        print("Unknown error occurred. ", e)
    finally:
        print("\nFinal game state")
        print("\nFizz index", [k for k in game if game[k] == "fizz"])
        print("\nBuzz index", [k for k in game if game[k] == "buzz"])
        print("\nFizzbuzz index", [k for k in game if game[k] == "fizzbuzz"])
        print("Done")

if __name__ == "__main__":
    main()