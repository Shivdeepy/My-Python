import subprocess

#path="/mnt/c/Users/shivdeep.k/Downloads/MobaXterm_Portable_v11.1/MobaXterm_Personal_11.1.exe"
#command = "MobaXterm_Personal_11.1"
#os.system(command)
#subprocess.Popen(path,command)

path = 'C:\\Users\\shivdeep.k\\Google Drive\\Programming\\Python\\atoz.py'
command = ["python3",path]
stdout = ''
stderr = ''
#command = ['/mnt/c/Users/shivdeep.k/Downloads/MobaXterm_Portable_v11.1/MobaXterm_Personal_11.1.exe' ,  "MobaXterm_Personal_11.1"]
subprocess.Popen(command, shell=True, 
stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(stdout)
print(stderr)