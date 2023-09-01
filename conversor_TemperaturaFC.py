from tkinter import *


def converter_temperatura():
    temperatura = float(entry_temperatura.get())
    if var.get() == 1:
        resultado = (temperatura * 9/5) + 32
        label_resultado.config(text=f"Temperatura em Fahrenheit: {resultado}")
    else:
        resultado = (temperatura - 32) * 5/9
        label_resultado.config(text=f"Temperatura em Celsius: {resultado}")

janela = Tk()
janela.title("Conversor de Temperatura")
janela.geometry("300x300")
janela.resizable(False, False)


label_temperatura = Label(janela, text="Temperatura:")
label_temperatura.pack(pady=10)

entry_temperatura = Entry(janela, width=20)
entry_temperatura.pack()

var = IntVar()

radio_fahrenheit = Radiobutton(janela, text="Fahrenheit", variable=var, value=1)
radio_fahrenheit.pack()

radio_celsius = Radiobutton(janela, text="Celsius", variable=var, value=2)
radio_celsius.pack()

btn_converter = Button(janela, text="Converter", command=converter_temperatura)
btn_converter.pack(pady=10)

label_resultado = Label(janela, text="")
label_resultado.pack(pady=10)

janela.mainloop()