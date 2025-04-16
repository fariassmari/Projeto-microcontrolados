import tkinter as tk
import serial
import math

porta = "COM3"
velocidade = 9600
portaSerial = serial.Serial(porta, velocidade)
#Cria um objeto Serial para comunicação com a porta serial especificada

def read_serial(canvas, serial_port): 
    if serial_port.in_waiting > 0:
        line = serial_port.readline().decode('utf-8').rstrip()
        angles = line.split("|")
        x_angle, y_angle = map(float, [angles[0].split(":")[1].strip(), angles[1].split(":")[1].strip()])

        draw_level(canvas, x_angle, y_angle, center_x=100, center_y=100, radius=80)
        #Exibe os ângulos na interface gráfica

    root.after(100, read_serial, canvas, serial_port)
    #Função que lê continuamente os dados da porta serial
    
def draw_level(canvas, x_angle, y_angle, center_x, center_y, radius):
    canvas.delete("all")

    x_rad, y_rad = map(math.radians, [x_angle, y_angle])
    x_end = center_x + radius * math.sin(x_rad)
    y_end = center_y - radius * math.cos(y_rad)
    #Função que desenha o nivel digital na tela

    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline="black")
    #Desenha círculo
    
    canvas.create_line(center_x, center_y, x_end, y_end, width=2, fill="red")
    #Desenha linha dentro do círculo
    
def on_closing():
    portaSerial.close()
    root.destroy()
    #Função que é chamada quando a janela é fechada, fecha a porta serial e destroi a janela Tkinter

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Nivelador de Obras Digital")

    canvas = tk.Canvas(root, width=200, height=200, bg="white")
    canvas.pack()
    #Cria o canvas

    root.protocol("WM_DELETE_WINDOW", on_closing)
    #Associa a função on closing quando a janela é fechada 

    read_serial(canvas, portaSerial)
    #Faz a leitura dos dados da porta serial e atualiza a interface

    root.mainloop()
