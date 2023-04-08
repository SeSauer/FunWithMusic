
Notes = {}

file = open("Music\\noten.txt")
lines = file.readlines()
for line in lines:
    try:
        if line[0] == "#": continue
        literals = line.split()
        names = literals[0].split("/")
        for name in names:
            name = name.upper()
            Notes[name] = literals[1]
    except Exception:
         raise Exception("Error in: " + line)


if __name__ == "__main__":
        print(Notes)