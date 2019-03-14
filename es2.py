string = input("Inserisci una stringa: ")
if len(string) < 5:
    string = ""
else:
    string = string[:2]+string[-2:]

print(string)