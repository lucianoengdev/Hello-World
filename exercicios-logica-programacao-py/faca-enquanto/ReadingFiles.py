"""Reading Files
Leia um arquivo .txt e imprima o conteúdo.
Conte quantas linhas o arquivo tem."""

file_work = open("file.txt", "r")


count_line = 0
for i in file_work:
    print(i, end= "")
    count_line +=1

print()
print(count_line)
        