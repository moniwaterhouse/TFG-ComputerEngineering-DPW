import tkinter as tk
from tkinter import filedialog
from dpw import start_simulation

TERRITORY_PATH = "Territory/territory.txt"
URI = 'radio://0/80/2M/E7E7E7E7E7'
TARGET_HEIGHT = 0.3
TARGET_SPEED = 0.2
TRAVEL_DISTANCE = 0.4
PHEROMONE_INTENSITY = 300

''' This method allows the selection of a .txt file with the territory'''
def select_file():
    global TERRITORY_PATH
    file_path = filedialog.askopenfilename()
    TERRITORY_PATH = file_path
    file_label.config(text=f"Selected file: {TERRITORY_PATH}")

''' This method allows user to enter the URI'''
def set_URI():
    global URI

    try:
        URI = uri_entry.get()
        print(f"URI set to {URI}")

    except ValueError:
        print("Please enter a valid URI.")

''' This method allows user to enter the flight height'''
def set_height():
    global TARGET_HEIGHT

    try:
        TARGET_HEIGHT = float(height_entry.get())
        print(f"Target height set to {TARGET_HEIGHT}")

    except ValueError:
        print("Please enter a valid value for the height.")

''' This method allows user to enter the drone speed'''
def set_speed():
    global TARGET_SPEED

    try:
        TARGET_HEIGHT = float(speed_entry.get())
        print(f"Target speed set to {TARGET_SPEED}")

    except ValueError:
        print("Please enter a valid value for the speed.")

''' This method allows user to enter the travel distance between cells'''
def set_travel_distance():
    global TARGET_SPEED

    try:
        TRAVEL_DISTANCE= float(travel_distance_entry.get())
        print(f"Target speed set to {TRAVEL_DISTANCE}")

    except ValueError:
        print("Please enter a valid value for the travel distance.")

''' This method allows user to enter the number of drones and the pheromone intensity'''
def set_parameters():
    global PHEROMONE_INTENSITY

    try:
        PHEROMONE_INTENSITY = int(pheromone_entry.get())
        print(f"Pheromone intensity set to {PHEROMONE_INTENSITY}")

    except ValueError:
        print("Please enter a valid integer for the pheromone intensity.")

''' This method is triggered when the submit button is pressed. It starts the simulation.'''
def open_pygame_window():
    start_simulation(TERRITORY_PATH, URI, TRAVEL_DISTANCE, TARGET_HEIGHT, TARGET_SPEED, PHEROMONE_INTENSITY)

# Create the main window
root = tk.Tk()
root.title("DPW Parameters")
root.geometry("600x550")

# Create and place the widgets
select_file_button = tk.Button(root, text="Select File", command=select_file)
select_file_button.pack(pady=20)

file_label = tk.Label(root, text="Selected file: ")
file_label.pack()

pheromone_label = tk.Label(root, text="Enter the pheromone intensity: ")
pheromone_label.pack(pady=10)
pheromone_entry = tk.Entry(root)
pheromone_entry.pack()

height_label = tk.Label(root, text="Enter the target altitude (m): ")
height_label.pack(pady=10)
height_entry = tk.Entry(root)
height_entry.pack()

speed_label = tk.Label(root, text="Enter the speed (m/s): ")
speed_label.pack(pady=10)
speed_entry = tk.Entry(root)
speed_entry.pack()

travel_distance_label = tk.Label(root, text="Enter the travel distance (m): ")
travel_distance_label.pack(pady=10)
travel_distance_entry = tk.Entry(root)
travel_distance_entry.pack()

uri_label = tk.Label(root, text="Enter the URI (): ")
uri_label.pack(pady=10)
uri_entry = tk.Entry(root)
uri_entry.pack()

submit_button = tk.Button(root, text="Submit", command=open_pygame_window)
submit_button.pack(pady=20)

# Start the main loop
root.mainloop()
