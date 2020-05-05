#coding:utf8
from modules.system import osrequeriments
from models.Host import Host
from modules.utils import snmpwalk

def main():

    if osrequeriments.checkForOsPreRequisites():
        print ("system is compatible")

    test = Host("roteador", "192.168.1.1")
    test.setSnmpCommunity("public")
    
    print(test.toJSONString())

    query = snmpwalk.snmpwalkQuery(test)

    print(query)

if __name__ == "__main__":
    main()