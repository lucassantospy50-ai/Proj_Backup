# Projeto de Backup 💾 (⚠EM ANDAMENTO⚠)

## índice 🏹
  - <a href="#contextualização-do-projeto">Contextualização do Projeto</a>
  - <a href="#links-para-me-contatar-">Sobre Mim</a>
  - <a href="#bibliotecas-utiluzadas">Bibliotecas Utilizadas</a>

## Contextualização do Projeto
Nesse projeto eu quis treinar meus conhecimentos em manipulação de arquivos no computador e, ao mesmo tempo, resolver um problema comum: fazer backups de segurança. Muitas vezes a gente esquece de fazer backup ou acaba não fazendo por ser demorado, então pensei em criar um projeto em Python que automatiza esse processo.

A ideia é simples: o usuário escolhe as pastas e arquivos que deseja incluir no backup e depois define o local onde o backup será salvo. A partir daí, nas próximas execuções, o computador faz tudo automaticamente, usando os caminhos que já ficaram salvos. Se, no futuro, você adicionar novos arquivos ou mover algum arquivo/pasta de lugar, basta atualizar a lista de itens que devem ser salvos. Caso queira começar um backup totalmente novo, com outros caminhos, é só selecionar essa opção no início do programa.

Assim, o processo de backup fica mais rápido, automático e menos sujeito ao esquecimento.

## Bibliotecas utiluzadas
```python
import os
from tkinter import messagebox, filedialog
from pathlib import Path
import shutil
import zipfile
import tkinter as tk
import sys
```
