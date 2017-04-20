dbFile = open("db.txt",)
file = open("index.html","w")

dbFileRead = dbFile.read()

def readFile():
    for line in dbFileRead:
        line = line.rstrip('\n')
        key, value = line.split(':')
        if ':' in line:
            if key == "studentName":
                studentName = value

            elif key == "studentNum":
                studentNum = value

            elif key == "studentEmp":
                studentEmp = value

            elif key == "studentPhone":
                studentPhone = value

            elif key == "studentEmail":
                studentEmail = value

            elif key == "studentResume":
                studentResume = value

            elif key == "studentWeb":
                studentWeb = value

            elif key == "studentAddress":
                studentAddress = value

