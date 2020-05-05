import subprocess
import platform
import modules.utils.lang as lang

def checkForOsPreRequisites():
    # the first pre-requisite is that the server is running under Linux / Unix (Debian, Ubuntu...)

    if platform.system() != "Linux":
        print(lang.incompatibleOsError())
        return False

    # check if this system has snmp library on it
    if subprocess.getstatusoutput("snmpwalk --version")[1] != "NET-SNMP version: 5.7.3":
        print("NÃO FOI POSSÍVEL ENCONTRAR O PACOTE SNMP v 5.7.3. POR FAVOR, INSTALE ATRAVÉS DO COMANDO\n $ sudo apt install snmp")
        return False

    return True