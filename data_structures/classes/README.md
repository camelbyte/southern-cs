Classes

    Blueprint for objects, contains attributes (data) and methods (functions).
    Use __init__() for initialization.
    Use instance methods, class methods (@classmethod), and static methods (@staticmethod).


| Feature          | Description                                  | Example |
|-----------------|----------------------------------------------|---------|
| **Instance Variable** | Specific to each instance | `self.name = name` |
| **Class Variable** | Shared across all instances | `species = "Human"` |
| **Instance Method** | Uses `self`, operates on instance data | `def greet(self):` |
| **Class Method** | Uses `@classmethod`, operates on class data | `@classmethod def set_species(cls, new_species):` |
| **Static Method** | Uses `@staticmethod`, doesn't depend on class/instance | `@staticmethod def is_adult(age): return age >= 18` |Classes

    Blueprint for objects, contains attributes (data) and methods (functions).
    Use __init__() for initialization.
