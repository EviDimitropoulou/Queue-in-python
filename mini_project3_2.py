lista=[]
print(lista)
inp=None
while True:
    inp=input('New element:')
    if inp=='q':
        break
    elif '0r' in inp:
        #delete from start of the queue
        del lista[0]
        print(lista)
           
    elif inp=='r':
        #delete from end of the queue
        del lista[-1]
        print(lista)
        
    elif '0' in inp:
       #input at start of the queue
        i=inp[1:]
        lista.insert(0,i)
        print(lista)
    else:
        #input at the end of the queue
       
        lista.append(inp)
        print(lista)
print('Telos')
