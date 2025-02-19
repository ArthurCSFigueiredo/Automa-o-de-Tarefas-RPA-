# Automacao de Cadastro de Produtos

📌 **Sobre o Projeto**

Este projeto realiza a automação do cadastro de produtos em um sistema web utilizando Python e a biblioteca PyAutoGUI. O código abre o navegador, faz login no sistema e insere automaticamente os dados de um arquivo CSV.


🚀 **Tecnologias Utilizadas**

**•Python**

**•PyAutoGUI** (Automação de interface gráfica)

**•Pandas** (Manipulação de dados)

**•Time** (Controle de tempo de execução)


🔧 **Como Funciona**

**Abertura do Sistema:** O código abre o navegador, acessa a URL do sistema e aguarda o carregamento.

**Login Automático:** Insere o e-mail e senha cadastrados e realiza o login.
![Login fictício (Não incluso no projeto)](imagens/pj_rpa.JPG)


**Importação da Base de Dados:** Lê um arquivo .CSV contendo os produtos a serem cadastrados.

**Cadastro Automático:** Percorre os dados do CSV e preenche os campos do sistema com as informações de cada produto até o fim o da base de dados.
![Tela de cadastramento (Não inclusa)](imagens/pj_rpa2.JPG)

📢 **Observações**
Foi utilizado para pegar a posição do cursor em tela, uma função do PyAutoGui chamada **pyautogui.position()** juntamente com um **time.sleep(8)** para posicionar o cursor no local correto.
![Código para pegar posição](imagens/pj_rpa3.JPG)
