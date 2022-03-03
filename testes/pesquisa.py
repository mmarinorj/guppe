opcao = int
entrevistados = 0
soma_idades = 0
ios = 0
android = 0


while opcao != 0:
    print('[ 1 ] Iniciar entrevista')
    print('[ 2 ] Exibir relatório')
    print('[ 0 ] Sair')
    opcao = int(input('Digite uma das opções acima: '))

    if opcao == 1:
        entrevistados += 1  # Contador dos entrevistados. É o mesmo que entrevistados = entrevistados + 1
        cliente = input('Olá, diga seu nome: ').lower().capitalize() # coloca tudo em minusculo e depois só a primeira em maiúscula
        print(f'Seja bem vindo(a), {cliente}!')

        idade = int(input('Por favor, qual sua idade? '))
        soma_idades += idade  # soma_idades = soma_idades + idade

        so = input('qual o sistema operacional em seu smartphone, Android ou iOS? ').lower()   #tudo em minúsculo
        print('Ok!')
        if so == 'ios':
            ios += 1  #contador de ios
        else:
            android += 1 # contador de android

        print(f'Obrigado por responder, {cliente}!!\n')
        media_idade = int(soma_idades / entrevistados)
    elif opcao == 2:
        print('')
        print('=' * 40)
        print(f'Média de idade dos entrevistados: {media_idade}')
        print(f'Número de entrevistados: {entrevistados}')
        print(f'Entrevistados que usam Android: {android}')
        print(f'Entrevistados que usam iOS: {ios}')
        print('=' * 40)
        print('')
