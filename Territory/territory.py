from Territory.cell import Cell
from client.territory_client import initiate_territory, delete_territory, reset_territory

'''
This class represents the territory. It creates the territory in a Python matrix for simulation purposes, and it also contains
the methods to create, delete and reset the territory in the DB
'''
class Territory:
    
    def __init__(self, file_path):

        self.file_path = file_path  # Replace with your file name
        self.lines = self.open_file()

        # Determine the dimensions of the matrix
        self.num_rows = len(self.lines)
        self.num_cols = max(len(line) for line in self.lines)
        self.matrix = self.create_territory();
    
    '''
    This method is used to get each line of the territory.txt file
    '''
    def open_file(self):
        # Read the file line by line
        with open(self.file_path, "r") as file:
            lines = file.readlines()
        # Remove newline characters
        lines = [line.rstrip("\n") for line in lines]
        return lines

    '''
    This method creates the territory in a python matrix, this is just for simulation purposes.
    '''    
    def create_territory(self):
        # Create an empty matrix
        matrix = [[None for _ in range(self.num_cols)] for _ in range(self.num_rows)]

        # Store the characters in the matrix
        for i, line in enumerate(self.lines):
            for j, char in enumerate(line):
                if char == '0':
                    cell = Cell(0)
                else:
                    cell = Cell(1)
                matrix[i][j] = cell
        return matrix

    '''
    This method creates the territory in the DB
    '''
    def initiate_territory_db(self):
        response = initiate_territory(self.file_path)
        return response
    
    '''
    This method deleted the territory in the DB
    '''
    def delete_territory(self):
        response = delete_territory()
        return response
    
    '''
    This method resets the territory in the DB
    '''
    def reset_territory(self):
        response = reset_territory()
        return response
    