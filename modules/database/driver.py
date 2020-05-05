import sqlite3
from models.Host import Host
DATABASE = "slv-snmp-database.sqlite3"

def createSchema():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS HOSTS
                (HOSTNAME text, IP_ADDRESS text, SNMP_COMMUNITY text, SNMP_VERSION text, SNMP_PORT text)''')
    conn.commit()
    conn.close()

def insertHostIntoHosts(host):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    INSERT_EXECUTE = "INSERT INTO HOSTS VALUES ('%s','%s','%s','%s','%s' )"%(
        host.getHostname(), host.getIpAddress(), host.getSnmpCommunity(), host.getSnmpVersion(), host.getSnmpPort() )
    
    c.execute(INSERT_EXECUTE)

    conn.commit()
    conn.close()
