import os

def listar_arquivos_para_txt(caminho_diretorio, nome_arquivo_saida="lista_arquivos.txt"):
    try:
        if not os.path.isdir(caminho_diretorio):
            print(f"Error: O caminho '{caminho_diretorio}' não é um diretório válido.")
            return
        
        itens = os.listdir(caminho_diretorio)
        arquivos = [item for item in itens if os.path.isfile(os.path.join(caminho_diretorio, item))]
        
        with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
            for nome in arquivos:
                arquivo_saida.write(nome + '\n')
                
        print(f"Sucesso! A lista foi gerada em '{os.path.abspath(nome_arquivo_saida)}'.")
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        
caminho = input("Digite o caminho do diretório para listar os arquivos: ")
listar_arquivos_para_txt(caminho)