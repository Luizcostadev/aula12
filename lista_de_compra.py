lista_de_compra = []
op = -1
while op != 0:
    print("1 Adioionar novo item")
    print('2 Remover item')
    print('3 Exibir lista')
    print('0 Sair do programa')
    op = int(input('Escolha uma opção: '))

    if op == 1:
        item = input('Digite o novo item')
        print('Novo item')
        lista_de_compra = lista_de_compra + [item]
        print (f' o item {item}foi adicionado')
    
    elif op == 2:
        print('\n')
        print('remover item')
        print(lista_de_compra)

    elif op == 3:
        print('\n')
        print('Exibir lista')

        for i in range (len(lista_de_compra)):
            print (f'{i+1}{lista_de_compra[i]}')

    elif op == 0:
        print('Saindo do programa')

    else:
        print('Opção invalida')
    
    