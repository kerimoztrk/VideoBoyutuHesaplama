import tkinter as tk
from tkinter import ttk,messagebox


def hesapla():
    try:
        videoBoyut= videoBoyutVar.get()
        sure=int(sureVar.get())

        #Bit hızlarını çözünürlüklerine göre ayarladığım yer (kbps)

        bitHızları={
            "360p":750,
            "480p":1500,
            "720p":3000,
            "1080p":4500
        }
        bitHızı=bitHızları[videoBoyut]

        #Dosya boyutuna göre hesaplama yani MB cinsinden

        dosyaBoyutMb=bitHızı*sure*60/8/1024
        sonucLabel.config(text=f"Video Boyutu : {dosyaBoyutMb:.2f} MB ")
    except ValueError:
        messagebox.showerror("Hata","Geçerli Bir Süre Giriniz.")


root=tk.Tk()
root.title("VİDEO Veri kullanımı Hesaplama")
root.geometry("450x450")
root.resizable(False,False)

style=ttk.Style()
style.configure("TLabel",font=("Helvetica",12))
style.configure("TButton",font=("Helvetica",12))
style.configure("TCombobox",font=("Helvetica",12))

style.map("TButton",foreground=[('active','black'),('!disabled','black')],
          background=[('active','#45a049'),('!disabled','#45a049')])

videoBoyutLabel=ttk.Label(root,text="Çözünürlük : ")
videoBoyutLabel.pack(pady=10)
videoBoyutVar=tk.StringVar()
videoBoyutCombobox=ttk.Combobox(root,textvariable=videoBoyutVar,state='readonly')
videoBoyutCombobox['values']=("360p","480p","720p","1080p")
videoBoyutCombobox.current(0)
videoBoyutCombobox.pack(pady=10)


sureLabel=ttk.Label(root,text="Video süresi (Dakika): ")
sureLabel.pack(pady=10)
sureVar=tk.StringVar()
sureEntry=ttk.Entry(root,textvariable=sureVar)
sureEntry.pack(pady=10)

hesapButonu=ttk.Button (root, text="Hesapla", command=hesapla)
hesapButonu.pack(pady=20)

sonucLabel=ttk.Label(root,text="Video Boyutu: ")
sonucLabel.pack(pady=20)

root.mainloop()
