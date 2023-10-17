from Territory.cell import Cell
from client.territory_client import initiate_territory, delete_territory, reset_territory

class Territory:
    
    def __init__(self, file_path):

        self.file_path = file_path  # Replace with your file name
        self.lines = self.open_file()

        # Determine the dimensions of the matrix
        self.num_rows = len(self.lines)
        self.num_cols = max(len(line) for line in self.lines)
        self.matrix = self.create_territory();
    
    
    def open_file(self):
        # Read the file line by line
        with open(self.file_path, "r") as file:
            lines = file.readlines()
        # Remove newline characters
        lines = [line.rstrip("\n") for line in lines]
        return lines
        
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

    def initiate_territory_db(self):
        response = initiate_territory(self.file_path)
        return response
    
    def delete_territory(self):
        response = delete_territory()
        return response
    
    def reset_territory(self):
        response = reset_territory()
        return response
    


        
'''def main():
    newTerritory = Territory("territory1.txt")
    territory = newTerritory.matrix
    for row in territory:
        print("\n")
        for cell in row:
            print(cell.visited, " ", end='')

main()'''