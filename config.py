#Location of the wifi h2000 file
wificap= "Path\\To\\Wifi\\Capture"

# Directory where all the password list are located
passwordir = "Path\\To\\Password\\Lists"

#Directory whee hashcat is located. Only for Windows users
hashcatdir = "Path\\To\\Hashcat"

#If for hashcat.hctune is located in a different directory than hashcat. This is needed if you get an error about hashtune is not found.
hashtunedir = ""

# Boolean value
displayresults = True

# Hashcat Mode
mode = 22000

#Formatting a text table so the output from found looks nice.
print("\r\n\r\n\033[0;31;49m{0:20}| {1}\033[0m".format("SSID","Password"))
header_divider = "-" * 30
print(f"\033[0;31;49m{header_divider}\33[0m")
foundsplit = [
        "MGMT_WIFI:L3tM31n",
        "IPStandingUp:IWithCUP",
        "BillWitheScience Fi:Sc13nc3Guy",
        "NetGear64G:Password123"
]
# Loop through all the found ssids and passwords
for split in foundsplit:
    if ":" in split:
        cleansplit = split.split(":")#[3]
        ssid = cleansplit[0]
        pwd = cleansplit[1]
        print("{0:20}\033[0;31;49m| \33[0m {1}".format(ssid,pwd))
print("\r\n\r\n")