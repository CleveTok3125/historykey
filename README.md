
## Description
The application automatically get the wish history link used for paimon.moe on Windows
## Use
[Download](https://github.com/CleveTok3125/historykey/releases) and run `historykey.exe`
#### To run every time the computer starts
**Windows + R** to open Run
```shell:startup```
Paste the shortcut into the startup folder
## Guide
1. [Set up environment](#Set-up-environment)
2. [Create executable file](#Create-executable-file)
3. [About historykey.ps1](#about-historykey.ps1)
4. [Run](#run)
5. [Close the application manually](#Close-the-application-manually)
### Set up environment <a name="Set-up-environment"></a>
```
$ python -m venv historykey
$ ".\historykey\Scripts\activate.bat"
$ (historykey) pip install -r requirements.txt
$ (historykey) ".\historykey\Scripts\activate.bat"
```
### Create executable file <a name="Create-executable-file"></a>
```
$ pip install pyinstaller
$ pyinstaller --onefile --noconsole --clean --paths ".\historykey\Lib\site-packages" historykey.py
$ move ".\dist\historykey.exe" ".\"
$ del historykey.spec
$ rmdir /q dist
$ rmdir /s /q build
$ rmdir /s /q historykey
```
### About historykey.ps1 <a name="about-historykey.ps1"></a>
- A third party powershell script from [MadeBaruna](https://gist.github.com/MadeBaruna/)
- Read the `README.md` in [MadeBaruna](https://gist.github.com/MadeBaruna/) and find the code named `getlink.ps1` . Download or copy and save using the name `historykey.ps1` and place it in the folder containing `historykey.exe`
- By default `historykey.exe` always uses `historykey.ps1`
### Run <a name="run"></a>
Supposed to run in historykey folder
```
$ cd historykey
$ python historykey.py
```
or
```
$ cd historykey
$ historykey.exe
```
*Note: the application will run in the background without any notification. To find out, look in the process manager. The application will stop when the wish history is obtained.*
### Close the application manually<a name="Close-the-application-manually"></a>
```$ taskkill /F /FI "Imagename eq historykey.exe" /T```