'''
100 doors problem
    - 100 doors in a row
    - all doors are initially closed
    - you make 100 passes by the doors
    - on the 1st pass, visit every door and toogle the door state
    - on the 2nd pass, visit every 2nd door (door #2,4,6) and toogle the door state
    - on the 3rd pass, visti every 3rd door (door #3,6,9) and toogle the door state
    - continue this pattern until you visit the 100th door
    - Which door is open/closed at the end of the last pass
'''
def main():
    doors = {k: 0 for k in range(0, 100)}
    print("Initial doors state ", doors)
    try:
        for i in range(0, 100):
            #print("\n\nPass #", i)
            for j in range(0, 100, i+1):
                #skip door#0 for rest of the pass
                if(i != 0 and j == 0):
                    pass
                else:
                    doors[j] = not doors[j]
                    #print("Door#",j, " State#", doors[j], end=" | ")
    except Exception as e:
        print("Unknown error occurred. ", e)
    finally:
        #print open/close door
        print("\n\nList of open door")
        print([key for key in doors if doors[key] == True])

        print("\n\nList of closed door")
        print([key for key in doors if doors[key] == False])
        print("Done")

if __name__ == "__main__":
    main()