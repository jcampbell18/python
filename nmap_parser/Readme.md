# nmap_parser

## Requirements 

- Install Nmap 7.80
    - Link: (https://Nmap.org/)
- Install Python 3.8.2
    - Link: https://www.python.org/)
    - Install library using pip: texttable 1.6.2
      - Link: https://pypi.org/project/texttable/

## Run the program

python main.py

## Documentation (How-to Guide)

### Create __init__.py

- This tells the Python to treat the directories like modules
- It is blank

### Create main.py

- Import os library to run Linux commands using the system() method
- Clear the screen with the system method from os
- Print intro of program, details of what it runs
- Prompt the user for filename
    - Defaults to “nmap_scan_parsed.txt” if nothing entered
- Prompt the user for the target
    - Defaults to my home network: 192.168.20.0/24 if nothing entered
- Assigns the nmap command to a string with its arguments, target and output file name
    - nmap -Pn -sS -sV -p 1-65535 [target] > nmap_scan_unparsed.txt
- Using the os system method, run the command
- Create a Report object sending the filename, command and target as parameters
    - Run the getSummaryReport method (screenshot below)
        - Display on screen and writes to file
        - Creates (or overwrites) file with the displayed Summary Report and a Detailed Report of each device found
### Create machine.py:

- Imports texttable
- Create constructor with an IP address and host description as parameters
    - Create instance variables
        - Create strings for Ip addresses and host description
        - Created empty strings for mac address and host (manufacturer)
        - Created empty dictionaries for the scanned ports (aka vulnerabilities), services, and totals (open ports and filtered ports)
    - Runs methods that set up the empty dictionaries for the vulnerabilities and totals
- Methods that set up dictionaries (listed above)
    - Vulnerabilities
        - Keys: ports, protocols, states, services, versions
        - Values for each key: empty list
    - Totals
        - Keys: open_ports, filtered_ports
        - Values for each key: 0
- Setter methods (sets instance variable to value)
    - Mac Address
    - Host
    - Services
- Other methods
    - Method that increases the open port count by 1
    - Method that increases the filtered port count by 1
    - Method that adds the number of open ports and filtered ports
        - Returns the total
- Method(s) to display:
    - Basic info: IP Address, Mac Address, Host, host description, Total number of vulnerable ports, open ports, and filtered ports
        - Returns as string
    - A table of the vulnerable port information (port, protocol, state, service, and version)
        - If the host is found, but no vulnerabilities, then return an empty string, otherwise return table as string
    - Returns the data of both methods above (basic info + table)

### Create fileParser.py

- Imports machine
- Create constructor with the filename as the parameter
    - Create instance variables
        - Create string for filename
        - Create empty strings for timestamp, nmap_version, machine
        - Create empty list for machines found (list of machines)
        - Create a counter, starting at 0
- Method that opens the file
    - Opens the file
    - Reads a line, and has the line parsed
    - When finished reading, closes the file
    - Returns true after closing file
- Method that parses the line
    - Nmap has particular statements that can be separated
        - If the line contains “Starting Nmap” then send to timestamp setter
        - If the line contains “Nmap scan report” then:
            - If the counter is not equal to 0, then add the last machine to the list, and reassign machine to an empty string
            - Increase the counter
            - Send to machine setter
        - If the line contains “/tcp” or “/udp” then send to scanned port setter
        - If the line contains “MAC Address” then send to mac address setter
        - If the line contains “Services Info” then send to services setter
- Getter methods
    - Return the timestamp
    - Return the nmap_version
    - Return the list of machines
    - Return the total vulnerabilities found
- Setter methods
    - Timestamp (takes in the read line from file as parameter)
        - Parses and sets the instance variables timestamp and nmap_version
    - Machine (takes in the read line from file as parameter)
        - Parses and sets the machine with ip address and host description as parameters as new Machine instance
    - Scanned Port (takes in the read line from file as parameter)
        - Parses and adds vulnerabilities to the Machine instance (port, protocol, state, service, and version)
            - If version isn’t listed, then send empty string
    - Mac Address (takes in the read line from file as parameter)
        - Parses and sets the instance variables Mac address and Host name
    - Service(s) (takes in the read line from file as parameter)
        - Parses and adds Services to the Machine instance
            - Since device can have multiple services, create a dictionary and each service contains its own key with the value being the description (separated by semicolon)
- Method that displays each machine
    - Run a for loop over each machine in the list of machines (instance variable)
        - Each listed machine can call a machine method to get all data
    - Returns a string of all machines

### Create report.py

- constructor with filename, command and target as parameters
     - Create instance variables
        - Create string for filename, command and target
        - Create empty string for timestamp, nmap version
        - Create empty list for machines
        - Create integers for total devices and total vulnerabilities; set to 0
        - Create FileParser object with the file “nmap_scan_unparsed.txt”
        - Run method that starts the Report
- Method to start the report
    - FileParser calls openFile method
        - If returns true, then:
            - Get the nmap version from FileParser
            - Get the timestamp from FileParser
            - Get the list of machines from FileParser
            - Get the number of machines (from the list)
            - Get the number of vulnerabilities from method
            - Get the summary report
- Method to get the total vulnerabilities
    - Create an integer with value of 0 that counts the total
    - Create for loop of all devices found
        - For each device add the number of open ports and filtered ports to the total
    - Returns the total
- Method to get revised list of devices
    - Create empty string for device list
    - Create a counter starting at 0
    - Create for loop of all devices found
        - Add a line to the string, with the IP address and host description
            - If host description is empty, use host name
    - Returns the string
- Methods for Reports
    - Summary Report (for screen and file)
        - Create a empty string
        - Add Nmap version to string
        - Add target to string
        - Add timestamp to string
        - Add number of machines found to string
        - Add ys number of vulnerabilities found to string
        - Add quick view of machine list to string
            - Method call to get the device list
        - Calls method to write the report with the string as parameter
        - Returns string
    - Write the Report with a string for the summary report as parameter
        - Create a string and assign the summary report to it
        - Add to string by calling the FileParser’s method to display the machines
        - Using a try and finally:
            - Try opening the filename the user specified with a writing permission (and overwrite)
            - Write the string to the file
            - Finally, close the file
