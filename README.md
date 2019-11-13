Kindle scripts V:1.0.1

Hello,

The purpose of this set of scripts is to allow the installation of batches of apps to multiple ADB enabled devices at once.

Much of the contents will be hidden when you download it.  You should never need to see them to use the enclosed scripts.
Most of the hidden things are the parts of ADB that are needed to run it without installing ADB to your computer.
These scripts are written in Python.  As such, you will need python installed to run any of them.
The hidden folder labeled "support" is where the lists of devices are placed when the scripts are run.

-------BEFORE USE-------

make sure to install python 3, you can find the most up to date release of that here. https://www.python.org/downloads/

you will need to enable adb on your devices.  To do this, go to settings>Device Options and tap serial number 8 times to enable developer mode.
Once you do that a new settings option should appear called Developer Options.  You want to switch on the first setting under the Debugging heading called "enable ADB"

The maximum number of devices that you can work on at once varies from computer to computer but is generally about 8-10.  This is due to the way USB works and I will not be able to fix this.


-------TO USE-------

step 1: place all .apk files that you want installed in the apk folder.

step 2: place any mass data files in the appropriate folder within "appdata" this can get tricky, so the easiest thing to do is install the app on a single android device and see how it places its data.
The data is stored in the Android folder that shows up when you plug a device into your computer and open its storage.  Coincidentally, this is also the easiest way to get the supporting files if you are missing them.

step 3: run the correct Script.  descriptions of each are below.

-------SCRIPTS-------

kindle_installer
This script creates a list of attached devices that have ADB enabled and a separate list of all apps in the APK folder.  Once it has done this, it steps through each device running the "adb install" command
for each app that you have in the folder.  once this is done, it pushes the files placed in the appdata folder to their respective folder.

kindle_first_time
functions the same as kindle_installer with a few extra steps above just installing apps that get the devices ready for use with Gapps.

kindle_reboot_to_format
restarts the device to recovery mode to make it easy to reformat devices.