from datetime import datetime
def markAttendance():
    name= 'Aman'
    with open('attendance.csv','r+') as f:
        myDataList = f.readlines()
        #print(myDataList)
        #nameList = []
        uniqueNameDate= []
        for entry in myDataList:
            entry1=entry.split(',')
            if len(entry1)>1:
                uniqueNameDate.append((entry1[0],entry1[1]))
                #newlist is list of tuple containing name and date
        #for line in myDataList:
        #    entry= line.split(',')
        #    nameList.append(entry[0])

        currentEntry=(name,'2021-02-20')
        #currentEntry is a tuple of name and current date
        #for item in newlist:
        #    print(item[1])
        if currentEntry not in uniqueNameDate:
            print("add")
            now = datetime.now()
            date_string = currentEntry[1]
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{date_string},{dtString}')
        #if name not in nameList:
        #    now = datetime.now()
        #    date_string= now.date()
        #    dtString= now.strftime('%H:%M:%S')
        #    f.writelines(f'\n{name},{date_string},{dtString}')
        print("mynewlist")
        print(uniqueNameDate)
markAttendance()