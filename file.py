
with open("text.txt", "w") as file:
    file.write(".\n")


with open("sample.txt", "r") as file:
    content = file.read()
    print(content)