import tkinter as tk
from tkinter import filedialog
from simulation import start_simulation

TERRITORY_PATH = "Territory/territory.txt"
DRONE_COUNT = 1
PHEROMONE_INTENSITY = 300

''' This method allows the selection of a .txt file with the territory'''
def select_file():
    global TERRITORY_PATH
    file_path = filedialog.askopenfilename()
    TERRITORY_PATH = file_path
    file_label.config(text=f"Selected file: {TERRITORY_PATH}")

''' This method allows user to enter the number of drones and the pheromone intensity'''
def set_parameters():
    global DRONE_COUNT
    global PHEROMONE_INTENSITY

    try:
        DRONE_COUNT = int(drone_entry.get())
        print(f"Number of drones set to {DRONE_COUNT}")
        PHEROMONE_INTENSITY = int(pheromone_entry.get())
        print(f"Number of drones set to {PHEROMONE_INTENSITY}")
        open_pygame_window()

    except ValueError:
        print("Please enter a valid integer for the drone count and pheromone intensity.")

''' This methos is triggered when the submit button is pressed. It starts the simulation.'''
def open_pygame_window():
    start_simulation(TERRITORY_PATH, DRONE_COUNT, PHEROMONE_INTENSITY)

# Create the main window
root = tk.Tk()
root.title("DPW - Simulation parameters")
root.geometry("600x300")

# Create and place the widgets
select_file_button = tk.Button(root, text="Select File", command=select_file)
select_file_button.pack(pady=20)

file_label = tk.Label(root, text="Selected file: ")
file_label.pack()

drone_label = tk.Label(root, text="Enter the number of drones: ")
drone_label.pack(pady=10)

drone_entry = tk.Entry(root)
drone_entry.pack()

pheromone_label = tk.Label(root, text="Enter the pheromone intensity: ")
pheromone_label.pack(pady=10)

pheromone_entry = tk.Entry(root)
pheromone_entry.pack()

submit_button = tk.Button(root, text="Submit", command=set_parameters)
submit_button.pack(pady=20)

# Start the main loop
root.mainloop()
