import gspread
from google.oauth2.service_account import Credentials
import pyautogui 
import time
import webbrowser
import pandas as pd
import pyperclip

link= "https://docs.google.com/spreadsheets/d/1O6hD6aKN4aRBHYbNroE12Urs99_JKnq6wuTbh_2lXis/edit?gid=0#gid=0"
webbrowser.open(link)
time.sleep(9)
pyautogui.hotkey('Alt','tab')
time.sleep(4)

CAMINHO_CREDENCIAL = 'planilha.json'
SCOPOES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
credenciais = Credentials.from_service_account_file(CAMINHO_CREDENCIAL, scopes= SCOPOES)
cliente = gspread.authorize(credenciais)


planilha = cliente.open_by_key("1O6hD6aKN4aRBHYbNroE12Urs99_JKnq6wuTbh_2lXis")
aba = planilha.sheet1

valores = aba.get_all_values()
df = pd.DataFrame(valores[1:], columns= valores[0])

print("Colunas encontradas:")
print(df.columns)

print("\nPrimeiras linhas da planilha")
print(df['Presença'].unique())

print("\nVisualizando os dados Brutos:")
print(df)

#Funcionarios da Minha Empresa

mais_faltoso = df[df['Presença'] == 'Faltas']['Funcionarios']
mais_faltoso = mais_faltoso.value_counts().idxmax()
print(f'O funcionario mais faltoso é:  {mais_faltoso}')

time.sleep(2)

mais_presente  = df[df['Presença'] == 'Presente']['Funcionarios']
funcionario_mais_presente = mais_presente.value_counts().idxmax().strip()
print(f'O funcionario com menos falta é:   {funcionario_mais_presente}')

df['Presença']= df['Presença'].str.strip().str.capitalize()

#Mensagem Por Email

time.sleep(2)
print("Eviar Mensagem de E-mail Para:", mais_faltoso)
time.sleep(3)
print("Enviando...")
time.sleep(5)
link= "https://mail.google.com/mail/u/0/?hl=pt_BR#inbox?compose=new"
webbrowser.open(link)
time.sleep(2)
email_mais_faltoso = df[df['Funcionarios'] == mais_faltoso]['Email'].values[0]
time.sleep(5)
pyautogui.write(email_mais_faltoso)
pyautogui.hotkey('enter')
pyautogui.hotkey('tab')
time.sleep(2)
pyautogui.write('Mensagem de Falta')
pyautogui.hotkey('tab')
time.sleep(6)
texto = "Você está com um percentual de Presença abaixo do padrão da empresa, atente-se a uma melhora."
pyperclip.copy(texto)
pyautogui.hotkey('ctrl','v')
time.sleep(8)
pyautogui.hotkey('Ctrl','enter')
print("Mensagem enviada!.")
time.sleep(2)
pyautogui.hotkey('ctrl','w')

pyautogui.hotkey('Alt','tab')
time.sleep(5)




print("Eviar Mensagem de E-mail Para:", funcionario_mais_presente)
time.sleep(4)
print("Enviando...")
time.sleep(5)
link= "https://mail.google.com/mail/u/0/?hl=pt_BR#inbox?compose=new"
webbrowser.open(link)
time.sleep(5)
email_mais_presente = df[df['Funcionarios'].str.strip() == funcionario_mais_presente]['Email'].values[0]
time.sleep(3)
pyautogui.write(email_mais_presente)
pyautogui.hotkey('enter')
pyautogui.hotkey('tab')
time.sleep(2)
pyautogui.write('Mensagem de Elogio')
pyautogui.hotkey('tab')
time.sleep(6)
texto = "Você foi um exemplo esse mês para nossa empresa, parabéns. você ganhou direito dia de (folga Bônus)."
pyperclip.copy(texto)
pyautogui.hotkey('ctrl','v')
time.sleep(8)
pyautogui.hotkey('Ctrl','enter')
pyautogui.hotkey('Alt','tab')

print("Mensagem enviada!")


