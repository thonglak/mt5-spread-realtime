import MT as mt
import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from matplotlib.animation import FuncAnimation
import time
import socket
import math


load_dotenv()


folder_dir = os.getenv('DIR')
login = int(os.getenv('LOGIN'))
pwd = os.getenv('PWD')
server = os.getenv('SERVER')
symbol = os.getenv('SYMBOL')
path = "C:/Program Files/" + folder_dir +"/terminal64.exe"



if not mt.initialize(path=path,login=login, server=server,password=pwd):
    print("Initialize() failed, error code =", mt.last_error())
    quit()
   


class MultiSymbolSpreadMonitor:
    def __init__(self, symbols,broker):
        self.symbols = symbols
        self.broker = broker
        self.fig, self.ax = plt.subplots()
        self.data = {symbol: {'timestamps': [], 'spreads': []} for symbol in symbols}
        

    def update(self, frame):
        for symbol in self.symbols:
            tick = self.broker.symbol_info_tick(symbol)
            if tick:
               
                spread = (tick.ask - tick.bid) / self.broker.symbol_info(symbol).point
                spread = int(round(spread,0))
                print(spread)
                symbol_data = self.data[symbol]
                symbol_data['spreads'].append(spread)
                symbol_data['timestamps'].append(time.strftime('%H:%M:%S'))
                # จำกัดจำนวนข้อมูลที่จะแสดง
                if len(symbol_data['spreads']) > 60:
                    symbol_data['spreads'].pop(0)
                    symbol_data['timestamps'].pop(0)
        self.ax.clear()
        for symbol, symbol_data in self.data.items():
            self.ax.plot(symbol_data['timestamps'], symbol_data['spreads'], label=f'{symbol} Spread')
        plt.xticks(rotation=90)
        plt.subplots_adjust(bottom=0.2)
        plt.title('Real-time Spread ' + folder_dir)
        plt.legend()

    def show(self):
        self.ani = FuncAnimation(self.fig, self.update, interval=1000)
        plt.grid(True)
        plt.show()


monitor = MultiSymbolSpreadMonitor([symbol],mt)
    
def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 6789))  # เปลี่ยน 'server_ip_address' เป็น IP ของ server

    # ส่งข้อความ 'ready' ไปยัง server
    client_socket.sendall('ready'.encode('utf-8'))

    # รอคำสั่ง 'start' จาก server
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message == 'start':
            print("Received start command. Working...")
            monitor.show()
            # เริ่มทำงานบางอย่างที่นี่
            break

if __name__ == "__main__":
    client()