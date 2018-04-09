import re
import numpy as np

inpfile = ''


def repliceManning(gqName, inletNode, outletNode, Manning):
    global inpfile
    content = ''
    for line in inpfile.splitlines():
        newline = line
        if (line.find(gqName) >= 0 and line.find(inletNode) >= 0 and line.find(outletNode) > 0):
            str = line.split()
            newline = re.sub(str[4], Manning, newline)
        content = content + newline + '\n'
    inpfile = content


def repliceSubArea(tableName, nextTableName, areaName, index, value):
    global inpfile
    content = ''
    start, end = getTableByName(inpfile, tableName, nextTableName)
    current = 0
    for line in inpfile.splitlines():
        newline = line
        if (current > start and current < end):
            if (line.find(areaName) >= 0):
                str = line.split()
                newline = re.sub(str[index], value, newline)
        content = content + newline + '\n'
        current += 1
    inpfile = content


def readResult(filestr, tableName, nextTableName, nodeName, nodeType):
    start, end = getTableByName(filestr, tableName, nextTableName)
    current = 0
    for line in filestr.splitlines:
        if (current > start and current < end):
            if (line.find(nodeName) >= 0 and line.find(nodeType) >= 0):
                str = line.split()
                avg = str[2]
                max = str[3]
                return avg, max
        current += 1
    return 'no value', 'no value'


def getTableByName(filestr, tableName, nextTableName):
    start, end = 0, 0
    current = 0
    for line in filestr.splitlines():
        if (line.find(tableName) >= 0):
            start = current
        if (line.find(nextTableName) >= 0):
            end = current
        current += 1
    return start, end

def changeManning(value):
    repliceManning('gq1', 'j1', 'j2', value)

def changeNimperv(value):
    repliceSubArea('SUBAREAS', 'INFILTRATION', 'zmj1', 1, value)

def changeNperv(value):
    repliceSubArea('SUBAREAS', 'INFILTRATION', 'zmj1', 2, value)

def changeSimperv(value):
    repliceSubArea('SUBAREAS', 'INFILTRATION', 'zmj1', 3, value)

def changeSperv(value):
    repliceSubArea('SUBAREAS', 'INFILTRATION', 'zmj1', 4, value)

def changeCZero(value):
    repliceSubArea('SUBAREAS', 'INFILTRATION', 'zmj1', 5, value)


# 使用全局变量内部声明
def runInp():
    global inpfile
    inp = open('D:\SWMMH\Examples\\test.inp', 'r')
    for line in inp:
        inpfile += line

    #repliceManning('gq1', 'j1', 'j2', '0.03')
    #repliceSubArea('SUBAREAS', 'INFILTRATION', 'zmj1', 1, '0.04')
    changeCZero('23')
    newinp = open('D:\SWMMH\Examples\\test2.inp', 'w')
    newinp.write(inpfile)
    newinp.close()
    inp.close()
    print(inpfile)


def runRpt():
    rpt = open('D:\SWMMH\Examples\\test.rpt', 'r')
    avg, max = readResult(rpt, 'Node Depth Summary', 'Node Inflow Summary', 'pfk1', 'OUTFALL')
    rpt.close()
    print(avg, max)


# 0.011-0.024
# manningRange = np.linspace(0.011, 0.024, 10, True)
# print(manningRange)

# N-imperv 0.005-0.05
# N_impervRange=np.linspace(0.005,0.05, 10, True)
# print(N_impervRange)

if __name__ == "__main__":
    runInp()
    print(inpfile)

# runRpt()
