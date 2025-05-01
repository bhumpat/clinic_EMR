import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import hashlib
from db import get_connection

class LoginFrame(ttk.Frame):
        def __init__(self, parent, controller):
                super().__init__(parent)
                self.place(x = 0, y = 0, relwidth = 1, relheight = 1)
                self.controller = controller                
                
                #create login entry
                userlabel = ttk.Label(self, text = "Username").pack(pady=(10,0))
                self.user = tk.StringVar()
                username = ttk.Entry(self, textvariable = self.user)
                username.pack()

                passlabel = ttk.Label(self, text = "Password").pack(pady=(10,0))
                self.pas = tk.StringVar()
                password = ttk.Entry(self, show = "*", textvariable = self.pas)
                password.pack()
                button = ttk.Button(self, text = "login", command = self.login)
                button.pack(pady=(20,0))

        #define hash function
        def hash_password(self, password):
                h = hashlib.sha256()
                h.update(password.encode())
                return h.hexdigest()

        #define login function
        def login(self):
                #connnect to database
                conn, cursor = get_connection()
                a = self.user.get()
                b = self.pas.get()
                hashed = self.hash_password(b)
                cursor.execute('''
                SELECT * FROM users WHERE username = ? and password = ?
                                ''', (a,hashed))
                result = cursor.fetchone()
                conn.close()
                if result is not None:
                        self.controller.set_current_user(result[0],result[3])
                        self.controller.show_frame("DashboardFrame")  
                        
                else:
                        tkinter.messagebox.showerror("Error", "Please enter valid data")
                        return