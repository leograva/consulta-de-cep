#imports
from pycep_correios import get_address_from_cep
from pycep_correios.exceptions import BaseException

#Laço try/except para tratamento de exceções
try:
    #Consultando o cep na  base dos correios
    endereco = pycep_correios.get_address_from_cep('03311000')
    
    #Imprimindo na tela os dados consultados
    print('*************** Endereço ***************')
    print("Endereço:",endereco["logradouro"])
    print("Bairro:",endereco["bairro"])
    print("Endereço:",endereco["cidade"])
    print("Endereço:",endereco["uf"])
    print("Endereço:",endereco["cep"])
    print('****************************************')
#Em caso de erro, imprimir o código de erro trazido pela exceção da API
except BaseException as exc:
    print('Erro:',exc)
