import json
import os

def consoleOutput(filename):
    out=filename.split("Input\\")

    os.system(os.getcwd()+"\\windows_binary.exe " + filename+" >> Output\\"+out[1])
    file1 = open(os.getcwd()+"\\Output\\"+out[1], "r")
    val=file1.read().replace("\"","'")
    val=val.split("},{")
    val[0]=val[0]+"}"
    val[0]=val[0].replace("[","")
    for lo in range(1,len(val)-1):
        val[lo]="{"+val[lo]+"}"
    val[len(val)-1]="{"+val[len(val)-1]
    val[len(val) - 1]=val[len(val)-1].replace("]","")
    val[len(val) - 1]=val[len(val)-1].strip()
    return (val)

def happy_scenario(filename):
    data = convertDict(filename)
    k = 0
    tasks = []
    empl = []
    for keys in data:
        empl.append(keys)
        if len(data[keys]) > k:
            k = len(data[keys])
            tasks = []
            for key in data[keys]:
                tasks.append(key)
    i = 0
    matx = []
    for keys in data:
        tas_mat = [0] * len(tasks)
        for task in tasks:
            try:
                tas_mat[tasks.index(task)] = data[keys][task]
            except KeyError:
                tas_mat[tasks.index(task)] = 0
        matx.append(tas_mat)
    res = []
    for loop in range(len(matx)):
        matx, high_no, i, j = max_and_matrix(matx)
        dict1 = {}
        dict1["Employee"] = empl[i]
        dict1["Task"] = tasks[j]
        dict1["Value"] = high_no
        op=str(dict1).replace(", ",",")
        op=op.replace(": ",":")
        res.append(op)
    return res

def validate(filename):
    try:
        data = convertDict(filename)
    except json.decoder.JSONDecodeError:
        print("Invalid JSON") # in case json is invalid
    else:
        print("Valid JSON file")
    for key in data:
        for keys in data[key]:
            try:
                assert isinstance(keys, str) and isinstance(data[key][keys], int)
            except AssertionError:
                if not isinstance(keys, str):
                    print(keys + " is not a string")
                elif not isinstance(data[key][keys], int):
                    print(data[key][keys] + " is not an integer")



def convertDict(filename):
    with open(filename) as file:
        data=json.load(file) # put JSON-data to a variable
        return data

def max_and_matrix(matx):
    higest_number = 0
    for i in range(len(matx)):
        for j in range(len(matx[i])):
            if (matx[i][j] > higest_number):
                higest_number = matx[i][j]
                rows=i
                col=j
    matx[rows][col] = 0
    for row in matx:
        row[col] = 0
    matx[rows] = [0] * len(matx[rows])
    return matx,higest_number,rows,col