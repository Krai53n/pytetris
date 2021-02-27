def generate_field():
    width = 10
    height = 20
    empty_cell = 0

    fields = []
    for h in range(width):
        fields.append([])
        for w in range(width):
            fields[h].append(0)
    return fields


class Tetris:
    def __init__(self):
        pass
    
    def run(self):
        self.field = generate_field()
    
    def pause(self):
        pass
    
    def cnte(self):
        """
        cnte - continue
        """
        pass


if __name__ == "__main__":
    Tetris().run()
