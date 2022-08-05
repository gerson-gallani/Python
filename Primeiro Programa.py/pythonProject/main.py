import animacao
from time import sleep
#testa se foi execultado, evita sobrescrever
confi_mae = 0
confi_ram = 0
confi_process = 0
confi_video = 0
verifica_componentes = 0

print('\n')
print(10*'=','\033[1;36mPROGRAMA QUE AINDA NÃO SEI O NOME\033[m',10*'=')

'''Chama a classe Senha e sua Função'''
usuSenha = int(input('Digite a Senha Numerica \n'))
senha = animacao.Senha(usuSenha)
senha.Comparador()
'''Aqui chama a classe e sua função anima'''
efeito = animacao.anima()
efeito.carregando()
'''Iniciando as funcionalidades'''
print(10*'=','BEM VINDO!',10*'=')
#menu principal
print(10*'=','Menu Princípal',10*'=')
print('''\033[1;31m[1]\033[m______Novo cadastro
\033[1;31m[2]\033[m______Corrigir Cadastro
\033[1;31m[3]\033[m______Salvar Cadastro
\033[1;31m[4]\033[m______Sair\n''')
#Menu principal

while True:
    if verifica_componentes == 0:
        opcao = int(input('Digite sua opção: '))
    if opcao == 1:

        while True:
            print(10 * '=', 'Escolha Qual Componente Cadastra:', 10 * '=')

            print('''\033[1;31m[1]\033[0;94m______Placa Mãe\033[m
\033[1;31m[2]\033[0;94m______Memória Ram\033[m
\033[1;31m[3]\033[0:94m______Processador\033[m
\033[1;31m[4]\033[0:94m______Placa de Video\033[m
\033[1;31m[0]\033[0:94m______Voltar\033[m
\033[mContinua...''')

            opcaoSub = int(input('Digite sua opção: '))

            if opcaoSub == 1:
                #evita sobrescrever
                confi_mae += 1

                ImprMae = animacao.ImputMae()
                CadMae = animacao.PlacaMae(ImprMae.nome,ImprMae.valor)

            elif opcaoSub == 2:
                #evita sobrescrever
                confi_ram += 1
                ImpRam = animacao.ImputarRam()
                CadRam = animacao.MemoriaRam(ImpRam.nome,ImpRam.valor,ImpRam.frequencia,ImpRam.capacidade)


            elif opcaoSub == 3:
                #evita sobrescrever
                confi_process += 1
                ImpProcessador = animacao.ImputarProcess()
                CadProcessador = animacao.Processador(ImpProcessador.nome,ImpProcessador.valor,ImpProcessador.frequencia
                                                      ,ImpProcessador.nucleos,ImpProcessador.treds)


            elif opcaoSub == 4:
                #evita sobrescrever
                confi_video
                ImpVideo = animacao.ImputarVideo()
                CadVideo = animacao.PlacaVideo(ImpVideo.nome,ImpVideo.valor,ImpVideo.vram)

            elif opcaoSub == 0:
                print('Voltando...')
                verifica_componentes = 0
                sleep(0.5)
                print('''\033[1;31m[1]\033[m______Novo cadastro
\033[1;31m[2]\033[m______Corrigir Cadastro
\033[1;31m[3]\033[m______Salvar Cadastro
\033[1;31m[4]\033[m______Sair''')
                break



    elif opcao == 2:
        #Corrigir Cadastro
        print('Anida n está feito')
        break
    elif opcao == 3:

        #Salvar Cadastro
        with open('python.txt','a') as arquivo:

            arquivo.write(str(CadMae))

        break

    elif opcao == 4:
            if confi_mae and confi_ram and confi_process and confi_video == 1:
                print('Tem certeza que quer sair?')
                s = input('Digite S/N  ').upper().strip()
                if s == 'S':
                    print('Encerrando...')
                    sleep(1)
                    break
                else:
                    print('Voltando...')
                    sleep(1)
            elif confi_mae != 1:
                print('Falto Cadastra a Placa Mãe.')
                verifica_componentes = 1
                opcao =1

            elif confi_ram != 1:
                print('Falto Cadastra as Memória Ram')
                verifica_componentes = 2
                opcao = 1

            elif confi_process != 1:
                print('Falto Cadastra o Processador')
                verifica_componentes = 3
                opcao = 1

            elif confi_video !=1:
                print('Falto Cadastra a Placa de Video')
                verifica_componentes = 4
                opcao = 1


    else:
        print('Opção invalida Tente novamente')
        opcao = int(input('Digite novamente sua opção: '))

#Mostrando o resultado
carregaAni = animacao.Carregando().carregandoAnima()
print(CadMae)










'''carregarani = animacao.Carregando()
carregarani.carregandoAnima()'''





