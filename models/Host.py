class Host:

    def __init__(self, hostname, ip_address, snmp_community="public", snmp_version = "v2c", snmp_port = "161"):
        self.hostname = hostname
        self.ip_address = ip_address
        self.snmp_community = snmp_community
        self.snmp_version = snmp_version
        self.snmp_port = snmp_port
        

    def setHostname(self, name):
        self.hostname = name

    def setIpAddress(self, ipaddress):
        self.ip_address = ipaddress

    def setSnmpCommunity(self, snmp_community):
        self.snmp_community = snmp_community
    
    def setSnmpVersion(self, snmp_version):
        self.snmp_version = snmp_version

    def setSnmpPort(self, snmp_port):
        self.snmp_port = snmp_port


    def getHostname(self):
        return self.hostname

    def getIpAddress(self):
        return self.ip_address

    def getSnmpCommunity(self):
        return self.snmp_community
    
    def getSnmpVersion(self):
        return self.snmp_version

    def getSnmpPort(self):
        return self.snmp_port

    def toString(self):
        return self.hostname+self.ip_address+self.snmp_community+self.snmp_port+self.snmp_version

    def toCSVString(self):
        return self.hostname+","+self.ip_address+","+self.snmp_community+","+self.snmp_port+","+self.snmp_version

    def toJSONString(self):
        return {
            'hostname': self.hostname,
            'ip_address': self.ip_address,
            'snmp_community': self.snmp_community,
            'snmp_port': self.snmp_port,
            'snmp_version': self.snmp_version
        }
