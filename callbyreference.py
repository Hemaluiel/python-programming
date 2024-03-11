string = "Geeks"

def test(string):
    string = "GeeksforGeeks"
    print("Inside Function:", string)

test(id(string))
print("Outside Function:", string)