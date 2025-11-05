citys = ("BH", "RIO", "SP")
print(citys[1])

list_citys = list(citys)
list_citys.append("FLORIPA")

citys = tuple(list_citys)

print(citys)