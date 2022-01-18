import os
import argparse
from posixpath import split
import time

pasta = './novapasta'

for caminho, diretorios, arquivos in os.walk(pasta):
    sep = '┣━'
    head, tail = os.path.split(caminho)
    if head.find(pasta) == -1:
        print(sep+tail)
    else:
        while head:
            sep += '━'
            head, _tail = os.path.split(head)
        print(sep+'┗━'+tail)
    # for arquivo in arquivos:
    #     print(sep+'┗━'+arquivo)
