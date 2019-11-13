


import os
import time
import subprocess

assert (os.path.isdir('apk')), "you must have a folder containing your apps named \"apk\" in the same directory as this script"
#creates a list of apps to install

print("Starting ADB")
#starts adb
os.system('adb kill-server')
os.system('adb start-server')
time.sleep(5)
print('you should have a prompt on all your devices that asks that you allow a device access to developer settings\nplease ensure that you have pressed \"ok\" or \"allow\" on all devices\n\n')
input('once you have pressed ok on all devices, press ENTER to continue\n\n')

#this is an effing mess, but it works to get the device IDs
fileName = ('support/' + str(time.time()) + '.txt')
#creates a file named with today's date and time for storing device ID strings and writes the STDOUT from 'adb devices' to it.
os.system('adb devices > ' + fileName)
devListUnfiltered=[""]
#creates an array where each entry is a line of the file we created from STDOUT
devListUnfiltered = open(fileName,'r',encoding='utf8').readlines()
del devListUnfiltered[0]
devList=[""]
tick=0
#print(str(len(devListUnfiltered)) + " lines")                #debug lines, left for later
#print(devListUnfiltered)
#creates a second array each with the 'filtered' device ID strings that we are going to use to install apps
while tick < (len(devListUnfiltered)-1):
    devList.append(devListUnfiltered[tick][0:16])
    #print(str(tick) + "tick")
    tick+=1
    #print(devList[tick])

#deletes the first object in the array as it is always a junk string
del devList[0]
#print(devList)

doneCount=0
    
devNum=0
while devNum < len(devList):
        
    os.system('adb ' + devList[devNum] + 'reboot recovery')
    devNum+=1
doneCount=doneCount+1
   # print("Apps installed " + str(doneCount))
print("once the devices have rebooted, use the volume rocker to select \n\"wipe data\\factory reset\" and then select yes from the list that pops up.")


time.sleep(5000)



##############################################################################################################
