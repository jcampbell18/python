import texttable as tt

class Machine:
    # constructor
    def __init__(self, ip_addr, host_desc):
        self.ip_addr = ip_addr.strip("\r").strip("\n").strip()
        self.host_desc = host_desc.strip("\r").strip("\n").strip()
        self.mac_addr = ""
        self.host = ""
        self.vulnerabilities = {}
        self.services = {}
        self.totals = {}
        self.setupVulnerabilities()
        self.setupTotals()

    # 
    def setupVulnerabilities(self):
        self.vulnerabilities['ports'] = []
        self.vulnerabilities['protocols'] = []
        self.vulnerabilities['states'] = []
        self.vulnerabilities['services'] = []
        self.vulnerabilities['versions'] = []

    def setupTotals(self):
        self.totals['open_ports'] = 0
        self.totals['filtered_ports'] = 0

    def setVulnerabilities(self, port, pro, sta, serv, ver):
        self.vulnerabilities['ports'].append(port)
        self.vulnerabilities['protocols'].append(pro)
        self.vulnerabilities['states'].append(sta)
        self.vulnerabilities['services'].append(serv)
        self.vulnerabilities['versions'].append(ver)
        if sta == "open":
            self.increaseOpenPortCount()
        else:
            self.increaseFilteredPortCount()

    def setServices(self, data):
        self.services = data
    
    def setMacAddr(self, mac_addr):
        self.mac_addr = mac_addr

    def setHost(self, host):
        self.host = host

    def increaseOpenPortCount(self):
        self.totals['open_ports'] += 1

    def increaseFilteredPortCount(self):
        self.totals['filtered_ports'] += 1

    def getTotal(self):
        return self.totals['open_ports'] + self.totals['filtered_ports']

    def buildHeading(self):
        str  = f"\n"
        str += f"            IP Address: {self.ip_addr}\n"
        str += f"           MAC Address: {self.mac_addr}\n"
        str += f"             Host Name: {self.host}\n"
        str += f"             Host Desc: {self.host_desc}\n"
        str += f"Total Vulnerable Ports: {self.getTotal()}  (open: {self.totals['open_ports']}, filtered: {self.totals['filtered_ports']})\n"
        str += f"\n"
        return str

    def buildTable(self):
        str = ""
        if len(self.vulnerabilities['ports']) > 0:
            table = tt.Texttable()
            table.set_cols_align(["c", "c", "c", "c", "c"])
            headings = ['Port','Protocol','State','Service', 'Version']
            table.header(headings)
            for row in zip(self.vulnerabilities['ports'], self.vulnerabilities['protocols'], self.vulnerabilities['states'], self.vulnerabilities['services'], self.vulnerabilities['versions']):
                table.add_row(row)
            str += table.draw()
        return str

    def getData(self):
        return self.buildHeading() + self.buildTable() + "\n"