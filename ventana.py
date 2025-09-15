import tkinter as tk
import threading
import webbrowser
import os

def lanzar_dashboard():
    threading.Thread(target=lambda: os.system("python -m streamlit run app.py"), daemon=True).start()
    threading.Timer(2, lambda: webbrowser.open("http://localhost:8501")).start()

def run():
    root = tk.Tk()
    root.title("Dashboard Tormenta")
    root.geometry("300x150")

    label = tk.Label(root, text="Pulsa para abrir el Dashboard", font=("Arial", 12))
    label.pack(pady=20)

    btn = tk.Button(root, text="Abrir Dashboard", command=lanzar_dashboard, font=("Arial", 12))
    btn.pack(pady=10)

    root.mainloop()
