from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from HeaterWrapper import HeaterWrapper

N = 100
sensor_data = []
sensor_time = []

data_max = []
data_min = []
def init():
    fig = plt.figure(figsize=(14, 7))
    ax = fig.add_subplot(1, 1, 1)


    def func_data_max():
        global data_max
        my_max = int(spin_max.get())
        HeaterWrapper().heater.setMax(my_max)
        data_max = [my_max] * len(sensor_data)


    def func_data_min():
        global data_min
        my_min = int(spin_min.get())
        HeaterWrapper().heater.setMin(my_min)
        data_min = [my_min] * len(sensor_data)


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

        func_data_max()
        func_data_min()
        if data_min[0] > temperature:
            HeaterWrapper().heater.turnOn()
        elif data_max[0] < temperature:
            HeaterWrapper().heater.turnOff()
        ax.clear()
        plt.title("Данные датчика")
        plt.xlabel("Время")
        plt.ylabel("Показания датчика")

        ax.plot(sensor_time, data_max, linestyle="--", color="r", linewidth=1)
        ax.plot(sensor_time, data_min, linestyle="--", color="g", linewidth=1)
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
    spin_min = Spinbox(window, from_=-55, to=125, width=5, textvariable=var1)
    spin_max = Spinbox(window, from_=-55, to=125, width=5, textvariable=var2)
    spin_max.grid(column=1, row=1)
    spin_min.grid(column=2, row=1)
    window.mainloop()
