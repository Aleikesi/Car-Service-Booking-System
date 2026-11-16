import tkinter as tk

window =  tk.Tk()
window.title("Car Service Booking System")
window.geometry('800x600')

label = tk.Label(window, font=("Times New Roman", 20, "bold"), text="Welcome to Car Service  Manager")
label.pack(expand=True)

button_frame = tk.Frame(window)
button_frame.pack(pady=20)

def open_customer_window():
    customer_window = tk.Toplevel(window)
    customer_window.title("Customer Management")
    customer_window.geometry('600x400')
    label = tk.Label(customer_window, font=("Times New Roman", 18, "bold"), text="Customer Management System")
    label.pack(pady=20)

customer_button = tk.Button(button_frame, text="Customer Management", command=open_customer_window)
customer_button.pack(pady=10)

appointment_button =  tk.Button(button_frame, text="Appointment Management")
appointment_button.pack(pady=10)

order_button =  tk.Button(button_frame, text="Service Orders")
order_button.pack(pady=10)



window.mainloop()