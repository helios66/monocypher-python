W = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
     'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
     '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 
     '[', '-' , '+' , '.' , '^' , '@' , '_' , ':' , '*' ,',' ,']']

UW = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O',
      'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 
      '5', '9', '6', '7','8', '1', '2', '3','0', '4', 
      '-' , '_' , ':' , ',', '[' ,']', '+' , '.' , '^', '*' , '@']


def en(value):
    c = []
    for i in xrange(len(value)):
        for j in xrange(len(W)):
            if value[i].lower() == W[j]:
                c.append(UW[j])
                break            
    return ''.join(c)

def dc(value):
    p1 = []
    for i in xrange(len(value)):
        for j in xrange(len(UW)):
            if UW[j] == value[i]:
                p1.append(W[j])
    return ''.join(p1)


print(en("user1234@abc.com"))
print(dc(en("user1234@abc.com")))