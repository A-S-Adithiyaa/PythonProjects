import random

directions = ['l', 'r', 's', 'b']

class GeneratePaths():
    """Returns a list of list containing combination of directions"""


    def generate_paths():
        def generate_path():
            path = []

            first_path = random.randint(0, 2)
            first_direction = directions[first_path]
            path.append(first_direction)

            for j in range(4):
                path_choosed = random.randint(0, 2)
                direction_choosed = directions[path_choosed]
                path.append(direction_choosed)
                
            return path

        paths = []
        while len(paths) != 9:
            path = generate_path()

            if path not in paths:
                paths.append(path)
        return paths
