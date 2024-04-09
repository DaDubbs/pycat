# pycat
Script to automate using multiple wordlist against caputured WIFI handshakes using hashcat

# Prequisites
There are a few prequisites that you will need. Those are:

- Capture handshakes
- Install Python
- Install Hashcat

## Capturing Handshakes
** DISCLAIMER **
Remember to only capture handshakes from networks that you have permission to capture them from.

You can use hardware devices such as the Wifi Pineapple by Hak5, a pwnagotchi, flipper zero and other such devices.  Another option is to run softare like aircrack, to capture handshakes using a computer. 

### Converting pcaps
If you have a pcap file, it will need to be converted to a supported file for Hashcat. Hashcat has a [Converter tool](https://hashcat.net/cap2hashcat/) that can assist in converting pcaps to a 22000 file format. This is not always successful, but it it is worth trying.

## Installing Python
Python.org has a Wiki page that is best on how to install Python itself. 

[Python Install Docs](https://wiki.python.org/moin/BeginnersGuide/Download)

## Installing Hashcat

### Windows:
Download the 7zip that contains everything you need from [Hashcat's website](https://hashcat.net/hashcat/). Once the files are downloaded, extract them. In the directory that the files were extracted to thee will be a hashcat.exe file.  ** NOTE: This directory is needed for the config.py file.***

### Linux
Install Hashcat with your local repo manager.  For Debian users, such as Kali, Ubuntu, etc use the following:
```
sudo apt install hashcat
```

### MacOS
Install Homebrew:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Then install Hashcat 

```
brew install hashcat
```


# Configuring pycat
Now that the prequisites are out of the way.  You will need to modify the config.py file. This file contains information about your setup such as where the 22200 files are locate, where hashcat is stored, and a few other options. 

## Modiying the Config.py file
The config.py file has six variables. Three of the variables will need to be changed, the other three can be left at their default unless there is a need to change them.

###  wificap
This variable is for the directory, or file location that the 22000 files are stored at.

### passworddir
This is the path to where the wordlist are stored.

### hashcatdir
This is for Windows users only. It will tell the script where the hashcat.exe is stored.

### hashtunedir
If your hashcat tune file is not located in the same directory as hashcat, then hashcat will display an error. This should be changed only if that error is encountered.

### ruledir
This is the location where custom rules are applied, for example adding additional characters at the end of each wordlist entry. Using this will increase the amount of time it takes hashcat to crack a hash since it has more entries to test.

### displayresults
If you want to display all the cracked passwords, set this value to true. It will run hashcat --show <capture> -m <mode>

### mode
This is the mode that hashcat will use to try to crack the file. This should be 22000 or 22001. 

# Running Pycat
Once the config file has been updated.  Open a terminal/command prompt and change directories until you are in the PyCat directory. Once there run the following:

```
python main.py
```
** Note: You may need to use python3 instead of python depending on your environment variables**

If displayresults is set to True, the output will be similar to the following.

![Example of PyCat output.](/output/output.png)
