import tkinter as tk
import random

# Função chamada quando o botão é pressionado
def sortear_numeros(count):
    if count > 0:
    # Atualiza o texto da label e agenda a função para ser chamada novamente
    # depois de 1000 milissegundos (1 segundo)
        label_numbers['text'] = count
        window.after(1000, sortear_numeros, count - 1)
    else:
    # Gera uma lista com 6 números aleatórios de 1 a 60
        numbers = random.sample(range(1, 61), 6)
    # Exibe os números sorteados na label
        label_numbers['text'] = 'Números sorteados: {}'.format(numbers)
    # Escolhe uma mensagem aleatória da lista
        message = random.choice(messages)
    # Exibe a mensagem escolhida na label
        label_message['text'] = message

def start_countdown():
    sortear_numeros(10)

# Cria a janela principal
window = tk.Tk()
window.title('Sorteio de números')

# Define o tamanho da janela
window.geometry('600x200')

# Cria uma lista com as mensagens que deseja exibir
messages = [
    'Que a boa sorte te encontre e jamais te abandone!',
    'Você será o próximo milionário!',
    'Tenha fé',
    'Vai com calma e tenha fé. Tudo vai dar certo! Boa sorte!',
    'Não desista!',
    'Sorte é o que acontece quando a preparação encontra a oportunidade.',
    'Nunca se esqueça do seu potencial.',
    'Estou torcendo por você!',
    'Você merece!'
]

# Cria um label para exibir o texto acima do botão
label_text = tk.Label(text='RUMO AO MILHÃO', font=('Arial', 20, 'bold'), fg='black')
label_text.pack(side='top')

# Cria um botão
button = tk.Button(text='Sortear números', font=('Arial', 12, 'bold'), fg='black', bg='white', command=start_countdown)
button.pack(side='top', pady=20)

# Cria uma label para exibir os números sorteados
label_numbers = tk.Label(text='', font=('Arial', 14), fg='black')
label_numbers.pack()

# Cria uma label para exibir a mensagem escolhida aleatoriamente
label_message = tk.Label(text='', font=('Arial', 12, 'bold'), fg='black')
label_message.pack(side='bottom')


# Inicia o loop de eventos da interface gráfica
window.mainloop()
