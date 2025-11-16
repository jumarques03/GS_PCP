from logica_da_aplicacao import cadastrar_perfil, criar_carreiras_padrao, criar_recomendador

def menu():
    perfil = None
    carreiras = criar_carreiras_padrao()
    recomendador = criar_recomendador()

    while True:
        print("\n===== FUTURE SKILLS: SEU RECOMENDADOR DE CARREIRA PERSONALIZADO =====")
        print("1. Cadastrar Perfil")
        print("2. Exibir Perfil")
        print("3. Listar Carreiras Disponíveis para Recomendação")
        print("4. Recomendar Carreira")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            perfil = cadastrar_perfil()
            print("\nPerfil cadastrado com sucesso!")

        elif opcao == "2":
            if perfil:
                print(perfil.exibir_perfil())
            else:
                print("\nNenhum perfil cadastrado ainda!")

        elif opcao == "3":
            print("\n=== Carreiras disponíveis para recomendação ===")
            for c in carreiras:
                print(f"- {c.nome}")
            print(f"\nTotal: {len(carreiras)} carreiras")

        elif opcao == "4":
            if not perfil:
                print("\nCadastre um perfil primeiro!")
                continue

            melhor = recomendador.recomendar(perfil)

            print("\n===== Carreira Recomendada =====")
            print(f"Sugestão ideal para você: **{melhor.nome}**")
            
            print("\n--- Explicação da Recomendação ---")
            explicacao = recomendador.explicar_recomendacao(perfil, melhor)
            print(explicacao)

        elif opcao == "5":
            print("\nObrigada por usar o Future Skills! Esperamos ter ajudado!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()