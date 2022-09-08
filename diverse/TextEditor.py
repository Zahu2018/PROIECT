# Editor text (like VIM)
# Tags:['text editor', 'VIM']
# Autor: Zah
# colors: negru=#282828, rosu=#333333
'''
+------------------------------------+
|  editor text                       |
|                                    |
|                                    |
+-                                  -+
|  command line                      |
+-                                  -+
|  result                            |
+------------------------------------+
'''

theme_black = {'button': ''}

import tkinter as tk
import tkinter.font as tkfont
import tkinter.scrolledtext as ts

class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Editor_v2')

        # =========== Frame All ================
        frame = tk.Frame(self, border=1)
        frame.grid()
        
        # ========= Frame Text Editor ========
        self.tx = ts.ScrolledText(frame, width=50, 
                                  height=20,
                                  font=('Consolas', 11, ), 
                                  wrap='word', undo=True,
                                  bg = '#f6f6f6')
        self.tx.grid()
        font = tkfont.Font(font=self.tx['font'])
        tab_width = font.measure(' '*4)
        self.tx.config(tabs=(tab_width,))
        self.tx.focus()
        
        # ====== Frame Consola Input ===========
        self.ci = tk.Entry(frame, font=('Consolas', 10, 'bold'), 
                           fg='#f6f6f6', bg='#969696',
                           border=0,)
        self.ci.grid(sticky='we')

        # ====== Frame Consola Ouput ===========
        self.co = tk.Entry(frame, font=('Consolas', 10, 'bold'), 
                           bg='#f6f6f6', fg='#969696',
                           border=0,)
        self.co.grid(sticky='we')

        self.tx.bind("<Escape>", self.ch_fo)
        self.ce.bind("<Escape>", self.ch_fo)
        self.ce.bind("<Return>", self.consola)
        
    def ch_fo(self, event):  # ch_fo=change focus
        event.widget.tk_focusNext().focus()
        return("break")
        
    def consola(self, event):  # Linia de comanda; consola = co
        a = self.ce.get()  # take text from console
        self.ce.delete(0, 'end')  # delete console
        c = a.lower()
        co = c.split(' ')  # -> comanda_name fisier
        comanda = co[0]
        match comanda:
            
            case 'n':  # new file
                #self.filename = "New"
                self.tx.delete(0.0, 'end')
                self.tx.focus()
                
            case 'o':
                with open(co[1], 'r', encoding="utf-8") as f:
                    t = f.read() 
                self.tx.delete(0.0, 'end')
                self.tx.insert(0.0, t)
                self.fisierul_in_lucru = co[1]
                
            case 'sa':  # save as
                with open(co[1], 'w', encoding="utf-8") as f:
                    f.write(self.tx.get('1.0', 'end'))
                self.fisierul_in_lucru = co[1]

            case 's':  # save
                try:
                    with open(self.fisierul_in_lucru, 'w', encoding="utf-8") as f:
                        f.write(self.tx.get('1.0', 'end'))
                except AttributeError as e:
                    self.ce.insert(0, 'Nu ai unde salva.')
                    
            case 'commands':
                with open('commands.txt', 'r') as f:
                    t = f.read()
                self.tx.insert(0.0, t)
                    
            case 'quit':  # close program
                app.destroy()
                
            case 'odir':
                import os
                cwd = os.getcwd()
                files = os.listdir(cwd)
                self.tx.delete(0.0, 'end')
                text = ""
                for f in files:
                    text += f"{f}\n"
                self.tx.insert(0.0, text)
                    
            case _:
                print('Aceasta nu este o comanda')
        
if __name__ == "__main__":
    app = Editor()
    app.mainloop()


