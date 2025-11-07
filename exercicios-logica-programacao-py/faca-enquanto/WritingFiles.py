"""Writing to Files
Crie um arquivo e escreva 3 linhas.
Acrescente uma linha ao arquivo sem apagar o conteúdo."""

new_file = open("NewFile.txt", "w")
new_file.write("Testing this code\n")
new_file.write("I think its ok\n")
new_file.write("It running ok\n")

new_file.close()

new_file = open("Newfile.txt", "a")
new_file.write("Texting using append")