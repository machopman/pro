import difflib


def readFile(name):
    a=[]
    with open(name, mode='r', encoding='utf-8-sig') as f:
        s = f.readlines()
        for i in s:
            y = i.replace('\n','')
            a.append(y)
    return a
a = readFile('ques.txt')

def message(event):

        e = difflib.get_close_matches(event,a)
        try:
           t =e[0]
           return t
        except:
           return event




def checkques(mess):
    result = message(mess)
    return result


