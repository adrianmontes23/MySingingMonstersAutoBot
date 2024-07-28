@echo off
echo Launching MySingingMonsters on BlueStacks...
:: Change the path below to match your BlueStacks installation
start "" "C:\Program Files\BlueStacks_nxt\HD-Player.exe" --instance "Android11_24" --cmd launchApp --package "com.bigbluebubble.singingmonsters.full"
echo Launcher executed. If the game doesn't start, please check the paths and package name.
echo Waiting for BlueStacks to launch...
timeout /t 5 /nobreak > nul
echo Focusing on BlueStacks window...
cscript //nologo "%~f0?.wsf" //job:Focus
echo Launcher executed. BlueStacks window should now be in focus.
echo Changing directory to the bot location...
cd /d C:\Users\"YOURS"\Desktop\MySingingMonstersAutoBot-main
echo Starting the bot script...
py main.py
echo Bot script has finished executing.
pause
exit /b
<job id="Focus">
<script language="VBScript">
Set WshShell = CreateObject("WScript.Shell")
WshShell.AppActivate "BlueStacks App Player"
</script>
</job>