# Importing the Enum module for creating enumerated constants
from enum import Enum

# Definition of the Atom class representing atomic structures
class Atom:
    def __init__(self, name, atomic_mass_unit, neutrons_number, protons_number, electrons_number, atom_type):
        # Initializing attributes for the atom
        self.name = name
        self.atomic_mass_unit = atomic_mass_unit
        self.neutrons = neutrons_number
        self.protons = protons_number
        self.electrons = electrons_number
        self.atom_type = atom_type

    def __str__(self):
        # String representation of the Atom object
        return f"{self.name} ({self.atomic_mass_unit} AMU, {self.neutrons} neutrons, {self.protons} protons, {self.electrons} electrons, Type: {self.atom_type})"

    def is_neutral(self):
        # Checking if the atom is electrically neutral
        return self.neutrons == self.electrons

# Definition of the EnumType class as an enumeration for atom types
class EnumType(Enum):
    ISOTYPE = 1
    RADIOACTIVE = 2
    ION = 3
    ANTIMATTER = 4
    STABLE = 5

# Definition of the Molecule class representing a collection of atoms
class Molecule:
    def __init__(self, name, atoms):
        # Initializing attributes for the molecule
        self.name = name
        self.atoms = atoms

    def add(self, atom):
        # Adding an atom to the molecule
        self.atoms.append(atom)

    def sortAtomsByMass(self):
        # Sorting atoms in the molecule by atomic mass in descending order
        self.atoms.sort(key=lambda atom: atom.atomic_mass_unit, reverse=True)
        # Printing the sorted atom names
        for atom in self.atoms:
            print(atom.name)

    def find_average_mass(self):
        # Calculating and returning the average atomic mass of atoms in the molecule
        total_mass = sum(atom.atomic_mass_unit for atom in self.atoms)
        return total_mass / len(self.atoms) if len(self.atoms) > 0 else 0

    def __str__(self):
        # String representation of the Molecule object
        return f"Molecule: {self.name}\nAtoms: {', '.join(atom.name for atom in self.atoms)}"

# Main function for demonstrating the functionality of the classes
def main():
    # Creating instances of Atom with specific parameters
    atom_oxygen = Atom("Oxygen", 16.00, 8, 8, 8, EnumType.ISOTYPE)
    atom_hydrogen = Atom("Hydrogen", 1.008, 0, 1, 1, EnumType.STABLE)

    # Creating a Molecule instance with atoms and a name
    molecule = Molecule("Water", [atom_oxygen, atom_hydrogen])

    # Sorting and printing atoms in the molecule by atomic mass
    molecule.sortAtomsByMass()

    # Printing detailed information about each atom in the molecule
    for atom in molecule.atoms:
        print(atom)

    # Calculating and printing the average atomic mass of atoms in the molecule
    average_mass = molecule.find_average_mass()
    print(f"\nAverage Mass of Atoms in {molecule.name}: {average_mass}")

    # Checking and printing whether each atom in the molecule is neutral
    for atom in molecule.atoms:
        print(f"{atom.name} is neutral: {atom.is_neutral()}")

# Invoking the main function to execute the code
main()
