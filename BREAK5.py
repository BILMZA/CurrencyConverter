import tkinter as tk  
import requests  

class CurrencyConverter:  
    def __init__(self):  
        self.root = tk.Tk()  
        self.root.title('CURRENCY CONVERTER')  
        self.root.geometry('200x250')  

        self.currencies = ['USD', 'EUR', 'GBP', 'INR', 'AUD', 'CAD','PKR']  
        self.from_var = tk.StringVar(self.root)  
        self.from_var.set('USD')  
        self.to_var = tk.StringVar(self.root)  
        self.to_var.set('EUR')  

        self.create_gui()  

    def create_gui(self):  
        # From Currency  
        self.from_menu = tk.OptionMenu(self.root, self.from_var, *self.currencies)  
        self.from_menu.pack(pady=5)  

        # To Currency  
        self.to_menu = tk.OptionMenu(self.root, self.to_var, *self.currencies)  
        self.to_menu.pack(pady=5)  

        # Amount Input  
        self.amount_label = tk.Label(self.root, text='Amount:')  
        self.amount_label.pack(pady=5)  

        self.amount_entry = tk.Entry(self.root)  
        self.amount_entry.pack(pady=5)  

        # Convert Button  
        self.convert_button = tk.Button(self.root, text='Convert', command=self.convert_currency)  
        self.convert_button.pack(pady=5)  

        # Quit Button  
        self.quit_button = tk.Button(self.root, text='Quit', command=self.root.destroy)  
        self.quit_button.pack(pady=5)  

        # Result Label  
        self.result_label = tk.Label(self.root, text="")  
        self.result_label.pack(pady=5)  

    def convert_currency(self):  
        try:  
            from_currency = self.from_var.get()  
            to_currency = self.to_var.get()  
            amount = float(self.amount_entry.get())  

            response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{from_currency}')  
            data = response.json()  
            rate = data['rates'][to_currency]  
            converted_amount = amount * rate  

            self.result_label.config(  
                text=f'{amount} {from_currency} = {converted_amount:.2f} {to_currency}'  
            )  
        except ValueError:  
            self.result_label.config(text='Please enter a valid number')  
        except KeyError:  
            self.result_label.config(text='Invalid currency')  
        except Exception as e:  
            self.result_label.config(text=f'An error occurred: {str(e)}')  

    def run(self):  
        self.root.mainloop()  

if __name__ == '__main__':  
    converter = CurrencyConverter()  
    converter.run()