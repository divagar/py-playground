

numOfCourse = 5
req = [[0,1], [0,2], [1,3], [1,4], [3,4]]

numOfCourse = 2
req = [[0,1], [1,0]]

preMap = {i:[] for i in range(numOfCourse)}
for i, j in req:
    preMap[i].append(j)


