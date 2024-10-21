import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np

# Load the model and encoders
model = joblib.load('car_price_model.pkl')
label_encoders = joblib.load('label_encoders.pkl')

# Function to make a prediction
def predict_price():
    try:
        # Get input values
        name = name_var.get()
        location = location_var.get()
        year = int(entry_year.get())
        kilometers = int(entry_kilometers.get())
        fuel = fuel_var.get()
        transmission = transmission_var.get()
        owner = owner_var.get()
        mileage = float(entry_mileage.get())
        engine = float(entry_engine.get())
        power = float(entry_power.get())
        seats = float(entry_seats.get())

        # Encode categorical features
        name_enc = label_encoders['Name'].transform([name])[0]
        location_enc = label_encoders['Location'].transform([location])[0]
        fuel_enc = label_encoders['Fuel_Type'].transform([fuel])[0]
        transmission_enc = label_encoders['Transmission'].transform([transmission])[0]
        owner_enc = label_encoders['Owner_Type'].transform([owner])[0]

        # Create feature array
        features = np.array([[name_enc, location_enc, year, kilometers, fuel_enc, transmission_enc, owner_enc, mileage, engine, power, seats]])

        # Make prediction
        price = model.predict(features)[0]
        label_result.config(text=f"Predicted Price: {price:.2f} Lakh")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for Year, Kilometers, Mileage, Engine, Power, and Seats.")

# Create the GUI window
window = tk.Tk()
window.title("Car Price Predictor")

# Tooltip function to display descriptions of fields
def create_tooltip(widget, text):
    def on_enter(event):
        widget.tooltip = tk.Toplevel()
        widget.tooltip.wm_overrideredirect(True)
        widget.tooltip.wm_geometry(f"+{widget.winfo_rootx()+20}+{widget.winfo_rooty()+20}")
        label = tk.Label(widget.tooltip, text=text, background="yellow", relief="solid", borderwidth=1)
        label.pack()

    def on_leave(event):
        widget.tooltip.destroy()

    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)

# Dropdown options from the dataset (replace with actual data from label_encoders)
names = list(label_encoders['Name'].classes_)
locations = list(label_encoders['Location'].classes_)
fuels = list(label_encoders['Fuel_Type'].classes_)
transmissions = list(label_encoders['Transmission'].classes_)
owners = list(label_encoders['Owner_Type'].classes_)

# Create variables for dropdowns
name_var = tk.StringVar(window)
location_var = tk.StringVar(window)
fuel_var = tk.StringVar(window)
transmission_var = tk.StringVar(window)
owner_var = tk.StringVar(window)

# Set default values
name_var.set(names[0])
location_var.set(locations[0])
fuel_var.set(fuels[0])
transmission_var.set(transmissions[0])
owner_var.set(owners[0])

# Dropdowns for categorical fields with tooltips
tk.Label(window, text="Car Name:").grid(row=0, column=0)
car_name_menu = tk.OptionMenu(window, name_var, *names)
car_name_menu.grid(row=0, column=1)
create_tooltip(car_name_menu, "Select the car model.")

tk.Label(window, text="Location:").grid(row=1, column=0)
location_menu = tk.OptionMenu(window, location_var, *locations)
location_menu.grid(row=1, column=1)
create_tooltip(location_menu, "Select the location where the car is being sold.")

tk.Label(window, text="Fuel Type:").grid(row=2, column=0)
fuel_menu = tk.OptionMenu(window, fuel_var, *fuels)
fuel_menu.grid(row=2, column=1)
create_tooltip(fuel_menu, "Select the type of fuel the car uses.")

tk.Label(window, text="Transmission:").grid(row=3, column=0)
transmission_menu = tk.OptionMenu(window, transmission_var, *transmissions)
transmission_menu.grid(row=3, column=1)
create_tooltip(transmission_menu, "Select the type of transmission (Manual/Automatic).")

tk.Label(window, text="Owner Type:").grid(row=4, column=0)
owner_menu = tk.OptionMenu(window, owner_var, *owners)
owner_menu.grid(row=4, column=1)
create_tooltip(owner_menu, "Select the number of previous owners.")

# Text input for numerical fields with tooltips
tk.Label(window, text="Year:").grid(row=5, column=0)
entry_year = tk.Entry(window)
entry_year.grid(row=5, column=1)
create_tooltip(entry_year, "Enter the year of manufacture (e.g., 2015).")

tk.Label(window, text="Kilometers Driven:").grid(row=6, column=0)
entry_kilometers = tk.Entry(window)
entry_kilometers.grid(row=6, column=1)
create_tooltip(entry_kilometers, "Total kilometers the car has been driven.")

tk.Label(window, text="Mileage (kmpl):").grid(row=7, column=0)
entry_mileage = tk.Entry(window)
entry_mileage.grid(row=7, column=1)
create_tooltip(entry_mileage, "Fuel efficiency of the car (kilometers per liter).")

tk.Label(window, text="Engine (CC):").grid(row=8, column=0)
entry_engine = tk.Entry(window)
entry_engine.grid(row=8, column=1)
create_tooltip(entry_engine, "Engine displacement in cubic centimeters (e.g., 1500 CC).")

tk.Label(window, text="Power (bhp):").grid(row=9, column=0)
entry_power = tk.Entry(window)
entry_power.grid(row=9, column=1)
create_tooltip(entry_power, "Power output of the car's engine in brake horsepower (bhp).")

tk.Label(window, text="Seats:").grid(row=10, column=0)
entry_seats = tk.Entry(window)
entry_seats.grid(row=10, column=1)
create_tooltip(entry_seats, "Number of seats in the car.")

# Create and place the result label
label_result = tk.Label(window, text="Predicted Price: ")
label_result.grid(row=12, column=1)

# Create and place the predict button
btn_predict = tk.Button(window, text="Predict Price", command=predict_price)
btn_predict.grid(row=11, column=1)

# Start the GUI event loop
window.mainloop()
