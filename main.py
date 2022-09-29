import os
def conversor(carteira):
    pasta = 'M:\Alexandre\\teste\webta\\'+carteira
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            print(os.path.join(os.path.realpath(diretorio), arquivo))
            caminho = os.path.join(os.path.realpath(diretorio), arquivo)
            file1 = open(caminho, 'r')
            file2 = open(caminho+'.txt', 'w')
            Lines = file1.readlines()
            NewLines = ''
            count = 0
            for line in Lines:
                 count += 1
                 print(f'Linha {count}: {line.strip()}')
                 NewLines += line
            file2.writelines(NewLines)
            file2.close()
            #os.remove(caminho)


conversor('CELPE')
conversor('COELBA')
conversor('COSERN')
