import os
from report import Report
os.system('clear')

print("""
----------------------------------------------------------------------------------------------
Welcome to a customized Nmap Scanner
----------------------------------------------------------------------------------------------
- The importance of this lab is to show a connection between Python and Nmap (or Networking).
    Python is a general-purpose high-level language that has a vast library, easy to learn,
    and has the ability to run linux commands (scripting) and parse collected data. In this
    case, Nmap's scanned output. The parsed reconnaissance can be simplified down to a summary
    report that can instantly show an overview of vulnerabilities.

- In this program: 

    - The user will enter the filename and target that they want to perform reconnaissance on

        1) If a filename is not used, it will be defaulted to \"nmap_scan.txt\"
        2) The target can be a hostname, ip addresses, networks, etc. Examples:
            1) ewu.edu
            2) 192.168.20.1
            3) 192.168.20.1-255
            4) 192.168.20.0/24

    - Nmap scanner will then perform a scan using the arguments: nmap -Pn -sS -sV -p 1-65535

        1) -Pn          treat all hosts as online (skips host discovery)
        2) -sS          stealth scan or SYN scan (doesn't complete TCP connection)
        3) -sV          service/version detection
        4) -p 1-65535   only scan within port range

    - All of the output of the scan will then be written on the named file

    - Finally, a summary and detailed report will be display on the screen and written to a
        file after parsing all the collected data from the file.
----------------------------------------------------------------------------------------------
""")

filename = input("Enter the name of the file you want to output to (default: nmap_scan_parsed.txt): ")

if len(filename) < 3:
    filename = "nmap_scan_parsed.txt"

target = input("Enter the target (hostname, ip addresses, networks, etc): ")

if len(target) < 3:
    target = "192.168.20.0/24"

command = "nmap -Pn -sS -sV " + target + " -p 1-65535 > nmap_scan_unparsed.txt"

print("\nperforming Nmap...")
os.system(command)
print("performing data parsing...\n")

report = Report(filename, command, target)
print(report.getSummaryReport())