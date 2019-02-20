from tkinter import *
import tkinter as tk
from tkinter import ttk
import threading
from coinbase.wallet.client import Client
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

x = []
y = []
class Prices():

    def Etc():
        key  = "97dc0590e82deff43786f4ae989efcba"
        secret = "gamgVpze2B1Ea6EbhFRAdIqze5hEc3nDVUXV3WHJjRjQiMJECW5GnSklT6+ZjWI5Xsh/2GcFOh4yud86YAQc3Q=="
        client = Client(key, secret, api_version='YYYY-MM-DD')
        rates = client.get_spot_price(currency_pair='ETC-EUR')
        etc_name = rates['base']
        etc_price= rates['amount']
        pricelabel.config(bg="#44BE24")
        etc = float(etc_price)
        output = round(etc, 2)
        pricevar.set(output)
        curenttime = datetime.now().strftime("%H:%M:%S")
        a.set(curenttime)
        Prices.matplotCanvas(curenttime, output)
        tree.insert('', '0', text=etc_name, values=(curenttime, output))
        # print(output)

    def EtcStart():
        if check1.get() == 1:
            pricelabel.config(bg="#f2f2f2")
            threading.Timer(1.0, Prices.Etc).start()
            threading.Timer(4.0, Prices.EtcStart).start()
            checkl.set("Live")
        else:
            checkl.set("Last price")

    def matplotCanvas(x1, y1):
        x.append(x1)
        y.append(y1)
        f = Figure(figsize=(10, 5), dpi=90)
        a = f.add_subplot(111)
        a.plot(x, y, '-o')
        a.axis([0, 5, y1, y1])
        canvas = FigureCanvasTkAgg(f)
        canvas.get_tk_widget().grid(row=3, sticky="W")



window = tk.Tk()
window.title("GUI")
window.geometry("680x650")

pricevar = StringVar()
check1 = IntVar()
checkl = StringVar()
a = StringVar()


etcnev = Label(window, text="ETC", width=10, bd=1, relief="groove", bg="#ddd")
etcnev.columnconfigure(0, weight=10)
etcnev.grid(row=0, column=0, padx=2, pady=5, sticky="W")

check = tk.Checkbutton(window, variable=check1, width=15, command=Prices.EtcStart, text="Check this for live", bg="#ddd")
check.columnconfigure(1, weight=10)
check.grid(row=0, column=1, sticky="W")

datelabel = tk.Label(window, textvariable = a, width=10, bg="#ddd")
datelabel.columnconfigure(2, weight=10)
datelabel.grid(row=0, column=2, sticky="W")

pricelabel = tk.Label(window, textvariable=pricevar, fg="#000", width=10)
pricelabel.columnconfigure(3, weight=10)
pricelabel.grid(row=0, column=3, sticky="W")

checklabel = tk.Label(window, textvariable=checkl,  width="10", bd=1, relief="groove")
checklabel.columnconfigure(4, weight=10)
checklabel.grid(row=0, column=5, sticky="W")


tree = ttk.Treeview(window, columns=("Current Time", "Price"))
tree.heading("#0", text="Krypto")
tree.heading("#1", text="Current Time")
tree.heading("#2", text="Price")
tree.grid(row=1, columnspan=2, padx=2, pady=5, sticky="W")

tree.insert('', 'end', text="ETC", values=('00:00:00', 'Price'))

window.mainloop()
