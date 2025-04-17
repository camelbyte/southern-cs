class Atom:
    """An element from the periodic table."""

    def __init__(self, symbol, atomic, mass, isotope):
        """Initialize an Atom object with symbol, atomic number, mass, and isotope."""
        self.symbol = symbol
        self.atomic = atomic
        self.mass = mass
        self.isotope = isotope


    def neutrons(cls, atom):
        """Returns the number of neutrons the element has"""
        number = atom.isotope - atom.atomic
        print("%s has %d neutrons" % (atom.symbol, number))
        print("Difference of atom.isotope-atom.atomic: " + str(number))
        return number

    @classmethod 
    def grams_to_moles(cls, atom, grams):
        """Converts the mass of an element in grams to moles"""
        moles = grams / atom.mass
        print(f"{grams:.1f} g is {moles:.1f} moles of {atom.symbol}")
        return moles
    

    

if __name__ == "__main__":
    # Create Atom objects
    oxygen = Atom('O', 8, 15.999, 16)
    carbon = Atom('C', 6, 12.001, 12)

    # Call class methods
    Atom.grams_to_moles(oxygen, 24)
    Atom.grams_to_moles(carbon, 24)
    
    gold = Atom('Au', 24, 96.06, 15)
    print(gold.symbol)
