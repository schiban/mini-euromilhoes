import random
import sys

custo = 2
opt = ''
num_apostas = 0
chave = [0 for x in range(4)]


# Função Menu Principal
# Esta função permite mostrar o menu com as diferentes opções de escolha para correr o jogo.
def menu_principal():
    print('┌' + 31 * '-' + '┐',
          '\n│', 'Bem-vindo ao MiniEuromilhões!', '│\n' +
          '├' + 31 * '-' + '┤\n' +
          '│ 1 - Realizar Apostas' + 10 * ' ' + '│\n' +
          '│ 2 - Consultar Apostas' + 9 * ' ' + '│\n' +
          '│ 3 - Verificar Chave Sorteada' + 2 * ' ' + '│\n' +
          '│ 4 - Verificar Prémio' + 10 * ' ' + '│\n' +
          '│ 5 - Regras' + 20 * ' ' + '│\n' +
          '│ 6 - Sair' + 22 * ' ' + '│\n' +
          '└' + 31 * '-' + '┘')


# Função Chave Aleatória
# Esta função realiza a randomização de uma chave que irá ser usada como "chave sorteada" no jogo.
def chave_sorteada():
    chavesorteada = []
    random_num = 0
    while len(chavesorteada) < 3:
        random_num = random.randrange(1, 20)
        if random_num not in chavesorteada:
            chavesorteada.append(random_num)
    random_num = random.randrange(1, 5)
    chavesorteada.append(random_num)
    return chavesorteada


chave = chave_sorteada()

# É iniciado o menu principal e de seguida é permitido ao utilizador indicar qual a opção desejada
while opt != 0:
    menu_principal()
    opt = int(input('Qual a opção: '))

# Na opção 1 é pedido ao utilizador para indicar quantas apostas deseja fazer e de seguida pede para as preencher.
    if opt == 1:
        i = 0
        num_apostas = int(input('Quantas apostas deseja fazer: '))
        if 1 <= num_apostas <= 5:
            mMatrix = [[0 for x in range(4)] for y in range(num_apostas)]
            while i < num_apostas:
                j = 0
                print(f"{i + 1}ª Aposta")
                while j < 4:
                    if j == 3:
                        estrela = int(input("▸ Estrela: "))
                        try:
                            if estrela not in range(1, 6):
                                print('Insira um número entre 1 e 5.')
                            else:
                                mMatrix[i][j] = estrela
                                j += 1
                        except ValueError:
                            print("Por favor escreva uma estrela.")
                    else:
                        numero = int(input(f"▸ {j + 1}º Número: "))
                        try:
                            if numero not in range(1, 21) or numero in mMatrix[i]:
                                print('Insira um número entre 1 e 20 ou número já escolhido.')
                            else:
                                mMatrix[i][j] = numero
                                j += 1
                        except ValueError:
                            print("Por favor escreva um número.")
                i += 1
        else:
            input("Número fora do limite permitido. Pressione qualquer tecla para avançar...")

# A opção 2 apresenta no ecrã as apostas feitas pelo utilizador.
    elif opt == 2:
        if num_apostas != 0:
            num = 0
            while num < num_apostas:
                num2 = 0
                print('\nAposta Nº', num + 1,
                      '\n▸', mMatrix[num][0], ",", mMatrix[num][1], ',', mMatrix[num][2], '->', mMatrix[num][3])
                num += 1
            print('\nO total gasto foi de', custo * num_apostas, '€.\n')
        else:
            input("Não fez nenhuma aposta. Pressione qualquer tecla para avançar...")

# Na opção 3 é apresentada a chave sorteada caso tenham sido feitas apostas.
    elif opt == 3:
        if num_apostas == 0:
            input("Não fez nenhuma aposta. Pressione qualquer tecla para avançar...")
        else:
            print('\nChave Sorteada:')
            print('▸', chave[0], ',', chave[1], ',', chave[2], '->', chave[3], '\n')

# A opção 4 faz a verificação se o utilizador teve ou não prémio.
    elif opt == 4:
        d = 0
        if num_apostas == 0:
            input("Não fez nenhuma aposta. Pressione qualquer tecla para avançar...")
        else:
            g = 0
            while g < num_apostas:
                k = 0
                contar_numeros = 0
                while k < 3:
                    h = 0
                    while h < 3:
                        if mMatrix[g][k] == chave[h]:
                            contar_numeros += 1
                        h += 1
                    k += 1
                print("\nAposta nº", g + 1)
                if mMatrix[g][3] == chave[3]:
                    print("Acertou em", contar_numeros, "número/s e na estrela.")
                else:
                    print("Acertou em", contar_numeros, "número/s e errou a estrela.")
                if contar_numeros == 3 and mMatrix[g][3] == chave[3]:
                    print("Parabéns, és o grande vencedor!\n")
                if contar_numeros != 3:
                    d = 1
                g += 1
        if d == 1:
            print("Infelizmente ainda não foi desta... Volta a tentar!\n")


# A opção 5 mostra as regras para correr o programa sem problema.
    elif opt == 5:
        print('\nRegras do MiniEuromilhões:\n')
        print('O jogo é composto pela realização de um máximo de 5 apostas.',
              '\nCada aposta é composta por 3 números (números de 1 a 20) e 1 estrela (1 a 5).',
              '\nCada aposta tem o valor de 2€.',
              '\nEste jogo foi criado pelos alunos João Bandeira e Fábio Oliveira.\n')

    # O programa encerra.
    elif opt == 6:
        print('\nEsperemos que te tenhas divertido!')
        sys.exit()
