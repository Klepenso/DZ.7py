
def search_view_number(contact):
    f = open(r'telephon_book.txt', 'r')
    line_new = f.readlines()
    f.close()
    for line in line_new:
        if line.find(contact) == 0:
            print(line)
