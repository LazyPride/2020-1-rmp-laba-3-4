from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from HeaterWrapper import HeaterWrapper

N = 100
sensor_data = []
sensor_time = []

def init():
    fig = plt.figure(figsize=(14, 7))
    ax = fig.add_subplot(1, 1, 1)
    
    def send_max_to_server():
        my_max = int(spin_max.get())
        HeaterWrapper().heater.setMax(my_max)

    def send_min_to_server():
        my_min = int(spin_min.get())
        HeaterWrapper().heater.setMin(my_min)

    def animate(self):
        # Считывание показания датчика
        temperature = HeaterWrapper().heater.now
        time_data = datetime.strftime(datetime.now(), "%H:%M:%S")
        if len(sensor_data) < N:
            sensor_data.append(temperature)
            sensor_time.append(time_data)
        elif len(sensor_data) == N:
            sensor_data.append(temperature)
            sensor_data.pop(0)
            sensor_time.append(time_data)
            sensor_time.pop(0)

        server_min = HeaterWrapper().heater.min
        server_max = HeaterWrapper().heater.max

        var1.set(server_min)
        var2.set(server_max)
        
        ax.clear()
        plt.title("Данные датчика")
        plt.xlabel("Время")
        plt.ylabel("Показания датчика")

        ax.plot(sensor_time, sensor_data, linestyle="solid", linewidth=2)
        plt.title("Данные датчика")
        plt.xlabel("Время")
        plt.ylabel("Показания датчика")
        plt.grid()
        plt.xticks(fontsize=6)
        plt.yticks(fontsize=8)
        plt.gcf().autofmt_xdate()


    window = Tk()
    window.title("Бригада №1")
    window.geometry('600x600')
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().place(x=10, y=10)
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    var1 = StringVar(window)
    var2 = StringVar(window)
    var1.set(HeaterWrapper().heater.min)
    var2.set(HeaterWrapper().heater.max)
    spin_min = Spinbox(window, from_=-55, to=125, width=5, textvariable=var1, command=send_min_to_server)
    spin_max = Spinbox(window, from_=-55, to=125, width=5, textvariable=var2, command=send_max_to_server)
    spin_max.grid(column=1, row=1)
    spin_min.grid(column=2, row=1)
    window.mainloop()
