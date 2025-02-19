import pyautogui
import time
import pandas


#ABERTURA DO SISTEMA
pyautogui.PAUSE=1
url="https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)
pyautogui.write(url)
pyautogui.press("enter")


#LOGIN NO SISTEMA
time.sleep(3)
pyautogui.click(x=592, y=410)
pyautogui.write("emailqualquer@gmail.com")
pyautogui.press("Tab")
pyautogui.write("12345")
pyautogui.press("enter")


#IMPORTAÇÃO DA BASE DE DADOS
tabela= pandas.read_csv("produtos.csv")


#CADASTRO DE PRODUTOS NO SISTEMA/LOOP PARA CADASTRAR TODA A BASE
time.sleep(2)

for linha in tabela.index:

    #Codigo
    pyautogui.click(x=627, y=292)
    codigo= tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("Tab")

    #Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("Tab")

    #Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("Tab")

    #Categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("Tab")

    #Preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("Tab")

    #Custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("Tab")

    #Obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("Tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)


#FALTA FAZER:

# agendamento do sistema (https://www.youtube.com/watch?v=SxEjHAlCqmo&t=0s)
# selenium para rodar em segundo plano (roda só em sites)