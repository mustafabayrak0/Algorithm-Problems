def read_txt(path: str):
    txt = open(path, "r").read()
    return txt
def manipulate(txt: str):
    txt = txt.lower()
    txt = txt.replace("a", "1")
    txt = txt.replace("e", "2")
    txt = txt.replace("i", "3")
    txt = txt.replace("o", "4")
    txt = txt.replace("u", "5")
    txt = txt[::-1]
    return txt

def write_to_txt(path: str, to_write: str):
    f = open(path, "w")
    f.write(to_write)
    f.close()

in_path = input()
out_path = input()
file = read_txt(in_path)
edited_file = manipulate(file)
write_to_txt(out_path, edited_file)
