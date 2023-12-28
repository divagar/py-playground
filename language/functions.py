from datetime import datetime

def main():
    try:
    
        def getCurrentTimeHrs():
            return str(datetime.now().strftime('%H'))

        #function with documentation
        def greetings(name):
            """
            greetings function greets the user with custom msg based on current time

            parameter: 
            name - take a user name as input
            """
            msg = None
            hrs = int(getCurrentTimeHrs())
            if hrs >= 5 and hrs < 12:
                msg = "Good Morning"
            elif hrs >= 12 and hrs < 17:
                msg = "Good Afternoon"
            elif hrs >= 17 and hrs < 22:
                msg = "Good Evening"
            else:
                msg = "Good night"
            return (msg + " " + name)

        users = ["Tom", "Jerry"]
        print(greetings.__doc__)
        for user in users:
            print(greetings(user))

        #function with variable argument list
        def add(*args):
            total = 0
            for el in args:
                total += el
            return total
        
        addTotal = add(1, 2, 3, 4, 5)
        print(addTotal)

        #lambda function a.k.a anonymous function
        sumTotal = lambda x, y: x*y
        isEven = lambda x: x%2 == 0
        isOdd = not isEven
        print(sumTotal(5, 5))
        print(isEven(2), isEven(9))
        print(isEven(1), isEven(6))

        #function with keyword only argument
        def hello(name, custom_message=None):
            if custom_message != None:
                return custom_message +" " + name
            else:
                return "Hello " + name
        print(hello("Divagar Mohandass"))
        print(hello("Divagar Mohandass", custom_message="Howdy"))
    except Exception as e:
        print("Unknown error occurred ", e)
    finally:
        pass

if __name__ == "__main__":
    main()