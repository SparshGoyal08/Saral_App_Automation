<p align="center">
  <img src="./Resources/logo.png" alt="Image Description">
</p>

# Saral App Automation Project (Android)
![Saral](./Resources/SaralLogo.png)
## Dependencies
1. Python [v3.x] (preferably 3.11)
2. PyCharm (Use community edition)
3. Node.js (to support Appium server and install drivers)
4. Appium [2.x] (Use the latest version)
5. Appium desktop GUI ***(Deprecated)***
6. Appium Inspector (any version compatible, check release notes)
7. Android Studio (IDE may not be necessary, but couldn’t find just the emulator)
8. UIAutomator2 (For android, library can be installed)
9. Java 17 ***(Deprecated)***

## Installation Process(es)
1. Python [v3.x]
   * Go to Python.org 
   * Look for v3.11 release 
   * Download the .exe file for windows (x86 or x64)
   * Install the .exe file, follow the instructions on screen
   **(make sure to check .py extension and “Add path to environment variables” checkboxes)**
   * Check if the language is added to the environment variable:
     * Open cmd as administrator 
     * Type in python –version

2. PyCharm 
   * Google, download PyCharm 
   * Open official link from JetBrains
   * Download the community edition 
   * Install by following the instructions on screen

3. Node.js 
   * Google, download node.js 
   * Click the first link and download the .exe file for windows 
   * Install the .exe file and follow the instructions on screen 
   * Check if the language is added to the environment variable:
     * Open cmd as administrator 
     * Type in
     >npm –version 
4. Appium [v2.x]
   * Google, download Appium 
   * Follow the instructions, on official Appium documentation link Here 
   * Check if Appium is installed successfully or not
     * Open cmd as administrator
     * Type in
     > appium –version 
5. Appium Desktop GUI
***(Deprecated)***

6. Appium Inspector 
   * Google, Appium Inspector 
   * Follow the official GitHub repo link [Here](https://github.com/appium/appium-inspector.git) 
   * Scroll down and click on [Releases](https://github.com/appium/appium-inspector/releases) 
   * Download the latest release for windows

7. Android Studio 
   * Google, download android studio 
   * Click the official ink by Android Developers Community [Here](https://developer.android.com/) 
   * Scroll down and download the latest release for windows
      **(Check windows specifications for 11x86, 11x64, 10x86 or 10x64)**
   * Create ANDROID_HOME variable under System Variables and add the following path 
   C:\Users\DELL\AppData\Local\Android\Sdk\
   **(Change according to your device)**
   * Now, add the Android Studio paths of following folders to environment “Paths” variable under System Variables
   C:\Users\DELL\AppData\Local\Android\Sdk\
   C:\Users\DELL\AppData\Local\Android\Sdk\platform-tools\
   **(Change according to your device)**
   * Now, check if the android studio is added to the global environment or not 
     * Open cmd as administrator 
     * Type in
     >adb –version
   
     
8. UIAutomator2 and XCUItest 
   * Go to C:\Users\DELL\.appium\node_modules and check if following files are present or not

9. Java 17
***(Deprecated)***

## Run your first test case
1. Make sure all the dependencies are downloaded and all the in libraries are installed properly
2. Go to Resources and changes the path of .bat files to support your system
3. Make sure to change the name of the device to the name you have chosen for your AVD
4. Now go to App/AndroidEmulator.py and change the path of .bat files to the one supported in your system
5. Repeat [4] for App/AppiumServe.py as well
6. Now, go to settings and make sure pytest plugin is installed for PyCharm IDE
7. Now, go to configurations and create a new configuration.
![ScreenShot](.\Resources\Screenshot 2023-08-17 154347.png)
8. Click Add a new Configuration, select script and then select the path to your test case
![ScreenShot](.\Resources\Screenshot 2023-08-17 154833.png)
9. Click OK and start the test case.