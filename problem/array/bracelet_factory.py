
#1 no two adjacent beads
#2 no pattern of three should repeat
# ["R", "Y", "G", "B"]

def generateBeats(colors):
    size = len(colors)
    myBeats = []

    for ci in range(len(colors)):
        
