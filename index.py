def kiir_file(file):
    h = open(file, encoding="UTF-8")
    for sor in h:
        f.write(sor)
    h.close()

def main():
    global f
    f = open("index.html", "w", encoding="UTF-8")
    kiir_file("header_and_nav.txt")
    kiir_file("rolunk.txt")
    kiir_file("celunk.txt")
    kiir_file("footer.txt")
    f.close()

main()