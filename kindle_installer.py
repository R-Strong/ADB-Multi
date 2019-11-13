import os
import time
import subprocess


assert (os.path.isdir('apk')), "you must have a folder containing your apps named \"apk\" in the same directory as this script"
#creates a list of apps to install

apkList = os.listdir('apk')



print("app list created, apps to be installed are\n")
print(apkList)

#creates a variable that is the number of apps to be installed
appCount=len(apkList)

print("total app count is - "+str(appCount))


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
#print(devListUnfiltered[0])
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
    
print("you have " + str(len(devList)) + " devices ready for apps, installing apps now\n\n")


doneCount=0
#this actually installs apps.
while doneCount<appCount:
    
    devNum=0
    while devNum < len(devList):
        print('installing app ' + apkList[doneCount] + ' on device ' + devList[devNum])
        os.system('adb -s ' + devList[devNum] + ' install apk/' + apkList[doneCount])
        devNum+=1
    doneCount=doneCount+1
    print("Apps installed " + str(doneCount))
print("completed, " + str(appCount) + " apps installed on your devices")
print("pushing additional files now.")
devNum=0

#this pushes the extra files to where they belong on the devices.  This is not usually necessary and will just copy nothing if it is not needed.
while devNum < len(devList):
    print("pushing files to device " + devList[devNum])
    #os.system('adb -s ' +devList[devNum] + ' shell mkdir /storage/emulated/0/Android/obb')
    os.system('adb -s ' + devList[devNum] + ' push appdata/obb /storage/emulated/0/Android/')
    print('pushed obbs')
    #os.system('adb -s ' +devList[devNum] + ' shell mkdir /storage/emulated/0/Android/data')
    os.system('adb -s ' + devList[devNum] + ' push appdata/data /storage/emulated/0/Android/')
    print('pushed data')
    #os.system('adb -s ' +devList[devNum] + ' shell mkdir /storage/emulated/0/Android/media')
    os.system('adb -s ' + devList[devNum] + ' push appdata/media /storage/emulated/0/Android/')
    print('pushed media')
    print("files pushed to device " + devList[devNum])
    devNum+=1
print("please review the installation process to ensure that there were no failures.")


time.sleep(5000)



##############################################################################################################
