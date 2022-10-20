
def del_phone_number(contact):
    f = open(r'telephon_book.txt', 'r')
    line_new = f.readlines()
    f.close()
    f = open(r'telephon_book.txt', 'w')
    for line in line_new: 
        if line.find(contact) == -1:
            f.write(line)
    f.close()
    