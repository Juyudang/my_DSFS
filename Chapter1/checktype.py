# 말 그대로 somethig의 타입을 알려준다.
def checktype(something):
    flag = isinstance(something, int)
    if flag == True: return print('int')

    flag = isinstance(something, float)
    if flag == True: return print('float')

    flag = isinstance(something, complex)
    if flag == True: return print('complex')

    flag = isinstance(something, str)
    if flag == True: return print('str')

    flag = isinstance(something, list)
    if flag == True: return print('list')

    flag = isinstance(something, dict)
    if flag == True: return print('dict')

    flag = isinstance(something, tuple)
    if flag == True: return print('tuple')

    flag = isinstance(something, set)
    if flag == True: return print('set')