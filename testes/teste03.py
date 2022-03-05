import time
import getpass, sys
import pyAesCrypt
from os import stat, remove
bufferSize = 64 * 1024
escolha = input('digite: \n1- Criptografar \n2- Descriptografar\nR: ')
nome = input('Informe o nome do arquivo: ')
print('Exemplo de extensões (digite somente as letras): txt, docx, pdf, .xlsx, rar')
extensao = input('Informe a extensão do arquivo: ').lower().strip()
password = getpass.getpass('\nDigite a Senha:')
if escolha == '1':
    passwordconfirm = getpass.getpass('\nConfirme a senha:')
    if password == passwordconfirm:
        if escolha == '1':
            # encrypt
            with open(f"{nome}.{extensao}", "rb") as fIn:
                with open(f"{nome}.{extensao}.aes", "wb") as fOut:
                    pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
            x = ' '
            while x not in 'SN':
                x = input('Gostaria de deletar o arquivo? [S/N]: ').upper().strip()[0]
            if x != 'S':
                print('\nok')
                time.sleep(1)
                sys.exit()
            remove(f"{nome}.{extensao}")
            print('Arquivo removido')
            time.sleep(2)
            sys.exit()
if escolha == '2':
    # get encrypted file size
    encFileSize = stat(f"{nome}.{extensao}.aes").st_size
    # decrypt
    with open(f"{nome}.{extensao}.aes", "rb") as fIn:
        try:
            with open(f"{nome}.{extensao}", "wb") as fOut:
                # decrypt file stream
                pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
        except ValueError:
            print('senha incorreta')
            # remove output file on error
            remove(f"{nome}.{extensao}")
    time.sleep(2)
    deletar = ' '
    while deletar not in 'SN':
        deletar = input('Gostaria de deletar o arquivo criptografado?[S/N]: ').upper().strip()[0]
        if deletar == 'S':
            remove(f"{nome}.{extensao}.aes")
            print('Arquivo Criptografado deletado.')
    time.sleep(2)
    sys.exit()
print('\n\nEscolha errada')
time.sleep(2)