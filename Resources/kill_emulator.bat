REM Uninstall Saral.apk from active AVD
adb uninstall com.saral.application
REM Kill the currently running AVD
adb -s emulator-5554 emu kill