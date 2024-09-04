import customtkinter
import tkinter as tk

cor1="#4f40a3"
cor2="#dfe8e7"
cor3="#273891"
font_estilo = ('Ivy', 13, 'bold')
font_estilo2 = ('Ivy', 25, 'bold')
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


todos_valores = ''


def valores(event):
    
    global todos_valores

    todos_valores = todos_valores + str(event)
    
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

janela = customtkinter.CTk()
janela.geometry("235x318")
janela.title("Calculadora")


visor_calc = customtkinter.CTkLabel(janela, width=235, height=50, bg_color=cor2, text="")
visor_calc.grid(row=1, column=0)

valor_texto = tk.StringVar()
visor_corpo = customtkinter.CTkLabel(janela, width=235, height=268)
visor_corpo.grid(row=2, column=0)

leitor=customtkinter.CTkLabel(visor_calc, textvariable=valor_texto, width=235, height=50, padx=10, anchor="e", font=font_estilo2, bg_color=cor2, text_color="black")
leitor.place(x=0,y=0)

b1= customtkinter.CTkButton(visor_corpo, command= limpar_tela, text="C", width=117.5, height=53.6, font=font_estilo, border_color="#2980b9", border_width=2)
b1.place(x=0, y=0)
b2= customtkinter.CTkButton(visor_corpo, command= lambda: valores('%'), text="%", width=58, height=53.6, font=font_estilo, border_color="#2980b9", border_width=2)
b2.place(x=117.5, y=0)
b3= customtkinter.CTkButton(visor_corpo, command= lambda: valores('/'),  text="/", width=58, height=53.6, fg_color=cor3, font=font_estilo, border_color="#2980b9", border_width=2)
b3.place(x=176, y=0)

b4= customtkinter.CTkButton(visor_corpo, command= lambda: valores('7'),  text="7", width=58, height=53.6, font=font_estilo, border_color="#2980b9", border_width=2)
b4.place(x=1, y=53.5)
b5= customtkinter.CTkButton(visor_corpo, command= lambda: valores('8'), text="8", width=58, height=53.6, font=font_estilo, border_color="#2980b9", border_width=2)
b5.place(x=59, y=53.5)
b6= customtkinter.CTkButton(visor_corpo, command= lambda: valores('9'), text="9", width=58, height=53.6, font=font_estilo, border_color="#2980b9", border_width=2)
b6.place(x=117.5, y=53.5)
bx= customtkinter.CTkButton(visor_corpo, command= lambda: valores('*'), text="*", width=58, height=53.6, fg_color=cor3, font=font_estilo, border_color="#2980b9", border_width=2)
bx.place(x=176, y=53.5)

b7= customtkinter.CTkButton(visor_corpo, command= lambda: valores('4'), text="4", width=58, height=53.6, font=font_estilo, border_color="#2980b9", border_width=2)
b7.place(x=1, y=107)
b8= customtkinter.CTkButton(visor_corpo, command= lambda: valores('5'), text="5", width=58, height=53.6, font=font_estilo, border_color="#2980b9", border_width=2)
b8.place(x=59, y=107)
b9= customtkinter.CTkButton(visor_corpo, command= lambda: valores('6'), text="6", width=58, height=53.6, font=font_estilo, border_color="#2980b9", border_width=2)
b9.place(x=117.5, y=107)
by= customtkinter.CTkButton(visor_corpo, command= lambda: valores('-'), text="-", width=58, height=53.6, fg_color=cor3, font=font_estilo, border_color="#2980b9", border_width=2)
by.place(x=176, y=107)

b10= customtkinter.CTkButton(visor_corpo, command= lambda: valores('1'), text="1", width=58, height=53.6, font=font_estilo, border_color="#2980b9", border_width=2)
b10.place(x=1, y=160.5)
b11= customtkinter.CTkButton(visor_corpo, command= lambda: valores('2'), text="2", width=58, height=53.6, font=font_estilo, border_color="#2980b9", border_width=2)
b11.place(x=59, y=160.5)
b11= customtkinter.CTkButton(visor_corpo, command= lambda: valores('3'), text="3", width=58, height=53.6, font=font_estilo, border_color="#2980b9", border_width=2)
b11.place(x=117.5, y=160.5)
bz= customtkinter.CTkButton(visor_corpo, command= lambda: valores('+'), text="+", width=58, height=53.6, fg_color=cor3, font=font_estilo, border_color="#2980b9", border_width=2)
bz.place(x=176, y=160.5)

bl= customtkinter.CTkButton(visor_corpo, command= lambda: valores('0'), text="0", width=117.5, height=53.6, font=font_estilo, border_color="#2980b9", border_width=2)
bl.place(x=0, y=214)
bl2= customtkinter.CTkButton(visor_corpo, command= lambda: valores('.'), text=".", width=58, height=53.6, font=font_estilo, border_color="#2980b9", border_width=2)
bl2.place(x=117.5, y=214)
bl3= customtkinter.CTkButton(visor_corpo, command= calcular, text="=", width=58, height=53.6, fg_color=cor3, font=font_estilo, border_color="#2980b9", border_width=2)
bl3.place(x=176, y=214)



janela.mainloop()