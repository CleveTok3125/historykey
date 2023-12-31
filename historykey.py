import time, subprocess, win32api, psutil, os, sys, warnings

def wish_history():
	powershell_command = 'Powershell.exe -executionpolicy remotesigned -File  historykey.ps1'
	output = subprocess.check_output(['powershell', '-Command', powershell_command], shell=True, text=True)
	if "Link copied to clipboard, paste it back to paimon.moe" in output:
		for i in output.split("\n"):
			if 'http' in i:
				output = i
		win32api.MessageBox(0, output[0:50]+"..."+output[round(len(output)/2)-25:round(len(output)/2)+25]+"..."+output[-50:-1], "Link copied to clipboard")
		return True
	elif "Cannot find the wish history url! Make sure to open the wish history first!" in output:
		warnings.warn('Cannot find the wish history url! Make sure to open the wish history first!')
		return False
	else:
		return False

def is_true_fn():
	cwf = os.path.basename(sys.argv[0])
	if (cwf == 'historykey.py') or (cwf == 'historykey.exe'):
		return True
	return False

def is_running():
	processes = psutil.process_iter()
	list_proc = []
	for p in processes:
		if p.name() == 'historykey.exe':
			list_proc.append(p.name())
	num_proc = len(list_proc)
	if (num_proc == 1) or ((num_proc % 2 == 0) and (num_proc > 2)):
		return True
	else:
		return False

def is_depen_exst():
	return os.path.exists("historykey.ps1")

if is_true_fn() == False:
	win32api.MessageBox(0, "Unable to locate executable file", "Error")
elif is_running():
	win32api.MessageBox(0, "Another Instance Is Already Running.", "Error")
elif is_depen_exst() == False:
	win32api.MessageBox(0, 'Could not find dependency file "historykey.ps1"', "Error")
else:
	if not wish_history():
		while True:
			try:
				processes = psutil.pids()
				for process in processes:
					name = psutil.Process(process).name()
					if "GenshinImpact" in name:
						if wish_history():
							break
			except:
				None
			time.sleep(1)