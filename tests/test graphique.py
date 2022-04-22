import env_tests  # Modifies path, DO NOT REMOVE
import unittest

from src.circuit import Circuit
from src.wire import Current, Wire
from src.world import World


class TestWorld(unittest.TestCase):

    WORLD_SHAPE = (71, 71)
    
    WIRES_0 = [ #boucle a
        Wire(start=(35, 10), stop=(10, 10), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(10, 10), stop=(10, 61), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(10, 61), stop=(35, 61), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(35, 61), stop=(61, 61), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(61, 61), stop=(61, 10), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(61, 10), stop=(35, 10), current=Current(x=-1, y=0), voltage=-4.5),
    ]
    
    WIRES_1 = [ #boucle b
        Wire(start=(12, 10), stop=(10, 10), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(10, 10), stop=(10, 61), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(10, 61), stop=(59, 61), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(59, 61), stop=(61, 61), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(61, 61), stop=(61, 10), current=Current(x=0,  y=-1), voltage=-4.5),
        Wire(start=(61, 10), stop=(12, 10), current=Current(x=-1, y=1), voltage=-4.5),
    ]
    
    WIRES_2 = [ #boucle c modifier le world shape pour (121, 71) 
        Wire(start=(109, 10), stop=(10, 10), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(10, 10), stop=(10, 61), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(109, 61), stop=(10, 61), current=Current(x=0, y=-1), voltage=4.5),
        Wire(start=(109, 61), stop=(111, 61), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(111, 61), stop=(111, 10), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(111, 10), stop=(109, 10), current=Current(x=0, y=1), voltage=-4.5),
    ]
    
    WIRES_3 = [ #boucle d 
        Wire(start=(35, 10), stop=(10, 10), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(10, 10), stop=(10, 61), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(35, 35), stop=(10, 35), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(35, 35), stop=(61, 35), current=Current(x=0, y=1), voltage=-4.5),
        Wire(start=(10, 61), stop=(35, 61), current=Current(x=0, y=-1), voltage=4.5),
        Wire(start=(35, 61), stop=(61, 61), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(61, 61), stop=(61, 10), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(61, 10), stop=(35, 10), current=Current(x=0, y=1), voltage=-4.5),
    ]

#Circuit1 VOIR LE PDF POUR LES FIGURES
    wire1= [
        Wire(start=(70, 45), stop=(45, 45), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(45, 45), stop=(45, 96), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(45, 96), stop=(70, 96), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(70, 96), stop=(96, 96), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(96, 96), stop=(96, 45), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(96, 45), stop=(70, 45), current=Current(x=-1, y=0), voltage=-4.5),
    ]
    
    CIRCUIT = Circuit(wires=WIRES_0)
    world = World(WORLD_SHAPE)
    world.place(CIRCUIT)
    world.compute()
    world.show_all()