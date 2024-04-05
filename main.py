import os
import platform
import subprocess
import config as config

def listcaptures(capture,mode):
    cmd = f"{hashcat} {capture} --show -m {mode}"
    found = subprocess.run(cmd, capture_output=True)
    found = str(found.stdout)

    if found == "b''":
        print(f"No cracks found for {capture}")
    else:
        if not found == "b''":
            #print("\033[1;31;40mThe following password(s) was/were found:\033[0m")
            foundsplit = (found).split("\\r\\n")
            #print (foundsplit)
            
            #Formatting a text table so the output from found looks nice.
            print("\r\n\r\n\033[0;31;49m{0:20}| {1}\033[0m".format("SSID","Password"))
            header_divider = "-" * 30
            print(f"\033[0;31;49m{header_divider}\33[0m")
            fondsplit = [
                    "MGMT_WIFI:L3tM31n",
                    "GuestWIFI:Password"
            ]
            # Loop through all the found ssids and passwords
            for split in foundsplit:
               if ":" in split:
                    cleansplit = split.split(":")#[3]
                    ssid = cleansplit[3]
                    pwd = cleansplit[4]
                    print("{0:20}\033[0;31;49m| \33[0m {1}".format(ssid,pwd))
            print("\r\n\r\n")


# Gettting the OS platform to make sure if we need to run exe in Windows.
plat = platform.system()

if plat == "Windows":
    hcat = "hashcat.exe"
else:
    hcat = "hashcat"

# Getting directories and config settings
wificapdir = config.wificap #"\\monkeynet_16-ef-35-d3-18-94_eviltwin.22000"
pwddir = config.passwordir
hashcat = f"{config.hashcatdir}\\{hcat}"
rulesdir = config.rulesdir
displayresults = config.displayresults
mode = config.mode


# Checking if password list directory exis. If it is vaalide get a all the word list from the directory.
if not os.path.isdir(pwddir):
    print (f"Error: Directory for password list ({pwddir}) does not exist")
else:
    pwdlists = os.listdir(pwddir)

if not os.path.isdir(rulesdir):
    print (f"Error: Directory for password list ({rulesdir}) does not exist")
else:
    ruleslist = os.listdir(rulesdir)
print(ruleslist)

# Checking if the hash tune file is located in a diffeent directory than hashcat.  The switching to the directory that hashtune lives in
if config.hashtunedir == "":
    if os.path.isdir(config.hashtunedir):
        os.chdir(config.hashtunedir)
    else:
        os.chdir(config.hashcatdir)
else:
        print(f"Error: Directory for hashtune ({config.hashcatdir}) does not exist.")

# Checking if the hash cat directory exist. If it does exist, get all the password list from the password dir, then run hashcat with each one.
if not os.path.exists(hashcat):
    print(f"Error: Directory hashcat ({config.hashcatdir}) does not exist")
else:    
    # Time to verify if the config is pointing to a file or a directory for the captures
    if os.path.isfile(wificapdir):
        capext = os.path.splitext(wificapdir)
        if capext[1] == f".{mode}":    
            for list in pwdlists:
                wordlist = f"{pwddir}\\{list}"  
                if ruleslist:
                    for rule in ruleslist:
                        rulelist = f"{rulesdir}\\{rule}"
                        print(f"Using \033[0;32;49m{list}\033[0m against \033[0;31;49m{wificapdir}\033[0m with rules {rule}")
                        subprocess.run(f"{hashcat} -a 0 -w 3 {wificapdir} -m {mode} -o 2 {wordlist} -r {rulelist} --stdout")    
                else:
                    print(f"Using \033[0;32;49m{list}\033[0m against \033[0;31;49m{wificapdir}\033[0m")
                    subprocess.run(f"{hashcat} -a 0 -w 3 {wificapdir} -m {mode} -o 2 {wordlist} --stdout")

        # Display cracked info
        if displayresults == True:
                listcaptures(wificapdir,mode)                
        else:
            print(f"Error: Wifi capture {wificapdir} is not a .22000 file")
    else:
        # Catpures was not a file, verify that it is a directory. If it is a valid directory, get a list of captures and pass them to hashcat.
        if os.path.isdir(wificapdir): 
            wificaps = os.listdir(wificapdir)
            for wificap in wificaps:
                capext = os.path.splitext(wificap)
                if capext[1] == f".{mode}":
                    capfile = f"{wificapdir}\\{wificap}"
                    for list in pwdlists:
                        wordlist = f"{pwddir}\\{list}"
                        if ruleslist:
                            for rule in ruleslist:
                                rulelist = f"{rulesdir}\\{rule}"
                                print(f"Using \033[0;32;49m{list}\033[0m against \033[0;31;49m{wificapdir}\033[0m with the rules \033[0;34;49m{rule}\033[0m")
                                subprocess.run(f"{hashcat} -a 0 -w 3 {wificapdir} -m {mode} -o 2 {wordlist} -r {rulelist} --stdout")    
                        else:
                            print(f"Using \033[0;32;49m{list}\033[0m against \033[0;31;49m{wificapdir}\033[0m")
                            subprocess.run(f"{hashcat} -a 0 -w 3 {wificapdir} -m {mode} -o 2 {wordlist} --stdout")

            # Display cracked info
            if displayresults == True:
                listcaptures(capfile,mode)
        else:
            print(f"Error: Directory Wificap {wificapdir} does not exist")