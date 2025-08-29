import tkinter as tk
from tkinter import font
from config import constantes as cons
from util import util_ventana as util_ventana

class FormularioCalculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.dark_theme = True
        self.buttons = []  
        self.config_window()
        self.construir_widget()
        self.construir_widget_toggle()

    def construir_widget_toggle(self):
        font_awesome = font.Font(family='Fontawesome', size=12)
        self.theme_button = tk.Button(
            self, text="Modo Oscuro \uf186", width=13, font=font_awesome,
            bd=0, borderwidth=0, highlightthickness=0, relief=tk.FLAT,
            command=self.toggle_theme, bg=cons.COLOR_BOTONES_ESPECIALES_LIGHT
        )
        self.theme_button.grid(row=0, column=0, columnspan=2, pady=0, padx=0, sticky="ew")
        
    def toggle_theme(self):
        if self.dark_theme:  
            self.configure(bg=cons.COLOR_DE_FONDO_LIGHT)
            self.entry.config(fg=cons.COLOR_DE_TEXTO_LIGHT, bg=cons.COLOR_CAJA_TEXTO_LIGHT)
            self.operation_label.config(fg=cons.COLOR_DE_TEXTO_LIGHT, bg=cons.COLOR_DE_FONDO_LIGHT)
            self.theme_button.configure(text="\uf185 Modo Claro", relief=tk.SUNKEN, bg=cons.COLOR_BOTONES_ESPECIALES_LIGHT)

            
            for btn in self.buttons:
                btn.config(bg=cons.COLOR_BOTONES_LIGHT, fg=cons.COLOR_DE_TEXTO_LIGHT)

        else:  
            self.configure(bg=cons.COLOR_DE_FONDO_DARK)
            self.entry.config(fg=cons.COLOR_DE_TEXTO_DARK, bg=cons.COLOR_CAJA_TEXTO_DARK)
            self.operation_label.config(fg=cons.COLOR_DE_TEXTO_DARK, bg=cons.COLOR_DE_FONDO_DARK)
            self.theme_button.configure(text="Modo Oscuro \uf186", relief=tk.RAISED, bg=cons.COLOR_BOTONES_ESPECIALES_LIGHT)

            
            for btn in self.buttons:
                if btn["text"] in ['=', '*', '/', '-', '+', 'C', '<', '%']:
                    btn.config(bg=cons.COLOR_BOTONES_ESPECIALES_DARK, fg=cons.COLOR_DE_TEXTO_DARK)
                else:
                    btn.config(bg=cons.COLOR_BOTONES_DARK, fg=cons.COLOR_DE_TEXTO_DARK)

        self.dark_theme = not self.dark_theme

    def config_window(self):
        self.title("Python GUI calculadora")
        self.configure(bg=cons.COLOR_DE_FONDO_DARK)
        self.attributes('-alpha', 0.96)
        w, h = 370, 570
        util_ventana.centrar_ventana(self, w, h)

    def construir_widget(self):
        self.operation_label = tk.Label(
            self, text="", font=('Arial', 16),
            fg=cons.COLOR_DE_TEXTO_DARK, bg=cons.COLOR_DE_FONDO_DARK,
            justify='right'
        )
        self.operation_label.grid(row=0, column=3, padx=10, pady=10)
        
        self.entry = tk.Entry(
            self, width=12, font=('Arial', 40), bd=0,
            fg=cons.COLOR_DE_TEXTO_DARK, bg=cons.COLOR_CAJA_TEXTO_DARK,
            justify='right'
        )
        self.entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        
        buttons = [
            'C', '%', '<', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-', 
            '1', '2', '3', '+',
            '0', '.', '=',
        ]

        row_val = 2
        col_val = 0
        roboto_font = font.Font(family="Roboto", size=16)

        for button in buttons:
            if button in ['=', '*', '/', '-', '+', 'C', '<', '%']:
                color_fondo = cons.COLOR_BOTONES_ESPECIALES_DARK
                button_font = font.Font(size=16, weight='bold')
            else: 
                color_fondo = cons.COLOR_BOTONES_DARK
                button_font = roboto_font

            if button == '=':
                btn = tk.Button(
                    self, text=button, width=11, height=2,
                    command=lambda b=button: self.on_button_click(b),
                    bg=color_fondo, fg=cons.COLOR_DE_TEXTO_DARK,
                    relief=tk.FLAT, font=button_font, padx=5, pady=5, bd=0,
                    borderwidth=0, highlightthickness=0, overrelief='flat'
                )
                btn.grid(row=row_val, column=col_val, columnspan=2, pady=5)
                col_val += 1
            else:
                btn = tk.Button(
                    self, text=button, width=5, height=2,
                    command=lambda b=button: self.on_button_click(b),
                    bg=color_fondo, fg=cons.COLOR_DE_TEXTO_DARK,
                    relief=tk.FLAT, font=button_font, padx=5, pady=5, bd=0,
                    borderwidth=0, highlightthickness=0, overrelief='flat'
                )
                btn.grid(row=row_val, column=col_val, pady=5)
                col_val += 1

            self.buttons.append(btn)  
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, value):
        if value == '=':
            try:
                expression = self.entry.get().replace('%', '/100')
                result = eval(expression)  
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                operation = expression + " " + value
                self.operation_label.config(text=operation)
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.operation_label.config(text="")
        elif value == 'C':
            self.entry.delete(0, tk.END)
            self.operation_label.config(text="")
        elif value == '<':
            current_text = self.entry.get()
            if current_text:
                new_text = current_text[:-1]
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, new_text)
                self.operation_label.config(text=new_text + " ")
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + value)
