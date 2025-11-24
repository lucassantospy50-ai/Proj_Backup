#Projeto Backup
import os
from tkinter import messagebox, filedialog
from pathlib import Path
import shutil
import zipfile
import tkinter as tk
import sys

root = tk.Tk()
root.withdraw()

#Deseja fazer o backup
fazer_backup = messagebox.askyesno('Backup Automáico', 'Opa! Deu a hora do seu backup automático. Quer fazer agora?')
# padronizar para sempre começar na home
home = os.path.expanduser("~")

#Pegar as pastas que o usuário deseja compactar
if fazer_backup:
    lista_diretorios = []
    confirmar_pastas = messagebox.askyesno('Criando Backup', 'Deseja fazer backup de pastas?')
    if confirmar_pastas:
        while True:
            diretorio = filedialog.askdirectory(title= 'Selecione as pastas que você deseja salvar no Backup', initialdir= home)
            #fechar o programa caso a pessoa clique no X
            if not diretorio:
                root.destroy()
                sys.exit()
            if diretorio not in lista_diretorios:
                lista_diretorios.append(diretorio)
            parar_pasta = messagebox.askyesno('Gerando os Caminhos', 'Precisa fazer backup em mais uma pastas?')
            if not parar_pasta:
                break

#Pegar os arquivos que ele deseja compactar
    lista_arquivos = []
    confirmar_arquivos = messagebox.askyesno('Criando Backup', 'Deseja fazer backup de arquivos?')
    if confirmar_arquivos:
        while True:
            arquivo = filedialog.askopenfile(title= 'Selecione os arquivos que você deseja salvar no Backup', initialdir= home)
            if not arquivo:
                root.destroy()
                sys.exit()
            if arquivo not in lista_arquivos:
                lista_arquivos.append(arquivo.name)
            parar_arquvivo = messagebox.askyesno('Gerando os Caminhos', 'Precisa fazer backup em mais um arquivo?')
            if not parar_arquvivo:
                break

#Pegar o local onde ele deseja salvar o backup
    while True:
        local_backup = filedialog.askdirectory(title='Selecione onde você deseja salvar o backup', initialdir= home)
        if local_backup:
            confirmar_backup = messagebox.askyesno('Salvando Caminho', f'Deseja salvar o backup no local {local_backup}?')
            if confirmar_backup:
                messagebox.showinfo('Caminho Salvo', f'Local de Backup salvo em {local_backup}')
                break
        else:
            root.destroy()
            sys.exit()


    if len(lista_arquivos) + len(lista_diretorios) != 0:
#Fazendo o Backup de pastas com tratamento de erro
        pasta_backup = Path(local_backup) / 'Backup'
        pasta_backup.mkdir(exist_ok=True)

        lista_erros_diretorios = []
        for diretorio in lista_diretorios:
            try:
                nome_diretorio = Path(diretorio).name
                novo_caminho = Path(local_backup / Path('Backup')) / Path(nome_diretorio)
                shutil.copytree(diretorio, novo_caminho)
            except (FileNotFoundError, FileExistsError, PermissionError, OSError) as e:
                lista_erros_diretorios.append(
                    {'Pasta': diretorio, 'Error': type(e).__name__, 'Mensagem': str(e)}
                )
            except Exception as e:
                lista_erros_diretorios.append(
                    {'Pasta': diretorio, 'Error': type(e).__name__, 'Mensagem': str(e)}
                )

    #Fazendo o Backup de arquivos com tratamento de erro
        lista_erros_arquivos = []
        for arquivo in lista_arquivos:
            try:
                nome_arquivo = Path(arquivo).name
                novo_caminho = Path(local_backup / Path('Backup')) / Path(nome_arquivo)
                shutil.copy2(arquivo, novo_caminho)
            except (FileNotFoundError, FileExistsError, PermissionError, OSError) as e:
                lista_erros_arquivos.append(
                    {'Arquivo': arquivo, 'Error': type(e).__name__, 'Mensagem': str(e)}
                )
            except Exception as e:
                lista_erros_arquivos.append(
                    {'Arquivo': arquivo, 'Error': type(e).__name__, 'Mensagem': str(e)}
                )
    else:
        messagebox.showinfo('Backup', 'Não foi selecionado nenhum arquivo/pasta para o backup')

    
    if len(lista_erros_arquivos) != 0:
        for error in lista_erros_arquivos:
            messagebox.showerror('Erro no Backup', f'O arquivo localizado no caminho {error['Arquivo']} não foi possível colocá-lo no backup, pois ele deu o erro {error['Error']}: {error['Mensagem']}')
    
    
    if len(lista_erros_diretorios) != 0:
        for error in lista_erros_diretorios:
            messagebox.showerror('Erro no Backup', f'A pasta localizada no caminho {error['Pasta']} não foi possível colocá-la no backup, pois ela deu o erro {error['Error']}: {error['Mensagem']}')
    
    
root.destroy()