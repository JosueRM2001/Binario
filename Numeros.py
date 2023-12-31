import openai
#Ingrsar la clave del OpenAi
openai.api_key = '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'
# Ingresar un número
user_input = input("Ingresa un número: ")
# Convertir el numero ingresado en binario
binary_number = bin(int(user_input))[2:]
#Mensaje que saldra en pantalla
user_message = {"role": "user", "content": f"{user_input} en binario es {binary_number}"}
# Los mensajes del sistema, del usuario y parámetros
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        user_message
    ],
    temperature=0.1,
    max_tokens=100
)
print(response)
