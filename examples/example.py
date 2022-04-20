import env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World


if __name__ == "__main__":
    world = World(shape=(51, 51))

    wires = [
        Wire(start=(25, 13), stop=(13, 13), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(13, 13), stop=(13, 37), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(13, 37), stop=(25, 37), current=Current(x=0, y=-1), voltage=4.5),
        Wire(start=(25, 37), stop=(37, 37), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(37, 37), stop=(37, 13), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(37, 13), stop=(25, 13), current=Current(x=0, y=1), voltage=-4.5),
    ]

    circuit = Circuit(wires=wires)

    world.place(circuit)

    world.compute()

    world.show_all()
