import subprocess
import sys
import os
import shutil

# psPath = 'C:\Windows\system32\WindowsPowerShell\\v1.0\powershell.exe'

fileNameList = os.listdir('ill-typed')

ghcPath = 'C:\ghc\\ghc-'
ghcExe = '\\bin\ghc.exe'

a = sys.argv[1]
b = sys.argv[2]

aLog = ' *> aLog.txt'
bLog = ' *> bLog.txt'

commandBuildA = ghcPath + a + ghcExe + ' 1.hs' + aLog
commandBuildB = ghcPath + b + ghcExe + ' 1.hs' + bLog

def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

def buildA(fileName):
    return ghcPath + a + ghcExe + ' ill-typed\\' + fileName + aLog

def buildB(fileName):
    return ghcPath + b + ghcExe + ' ill-typed\\' + fileName + bLog


def logcreator(fileName):
    name = fileName.replace('.hs', '.txt')
    log = open('txt-output\\' + name, 'w')
    log.write('RAW FILE BEING COMPILED: \n---------------------------------------\n\n')
    hs = open('ill-typed\\' + fileName, 'r')
    hsLines = hs.readlines()
    log.writelines(hsLines)
    hs.close()
    log.write('\n\nOUTPUT FROM GHC v ' + a + ': \n---------------------------------------\n\n')
    aLogFile = open('aLog-utf8.txt', 'r')
    aLines = aLogFile.readlines()
    log.writelines(aLines)
    aLogFile.close()
    log.write('\n\nOUTPUT FROM GHC v ' + b + ': \n---------------------------------------\n\n')
    bLogFile = open('bLog-utf8.txt', 'r')
    bLines = bLogFile.readlines()
    log.writelines(bLines)
    bLogFile.close()

for fileName in fileNameList:
    if '.hs' in fileName:
        run(buildA(fileName))
        run('Get-Content .\\aLog.txt | Set-Content -Encoding utf8 aLog-utf8.txt')
        run(buildB(fileName))
        run('Get-Content .\\bLog.txt | Set-Content -Encoding utf8 bLog-utf8.txt')
        logcreator(fileName)

fileNameList = os.listdir('ill-typed')

for fileName in fileNameList:
    if not '.hs' in fileName:
        os.remove("ill-typed\\" + fileName)