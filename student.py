class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.physics_marks = 0
        self.chemistry_marks = 0
        self.mathematics_marks = 0

    def enter_marks(self, physics_marks, chemistry_marks, mathematics_marks):
        self.physics_marks = physics_marks
        self.chemistry_marks = chemistry_marks
        self.mathematics_marks = mathematics_marks

    def change_marks(self, physics_marks=None, chemistry_marks=None, mathematics_marks=None):
        if physics_marks is not None:
            self.physics_marks = physics_marks
        if chemistry_marks is not None:
            self.chemistry_marks = chemistry_marks
        if mathematics_marks is not None:
            self.mathematics_marks = mathematics_marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Physics Marks: {self.physics_marks}")
        print(f"Chemistry Marks: {self.chemistry_marks}")
        print(f"Mathematics Marks: {self.mathematics_marks}")


# Example usage:
student1 = Student("Alice", "S001")
student1.enter_marks(85, 90, 95)
student1.display_details()

# If marks need to be changed
student1.change_marks(physics_marks=90, mathematics_marks=92)
student1.display_details()
