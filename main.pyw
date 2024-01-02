import tkinter as tk
import tkinter.ttk as ttk
import requests

pad = 5
root = tk.Tk()
root.title("CEP Finder")
root.geometry("625x229")
root.minsize(width=372, height=230)
root.resizable(True, False)
root.iconphoto(True, tk.PhotoImage(file="assets/logo.png"))

root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=0)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)

logradouro = ""
bairro = ""
cidade = ""
uf = ""
ddd = ""

# Functions
def checkbutton():
    if lb_logradouro.cget("text") == "":
        button2.configure(state="disabled")
    else:
        button2.configure(state="enabled")

    if lb_bairro.cget("text") == "":
        button3.configure(state="disabled")
    else:
        button3.configure(state="enabled")

    if lb_cidade.cget("text") == "":
        button4.configure(state="disabled")
    else:
        button4.configure(state="enabled")

    if lb_uf.cget("text") == "":
        button5.configure(state="disabled")
    else:
        button5.configure(state="enabled")

    if lb_ddd.cget("text") == "":
        button6.configure(state="disabled")
    else:
        button6.configure(state="enabled")


# Column 0
label1 = tk.Label(root, text="Digite o CEP:", font=("Segoe UI", 12))
label1.grid(row=0, column=0, padx=pad, pady=pad, sticky="w")

label2 = tk.Label(root, text="Logradouro:", font=("Segoe UI", 10))
label2.grid(row=1, column=0, padx=pad, pady=pad, sticky="w")

label3 = tk.Label(root, text="Bairro:", font=("Segoe UI", 10))
label3.grid(row=2, column=0, padx=pad, pady=pad, sticky="w")

label4 = tk.Label(root, text="Cidade:", font=("Segoe UI", 10))
label4.grid(row=3, column=0, padx=pad, pady=pad, sticky="w")

label5 = tk.Label(root, text="Unidade Federativa:", font=("Segoe UI", 10))
label5.grid(row=4, column=0, padx=pad, pady=pad, sticky="w")

label6 = tk.Label(root, text="DDD:", font=("Segoe UI", 10))
label6.grid(row=5, column=0, padx=pad, pady=pad, sticky="w")

# Column 1

entry1 = ttk.Entry(root, justify="center")
entry1.grid(row=0, column=1, padx=pad, pady=pad, columnspan=2, sticky="NSEW")

lb_logradouro = tk.Label(root, text=logradouro, justify="center")
lb_logradouro.grid(row=1, column=1, padx=pad, pady=pad)

lb_bairro = tk.Label(root, text=bairro, justify="center")
lb_bairro.grid(row=2, column=1, padx=pad, pady=pad)

lb_cidade = tk.Label(root, text=cidade, justify="center")
lb_cidade.grid(row=3, column=1, padx=pad, pady=pad)

lb_uf = tk.Label(root, text=uf, justify="center")
lb_uf.grid(row=4, column=1, padx=pad, pady=pad)

lb_ddd = tk.Label(root, text=ddd, justify="center")
lb_ddd.grid(row=5, column=1, padx=pad, pady=pad)

label_error = tk.Label(root)
label_error.grid(row=6, column=1, padx=pad, pady=pad, columnspan=2)


def command0():
    try:
        cep = "".join(filter(lambda char: char.isdigit(), entry1.get()))
        json = (requests.get(f"https://viacep.com.br/ws/{cep}/json/")).json()
        lb_logradouro.configure(text=json['logradouro'])
        lb_bairro.configure(text=json['bairro'])
        lb_cidade.configure(text=json['localidade'])
        lb_uf.configure(text=json['uf'])
        lb_ddd.configure(text=json['ddd'])
        label_error.configure(text="")
    except requests.exceptions.JSONDecodeError:
        label_error.configure(text="Não foi encontrar o CEP! Tente novamente.", font=("Segoe UI", 10), foreground="red")
        lb_logradouro.configure(text="")
        lb_bairro.configure(text="")
        lb_cidade.configure(text="")
        lb_uf.configure(text="")
        lb_ddd.configure(text="")
    checkbutton()


button0 = ttk.Button(root, text="Listar", command=command0)
button0.grid(row=6, column=0, sticky="w", padx=pad, pady=pad)


# Column 2
def command2():
    root.clipboard_clear()
    root.clipboard_append(lb_logradouro.cget("text"))


button2 = ttk.Button(root, text="Copiar", command=command2, state="disabled")
button2.grid(row=1, column=2, padx=pad, pady=pad, sticky="e")


def command3():
    root.clipboard_clear()
    root.clipboard_append(lb_bairro.cget("text"))


button3 = ttk.Button(root, text="Copiar", command=command3, state="disabled")
button3.grid(row=2, column=2, padx=pad, pady=pad, sticky="e")


def command4():
    root.clipboard_clear()
    root.clipboard_append(lb_cidade.cget("text"))


button4 = ttk.Button(root, text="Copiar", command=command4, state="disabled")
button4.grid(row=3, column=2, padx=pad, pady=pad, sticky="e")


def command5():
    root.clipboard_clear()
    root.clipboard_append(lb_uf.cget("text"))


button5 = ttk.Button(root, text="Copiar", command=command5, state="disabled")
button5.grid(row=4, column=2, padx=pad, pady=pad, sticky="e")


def command6():
    root.clipboard_clear()
    root.clipboard_append(lb_ddd.cget("text"))


button6 = ttk.Button(root, text="Copiar", command=command6, state="disabled")
button6.grid(row=5, column=2, padx=pad, pady=pad, sticky="e")

root.mainloop()
