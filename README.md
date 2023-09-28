## Description
The script file automatically get the wish history link used for paimon.moe on Windows
## Guide
1. [Install dependencies](#install-dependencies)
2. [Set up configuration](#set-up-configuration)
3. [About historykey.ps1](#about-historykey.ps1)
4. [Run](#run)
### Install dependencies <a name="install-dependencies"></a>
`pip install -r requirements.txt`

*Note: [historykey.exe](https://github.com/CleveTok3125/historykey/releases/) - executable version of `historykey.py` that can be run without installing dependencies.*
### Set up configuration <a name="set-up-configuration"></a>
Open historykey.ini with notepad or similar to configure
### About historykey.ps1 <a name="about-historykey.ps1"></a>
- A third party powershell script from [MadeBaruna](https://gist.github.com/MadeBaruna/)
- Read the `README.md` in [MadeBaruna](https://gist.github.com/MadeBaruna/) and find the code named `getlink.ps1` . Download or copy and save using the name `historykey.ps1` and place it in the folder containing `historykey.py`
- By default `historykey.py` always uses `historykey.ps1`
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