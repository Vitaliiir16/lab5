from enum import Enum

class Atom:
    def __init__(self, name, atomic_mass_unit, neutrons_number, protons_number, electrons_number, atom_type):
        self.name = name
        self.atomic_mass_unit = atomic_mass_unit
        self.neutrons = neutrons_number
        self.protons = protons_number
        self.electrons = electrons_number
        self.atom_type = atom_type

    def __str__(self):
        return f"{self.name} ({self.atomic_mass_unit} AMU, {self.neutrons} neutrons, {self.protons} protons, {self.electrons} electrons, Type: {self.atom_type})"

    def is_neutral(self):
        return self.neutrons == self.electrons

class EnumType(Enum):
    ISOTYPE = 1
    RADIOACTIVE = 2
    ION = 3
    ANTIMATTER = 4
    STABLE = 5

class Molecule:
    def __init__(self, name, atoms):
        self.name = name
        self.atoms = atoms
    def add(self, atom):
        self.atoms.append(atom)
    def sortAtomsByMass(self):
        self.atoms.sort(key=lambda atom: atom.atomic_mass_unit, reverse=True)
        for atom in self.atoms:
            print(atom.name)


    def find_average_mass(self):
        total_mass = sum(atom.atomic_mass_unit for atom in self.atoms)
        return total_mass / len(self.atoms) if len(self.atoms) > 0 else 0

    def __str__(self):
        return f"Molecule: {self.name}\nAtoms: {', '.join(atom.name for atom in self.atoms)}"

def main():
    atom1 = Atom("Oxygen", 16.00, 8, 8, 8, EnumType.ISOTYPE)
    atom2 = Atom("Hydrogen", 1.008, 0, 1, 1, EnumType.STABLE)

    molecule = Molecule("Water", [atom1, atom2])
    molecule.sortAtomsByMass()
    for atom in molecule.atoms:
        print(atom)

    average_mass = molecule.find_average_mass()
    print(f"\nAverage Mass of Atoms in {molecule.name}: {average_mass}")
    for atom in molecule.atoms:
        print(f"{atom.name} is neutral: {atom.is_neutral()}")

if __name__ == "__main__":
    main()
