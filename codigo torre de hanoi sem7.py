class TowerOfHanoi:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.source_stack = []
        self.auxiliary_stack = []
        self.destination_stack = []
        self.initialize_towers()

    def initialize_towers(self):
        for i in range(self.num_disks, 0, -1):
            self.source_stack.append(i)

    def move_disk(self, from_stack, to_stack):
        disk = from_stack.pop()
        to_stack.append(disk)
        print(f"Moviendo disco {disk} de {from_stack} a {to_stack}")

    def solve_towers(self, num_disks, source, auxiliary, destination):
        if num_disks == 1:
            self.move_disk(source, destination)
        else:
            self.solve_towers(num_disks - 1, source, destination, auxiliary)
            self.move_disk(source, destination)
            self.solve_towers(num_disks - 1, auxiliary, source, destination)

    def run(self):
        print(f"Resolviendo las Torres de Hanoi con {self.num_disks} discos:")
        self.solve_towers(self.num_disks, self.source_stack, self.auxiliary_stack, self.destination_stack)

def main():
    num_disks = 3
    towers = TowerOfHanoi(num_disks)
    towers.run()

if __name__ == "__main__":
    main()
