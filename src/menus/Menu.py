def continuar_sistema(submenu):
    while True:
        continuar = int(input("Deseja realizar nova operação? "
                              "\n1 - Sim"
                              "\n2 - Não"))
        if continuar == 1:
            submenu
            break
        elif continuar == 2:
            sair_do_programa()
            break
        else:
            print("\033[31mOpção inexistente. Por favor, digitar opção válida (1 ou 2).\033[m")
            continue
        
def sair_do_programa():
    """
      Encerra o programa.

      :return: Nenhum valor é retornado. A função imprime uma mensagem de agradecimento e finaliza o programa.
    """
    print("Obrigado por usar nosso serviço. Até a próxima! :)")
    exit()
