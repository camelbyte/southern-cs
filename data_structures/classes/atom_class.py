

class Atom:


    def __init__(self, atomic_number, symbol, name, atomic_mass, isotope=14):
        self.atomic_number = atomic_number
        self.symbol = symbol
        self.name = name
        self.atomic_mass = atomic_mass
        self.isotope = isotope 


    def __str__(self):
        return f"{self.name} ({self.symbol}) {self.atomic_number} - {self.atomic_mass}"


    def neutrons(self):
        number = self.atomic_mass - self.atomic_number
        print(f"{self.name} has {number} neutrons")
        return number


    def grams_to_moles(self, grams):
        moles = grams / self.atomic_mass
        print(f"{grams:.1f} g is {moles:.1f} moles of {self.symbol}")
        return moles


def grams_to_m(atom, grams):
    m = grams / atom.atomic_mass
    print(f"{grams: .1f} g is {m:.1f} moles of {atom.symbol}")






if __name__ == "__main__":
    
    """
    Description: The main function creates instances of Atom and calls some class methods. Created an object 
    or instance of the Atom class called gold and used the methods defined in the class. 

    """
    oxygen = Atom(8, 'O', 'Oxygen', 15.999)
    carbon = Atom(6, 'C', 'Carbon', 12.001)


    # Call class methods
    oxygen.neutrons()
    oxygen.grams_to_moles(24)
    carbon.grams_to_moles(24)
   
    
    gold = Atom(24, 'Au', 'Gold', 96.96)
    print(gold.symbol)
    print(gold)
    gold.neutrons()


    print(gold.isotope)
    print(gold.atomic_mass)



    
    grams_to_m(gold, 23)














