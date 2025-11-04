def sum(a,b):
    '''
    :param a:
    :param b:
    :return: 
    '''
    print("a:",a,"this is a ok & concate"+" hello by +")
    x = 5
    print("x:",x,"This is local")
    print("y:", y, "This is global")
    return a+b

y = 10
total = sum(b=5,a=6)
print("x:", x, "This is local and error")
print(total)