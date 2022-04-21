import numpy as np

from src.fields import ScalarField


class LaplaceEquationSolver:
    """
    A Laplace equation solver used to compute the resultant potential field P in 2D-space generated by a constant
    voltage field V (for example due to wires).
    """

    def __init__(self, nb_iterations: int = 3000):
        """
        Laplace solver constructor. Used to define the number of iterations for the relaxation method.

        Parameters
        ----------
        nb_iterations : int
            Number of iterations performed to obtain the potential by the relaxation method (default = 1000).
        """
        self.nb_iterations = nb_iterations

    def solve(self, constant_voltage: ScalarField) -> ScalarField:
        """
        Solve the Laplace equation to compute the potential field given a constant voltage field.

        Parameters
        ----------
        constant_voltage : ScalarField
            A scalar field V : ℝ² → ℝ ; (x, y) → V(x, y), where V(x, y) is the wires' voltage at a given point (x, y)
            in space.

        Returns
        -------
        potential : ScalarField
            A scalar field P : ℝ² → ℝ ; (x, y) → P(x, y), where P(x, y) is the electric potential at a given point
            (x, y) in space. The difference between P and V is that P gives the potential in the whole world, i.e in
            the wires and in the empty space between the wires, while the field V always gives V(x, y) = 0 if (x, y)
            is not a point belonging to an electric wire.
        """
        voltage = np.pad(constant_voltage, pad_width=1, mode='constant', constant_values=0)
        for i in range(self.nb_iterations):
            a_1 = voltage[:-2, 1:-1]/4
            a_2 = voltage[2:,1:-1]/4
            a_3 = voltage[1:-1,:-2]/4
            a_4 = voltage[1:-1, 2:]/4
            voltage_n1 = (a_1+a_2+a_3+a_4)
            fin = np.where(constant_voltage ==0, voltage_n1, constant_voltage.copy())
            if np.max(abs(fin- voltage_n1)) <= 1**-10:
                break
            else :
                voltage = np.pad(fin, 1)
        return ScalarField(fin)
        
