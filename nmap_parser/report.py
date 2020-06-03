
from fileParser import FileParser

class Report:
    def __init__(self, filename, command, target):
        self.filename = filename
        self.command = command
        self.target = target
        self.nmap_version = ""
        self.timestamp = ""
        self.total_devices = 0
        self.total_vulnerabilities = 0
        self.devices = []
        self.fp = FileParser("nmap_scan_unparsed.txt")
        self.startReport()

    def startReport(self):
        if (self.fp.openFile()):
            self.nmap_version = self.fp.getNmapVersion()
            self.timestamp = self.fp.getTimestamp()
            self.devices = self.fp.getMachinesFound()
            self.total_devices = len(self.devices)
            self.total_vulnerabilities = self.getTotalVulnerabilities()
            self.getSummaryReport()

    def getTotalVulnerabilities(self):
        total = 0
        for dev in self.devices:
            open_ports = dev.totals['open_ports']
            filtered_ports = dev.totals['filtered_ports']
            total += open_ports + filtered_ports
        return total

    def getDeviceList(self):
        device_list = ""
        ix = 0
        for dev in self.devices:
            ip_addr = dev.ip_addr
            if dev.host_desc == "":
                host = dev.host
            else:
                host = dev.host_desc
            device_list += f"\t{dev.ip_addr}\t|\t{host}\n"

            if ix < len(self.devices) -1:
                device_list += f"\t" + "-" * 16 + "+" + "-" * 50 + "\n"
            ix += 1
        return device_list

    def writeReport(self, summaryReport):
        str = ""
        str += summaryReport
        str += self.fp.displayMachines()
        try:
            f = open(self.filename, "w+")
            f.write(str)
        finally:
            f.close()

    def getSummaryReport(self):
        str  = f"-" * 100 + "\n"
        str += f"Nmap Scan Report:\n"
        str += f"-" * 100 + "\n"
        str += f"                    Nmap Version:\t{self.nmap_version}\n"
        str += f"                    Nmap Command:\t{self.command}\n"       
        str += f"                          Target:\t{self.target}\n"
        str += f"                       Timestamp:\t{self.timestamp}"
        str += f"-" * 100 + "\n"
        str += f"        Total # of Devices found:\t{self.total_devices}" + "\n"
        str += f"Total # of Vulnerabilities found:\t{self.total_vulnerabilities}" + "\n"
        str += f"-" * 100 + "\n"
        str += f"Device List:\n\n"
        str += f"\tip address\t|\tdevice name\n"
        str += f"\t" + "=" * 16 + "+" + "=" * 50 + "\n"
        str += self.getDeviceList()
        str += f"\t" + "-" * 16 + "+" + "-" * 50 + "\n\n"
        str += f"-" * 100 + "\n"
        str += f"For a detailed report, please view the file \'" + self.filename + "\' with a text editor\n"
        str += f"For the unparsed Nmap file, please view the file \'nmap_scan_unparsed.txt\' with a text editor\n"
        self.writeReport(str)
        return str
