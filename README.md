## Description
The script file automatically get the wish history link used for paimon.moe on Windows
## Guide
1. [Install dependencies](#Install-dependencies)
2. [Set up configuration](Set-up-configuration)
3. [About historykey.ps1](#About-historykey.ps1)
4. [Run](#Run)
### Install dependencies
`pip install -r requirements.txt`

*Note: `historykey.exe` - executable version of `historykey.py` that can be run without installing dependencies.*
### Set up configuration
Open historykey.ini with notepad or similar to configure
### About historykey.ps1
- A third party powershell script from [MadeBaruna](https://gist.github.com/MadeBaruna/)
- Read the `README.md` in [MadeBaruna](https://gist.github.com/MadeBaruna/) and find the code named `getlink.ps1` . Download or copy and save using the name `historykey.ps1` and place it in the folder containing `historykey.py`
- By default `historykey.py` always uses `historykey.ps1`
### Run
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