import os
import pyaes

#abrir o arquivo a criptografado
file_name = "meu_teste.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

#chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypted_data = aes.decrypt(file_data)

#remove o arquivo que foi selecionado criptografado
os.remove(file_name)

#cria um arquivo descriptografado
new_file = "meu_teste.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypted_data)
new_file.close()