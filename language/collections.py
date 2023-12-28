import collections

def main():
    try:
        #list
        print("List collection")
        nums = [10, 20, 30, 40, 50]
        print(nums)

        #tuple
        print("Tuple collection")
        nums = (10, 20, 30, 40, 50)
        print(nums)

        #set
        print("Set collection")
        nums = set([10, 20, 30, 40, 50, 50])
        print(nums)

        #dict
        print("Dict collection")
        nums = {1: "one", 2: "two", 3: "three", 4:  "four", 5: "five"}
        print(nums)
        for key in nums:
            print("key:", key, "val:",nums[key])

        #named tuple
        print("Named tuple collection")
        User = collections.namedtuple("User", "firstname lastname age")
        myUser = User("Divagar", "Mohandass", 37)
        print(myUser)
        print(myUser.firstname, myUser.lastname, myUser.age)

        #default dict
        print("Defact dict collection")
        user = collections.defaultdict(str)
        user['firstName'] = "Divagar"
        user['lastName'] = "Mohandass"
        user['age'] = 37
        print(user['hello']) # this access can produce exception using normal dict, but here it is init to empty str
        
    except Exception as e:
        print("Unknown error occurred ", e)
    finally:
        pass

if __name__ == "__main__":
    main()