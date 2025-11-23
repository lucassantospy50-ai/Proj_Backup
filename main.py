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
            parar_pasta = messagebox.askyesno('Gerando os Caminhos', 'Precisa fazer backup em mais um diretório?')
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

#Fazer o Backup dos arquivos 
    try:
        if Path(local_backup / Path('Backup')).exists():
            for arquivo in lista_arquivos:
                shutil.copy2(arquivo, Path(local_backup / Path('Backup')))
        else:
            Path(local_backup / Path('Backup')).mkdir()
            for arquivo in lista_arquivos:
                shutil.copy2(arquivo, Path(local_backup / Path('Backup')))
    except:
        messagebox.showerror('Backup Automáico', 'Ocorreu um erro no Backup')

#Fazer o Backup dos diretórios 
    try:
        if Path(local_backup / Path('Backup')).exists():
            for diretorio in lista_diretorios:
                nome_diretorio = Path(diretorio).name
                novo_caminho = Path(local_backup / Path('Backup')) / Path(nome_diretorio)
                shutil.copytree(diretorio, novo_caminho)
        else:
            Path(local_backup / Path('Backup')).mkdir()
            for diretorio in lista_diretorios:
                nome_diretorio = Path(diretorio).name
                novo_caminho = Path(local_backup / Path('Backup')) / Path(nome_diretorio)
                shutil.copytree(diretorio, novo_caminho)
    except:
        messagebox.showerror('Backup Automáico', 'Ocorreu um erro no Backup')

root.destroy()