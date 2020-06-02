from machine import Machine

class FileParser:
    def __init__(self, filename):
        self.filename = filename
        self.nmap_version = ""
        self.timestamp = ""
        self.machine = ""
        self.machinesFound = []
        self.ix = 0

    def openFile(self):
        fo = open(self.filename, 'r')
        for line in fo:
            self.parseLine(line)
        fo.close()
        return True

    def parseLine(self, line):
        if "Starting Nmap" in line:
            self.parseTimestamp(line)
        elif "Nmap scan report" in line:
            if self.ix != 0:
                self.machinesFound.append(self.machine)
                self.machine = ""
            self.parseMachine(line)
            self.ix += 1
        elif "/tcp" in line or "/udp" in line:
            self.parsePort(line)
        elif "MAC Address" in line:
            self.parseMac(line)
        elif "Service Info" in line:
            self.parseServ(line)

    def getTimestamp(self):
        return self.timestamp

    def getNmapVersion(self):
        return self.nmap_version

    def getMachinesFound(self):
        return self.machinesFound

    def getTotalVulnerabilities(self):
        return self.total_vulnerabilities

    def parseTimestamp(self, line):
        data = line.split(" ")
        new_array = []
        for d in range(len(data)):
            if data[d] == "at":
                ix = d
        for d in range(ix+1, len(data)):
            new_array.append(data[d])
        self.timestamp = (" ").join(new_array)
        self.nmap_version = data[2]

    def parseMachine(self, line):
        data = line[21:].split(" ")
        ip_addr = ""
        host_desc = ""
        if len(data) == 1:
            ip_addr = data[0]
        else:
            host_desc = data[0]
            ip_addr = (data[1])[1:-2]
        self.machine = Machine(ip_addr, host_desc)

    def parsePort(self, line):
        data = line.split()
        portInfo = data[0].split("/")
        if len(data) > 3:
            new_array = []
            for v in range(3, len(data)):
                new_array.append(data[v])
            ver = (" ").join(new_array)
        else:
            ver = ""
        self.machine.setVulnerabilities(portInfo[0], portInfo[1], data[1], data[2], ver)

    def parseMac(self, line):
        data = line.split()
        mac_addr = data[2]
        new_array = []
        host = ""
        if len(data) > 3:
            for d in range(3, len(data)):
                new_array.append(data[d])
            temp = (" ").join(new_array)
            host = temp[1:-1]
        self.machine.setMacAddr(mac_addr)
        self.machine.setHost(host)

    def parseServ(self, line):
        cat = {}
        line = line[14:]
        data = line.split(";")
        for d in data:
            data_split = d.split(": ")
            key = data_split[0]
            
            if "," in data_split[1]:
                val = []
                values = (data_split[1]).split(", ")
                for v in values:
                    val.append(v)
            else:
                val = data_split[1]
            cat[key] = val
        self.machine.setServices(cat)

    def displayMachines(self):
        str = ""
        for m in self.machinesFound:
            str += m.getData()
        return str