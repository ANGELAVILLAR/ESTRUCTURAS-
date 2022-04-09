Alfabeto=('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
Texto=str(input('Dgite la palabra: '))
contar=0

for i in Texto:
    if i in Alfabeto:
        contar+=1
        print('se ha encontrado caracteres alfabéticos:')
    else:
        print('No se ha encuentrado caracteres alfabeticos ')