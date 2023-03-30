x = '❤️'
y = f"{x.encode('utf-8')}"
y = y.replace("\\x","%").upper()[2:-1]
print()

