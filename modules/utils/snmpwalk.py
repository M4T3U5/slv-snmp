import subprocess
from models.Host import Host


def getResultFromExec(command):
    proccess = subprocess.getstatusoutput(command)

    if proccess[0] == 0:
        return proccess[1]
    return "ERROR (STATUS: "+str(proccess[0])+") -> "+proccess[1]

def snmpwalkQuery(host):
    query_string = "snmpwalk -%s -c %s %s"%(host.snmp_version, host.snmp_community, host.ip_address)
    return getResultFromExec(query_string)    

def snmpQueryByOID(host, oid):

    query_string = "snmpwalk -%s -c %s %s %s"%(host.snmp_version, host.snmp_community, host.ip_address, oid)
    return getResultFromExec(query_string)

