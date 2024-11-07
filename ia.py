import os
from groq import Groq


os.environ["GROQ_API_KEY"] = "Chave API"

client = Groq (
    api_key=os.environ.get("GROQ_API_KEY"),
)


messages=[]

while True:
    usuario = input ("Digite uma mensagem ou 'sair' para encerrar: ")

    if usuario.lower() == 'sair':
        print("Conversa encerrada.")
        break

    
    messages.append({"role": "user", "content": usuario})

chat_completion = client.chat.completions.create(
    messages=messages,
    model="llama-3.1-70b-versatile",
)

resposta = chat_completion.choices[0].message.content
print("Resposta: ", resposta)


messages.append({"role": "assistant", "content": resposta})
