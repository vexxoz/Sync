import shutil #copy commands
import os #filepath commands
import time # sleep command

fromDir = "C:/wamp64/www/SalonMaison" # from directory
toDir = "C:/Users/blake/Documents/GitHub/Database" # directory copy of fromDir
ingnoreFilePath = fromDir + "/ignore.txt"

#how often to sync in seconds
seconds = 90

#intialize count
count = 0

#open ignore list file
ingnoreFile = open(ingnoreFilePath, "r")

#inf loop to keep syncing files
while True:
    #for each file in the from directory
    for filename in os.listdir(fromDir):
        #check if file is ignored
        if filename not in ingnoreFile.read():
            #print the filename
            shutil.copyfile((fromDir + "/" + str(filename)), (toDir + "/" + str(filename)))
            count += 1

    print("Synced " + str(count) + " files!")

    #reset the count
    count = 0

    #sync every time seconds
    time.sleep(seconds)
