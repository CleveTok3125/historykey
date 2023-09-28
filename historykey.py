import time, subprocess, win32api, configparser
config = configparser.ConfigParser()
config.read('historykey.ini')
limit = int(config.get('HISTORYKEY_SETTING', 'LIMIT'))
count = 0
if str(config.get('HISTORYKEY_SETTING', 'RUN_GENSHIN_IMPACT')).upper() == "TRUE":
	subprocess.run(config.get('HISTORYKEY_SETTING', 'GENSHIN_PATH'))
while True:
	try:
		powershell_command = 'Powershell.exe -executionpolicy remotesigned -File  historykey.ps1'
		output = subprocess.check_output(['powershell', '-Command', powershell_command], shell=True, text=True)
		if "Link copied to clipboard, paste it back to paimon.moe" in output:
			win32api.MessageBox(0, output.split("\n")[2][0:50]+"..."+output.split("\n")[2][round(len(output.split("\n")[2])/2)-25:round(len(output.split("\n")[2])/2)+25]+"..."+output.split("\n")[2][-50:-1], "Link copied to clipboard")
			break
		elif "Cannot find the wish history url! Make sure to open the wish history first!" in output:
			raise ValueError("Cannot find the wish history url! Make sure to open the wish history first!")
		else:
			None
	except:
		count += 1
		if count >= limit:
			win32api.MessageBox(0, "Can't find link after "+str(limit)+" attempt(s)", "Error")
			break
	time.sleep(1)