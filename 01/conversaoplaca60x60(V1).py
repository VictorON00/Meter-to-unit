def principal():
    opcao = int(input('''\nQUAL CONVERSAO DESEJA DESCOBRIR?
        [1] M^2 para Quantidade
        [2] Quantidade para M^2
        [3] Sair\n'''))

    if opcao == 1:
        m2_para_quantidade()
    elif opcao == 2:
        quantidade_para_m2()
    elif opcao == 3:
        sair()
    else:
        print("Digite apenas uma das alternativas!")
        return principal()

def m2_para_quantidade():
    m2 = float(input("Metros Quadrados: \n"))
    m2_placa = 0.36
    calc = m2 / m2_placa
    calc = math.ceil(calc)  # Arredonda para um valor inteiro acima com math
    print('X'*40)
    print(f'O RESULTADO EM QUANTIDADE É: {calc} placas')
    print('X'*40)

def quantidade_para_m2():
    qnt = int(input("Quantidade de placas: \n"))
    m2_placa = 0.36
    calc = qnt * m2_placa
    calc = round(calc, 1)  # Arredonda valor
    print('X'*40)
    print(f'O RESULTADO EM M^2 É: {calc} metros quadrados')
    print('X'*40)
    
def sair():
    sn = str(input("\nDeseja sair? [s/n] "))
    if sn.lower() == 's':
        global loop
        loop = False
    elif sn.lower() == 'n':
        pass
    else:
        print('Não entendi!')

import math
loop = True
while loop:
    principal()


