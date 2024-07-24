import tkinter as tk
import socket
import time
import random
from threading import Thread

# Define 'client_socket' at the top level so it's accessible throughout




class App:
    def __init__(self, root):
        self.root = root
        self.running = False  # Control flag
        self.client_socket = None
        self.x = 20
        self.y = 40 + (0*60)
        self.font = ("Helvetica", 16)

        self.bg_green= "#2ea509"
        self.bg_red= "#df3079"
        self.bg_blue= "#2e95d3"
        self.bg4= "#00FF00"

        # Create the Connect button
        self.connect_button = tk.Button(root, text="Connect", command=self.on_connect_click,width=11,heigh=2,font=self.font,fg="white", bg=self.bg_green)
        self.connect_button.place(x=self.x,y=self.y)

        self.x = 180
        self.y = 40 + (0*60)
        # Create the Start button
        self.open_button = tk.Button(root, text="Start", command=self.on_start_click,width=11,heigh=2,font=self.font,fg="white", bg=self.bg_green)
        self.open_button.place(x=self.x,y=self.y)

        self.x = 20
        self.y = 60 + (1*70) 

        # Create the Buy button
        self.buy_button = tk.Button(root, text="Buy", command=self.on_buy_click,width=11,heigh=2,font=self.font,fg="white", bg=self.bg_green)
        self.buy_button.place(x=self.x,y=self.y)


        self.x = 180
        self.y = 60 + (1*70)
        # Create the Close button
        self.sell_button = tk.Button(root, text="Sell", command=self.on_sell_click,width=11,heigh=2,font=self.font,fg="white", bg=self.bg_red)
        self.sell_button.place(x=self.x,y=self.y)



        self.x = 20
        self.y = 60 + (2*70)
        # Create the Open button
        self.close_profit_button = tk.Button(root, text="Close Profit", command=self.on_close_profit_click,width=11,heigh=2,font=self.font,fg="white", bg=self.bg_blue)
        self.close_profit_button.place(x=self.x,y=self.y)


        self.x = 180
        self.y = 60 + (2*70)

        # Create the Close button
        self.close_button = tk.Button(root, text="Close All", command=self.on_close_click,width=11,heigh=2,font=self.font,fg="white", bg=self.bg_blue)
        self.close_button.place(x=self.x,y=self.y)



        self.x = 20
        self.y = 60 + (3*70)
        # Create the Open button
        self.run_button = tk.Button(root, text="Run", command=self.start,width=11,heigh=2,font=self.font,fg="white", bg=self.bg_blue)
        #self.run_button.place(x=self.x,y=self.y)


        self.x = 180
        self.y = 60 + (3*70)

        # Create the Close button
        self.stop_button = tk.Button(root, text="Stop", command=self.stop,width=11,heigh=2,font=self.font,fg="white", bg=self.bg_blue)
        #self.stop_button.place(x=self.x,y=self.y)
        
        
        root.protocol("WM_DELETE_WINDOW", self.on_close)


    def repetitive_task(self):
        """Function to call every second."""
        while self.running:
            print("Function called.")
            if self.client_socket:
                print("Close button was clicked!")
                self.client_socket.sendall('run'.encode('utf-8'))
            else:
                print("Not connected to a server.")
            time.sleep(1)  # Wait for 1 second

    def start(self):
        """Start the repetitive task."""
        if not self.running:
            self.running = True
            self.thread = Thread(target=self.repetitive_task)
            self.thread.start()
            
    def on_close(self):
        """Handle the window close event."""
        #self.stop()  # Stop the repetitive task
        self.root.destroy()  # Destroy the window

    def stop(self):
        """Stop the repetitive task."""
        self.running = False
        self.thread.join()  # Wait for the thread to finish
        
    def client(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect(('localhost', 6789))  # Replace 'localhost' with the actual server IP if necessary
            self.client_socket.sendall('ready'.encode('utf-8'))
            print("Connected to server")
        except Exception as e:
            print(f"Failed to connect to server: {e}")

    def on_connect_click(self):
        print("Connect button was clicked!")
        self.client()



    def on_close_profit_click(self):
        if self.client_socket:
            print("Close Profit button was clicked!")
            self.client_socket.sendall('close_profit'.encode('utf-8'))
        else:
            print("Not connected to a server.")




    def on_start_click(self):
        if self.client_socket:
            print("Start button was clicked!")
            self.client_socket.sendall('start'.encode('utf-8'))
        else:
            print("Not connected to a server.")
        


    def on_buy_click(self):
        if self.client_socket:
            print("buy button was clicked!")
            self.client_socket.sendall('buy'.encode('utf-8'))
        else:
            print("Not connected to a server.")
            
    def on_sell_click(self):
     
        if self.client_socket:
            print("sell button was clicked!")
            self.client_socket.sendall('sell'.encode('utf-8'))
        else:
            print("Not connected to a server.")  
            

        
    def on_close_click(self):
        if self.client_socket:
            print("Close button was clicked!")
            self.client_socket.sendall('close'.encode('utf-8'))
        else:
            print("Not connected to a server.")
            
            
            
# Create the main window
root = tk.Tk()
root.title("ForexInThai Trading Controller")
root.geometry("350x400")
root.configure(bg='black')

app = App(root)
# Start the GUI event loop
root.mainloop()
