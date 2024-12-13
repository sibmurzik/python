# "Генераторы"

def all_variants(text):
    line = str(text)
    for sym_qty in range(1, len(line) + 1):
        for index in range(len(line)):
            if index + sym_qty > len(line):
                continue
            yield line[index: index + sym_qty]


a = all_variants("abchj")
for i in a:
    print(i)

a = all_variants("a")
for i in a:
    print(i)
