SYSTEM_DEFAULT_LANGUAGE = 'pt-BR'



IMCOMPATIBLE_OS_ERROR = {
    'pt-BR':"ERRO: O SISTEMA OPERACIONAL DO SERVIDOR É IMCOMPATÍVEL COM ESTE PROGRAMA. POR FAVOR, CERTIFIQUE-SE DE UTILIZAR UM SISTEMA COMPATIVEL",
    'en-US':'ERROR: THE OPERATIONAL SYSTEM OF THIS SERVER IS IMCOMPATIBLE WITH THIS PROGRAM. PLEASE CERTIFY THAT USES AN COMPATIBLE SYSTEM'
    }


def incompatibleOsError():
    return IMCOMPATIBLE_OS_ERROR[SYSTEM_DEFAULT_LANGUAGE]

