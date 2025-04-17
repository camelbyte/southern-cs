"""
Title: Exercise 3 - Classes
Author: Keith Thomson

"""



class Person:
    def __init__(self, name, age, student_id, classes):


        """
        Description: The __init__ constructor initializes the class with attributes: name, age, student_id, and classes.

        Parameters:
            name (str): The name of the person.
            age (int): The age of the person.
            student_id (str): The student ID of the person.
            classes (list): A list of classes the person is enrolled in.

        Returns:
            None
        """


        self.name = name
        self.age = age
        self.student_id = student_id


        self.classes = classes

    def __str__(self):
        """
        Description: This method returns a string representation of the object.
        Without doing this, printing the Person object would render output like this:

        <__main__.Person object at 0x78409ad36e40>
        __str__ method tells python I want a string, not the object location. 
        
        Parameters: None
        
        Returns: A string representation of the object.
        """
        return f"Person({self.name}, Age: {self.age}, ID: {self.student_id}, Classes: {', '.join(self.classes)})"


    def speak(self):
        """
        Description: This method uses self from which I can grab any attributes
        
        Parameters: None
        
        Returns: A string representation of the object.
        """

        return f"Hello! My name is {self.name} and my student_id is {self.student_id}"


    def schedule(self, classes):
        """
        Description: This method takes the 'classes' attribute, and returns a list containing courses.
        
        Parameters: classes (list)
        
        Returns: A list[] or strings containing courses.
        """

        return f"{self.name} is currently taking: {', '.join(self.classes)}"



class Teacher(Person):
    """
    Description: The Teacher class extends the Person class and adds a teacher_id attribute.

    # This is called inheritance. The Teacher class inherits all the attributes and methods of the Person class.

    Parameters: name, age, teacher_id, classes (list)

    Returns: None
    """
    def __init__(self, name, age, teacher_id, classes):
        super().__init__(name, age, teacher_id, classes)
        self.teacher_id = teacher_id

    def __str__(self):
        return f"Teacher({self.name}, Age: {self.age}, ID: {self.teacher_id}, Classes: {', '.join(self.classes)})"

    def speak(self):
        return f"Hello, {student_1.name}! My name is Professor {self.name} :) My teacher_id is {self.teacher_id}"


teacher_1 = Teacher("Dr. Smith", 45, "id_67890", ['Ethics', 'Programming', 'Mathematics'])

student_1 = Person("John Doe", 25, "id_12345", ['Ethics', 'Programming', 'Mathematics'])





if __name__ == '__main__':
    print("\n")
    print(student_1.speak())
    print(teacher_1.speak())

    print(student_1.schedule(student_1.classes))
    print(teacher_1.schedule(teacher_1.classes))


    print("\nThis is how the __str__ method prints the class object:\n")
    print(student_1)
    print(teacher_1)

    print("\nYou could also call it explicitly like below: \n")
    print(Person.__str__(self=student_1))

    print("\n Printing the class directly without a __str__ method gets you the class object location:")
    print(Person)
    print(Teacher)






"""

Summary:

Object-oriented programming (OOP) enhances code organization, readability, and maintainability by leveraging key 
principles such as polymorphism, encapsulation, inheritance, and abstraction. Instead of defining separate classes for 
each individual object, I can create a single base class and extend its functionality through subclasses. For instance, 
rather than creating a new "Person" class for every individual, I can define a general "Person" class and derive 
subclasses like "Student," "Teacher," or "Faculty" using inheritance.  

Polymorphism allows methods like `speak()` to be defined in the base class and customized in each subclass. While each 
subclass can implement its own version of `speak()`, the method remains universally accessible across all instances. 
Encapsulation ensures that class attributes are protected from external access, preventing unintended modifications.

"""
 
