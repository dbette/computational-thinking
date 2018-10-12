class Student:      # Classes are defined with uppercase letter
    
    def __init__(self, firstname, lastname, birthday, email, grade):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.email = email
        self.phone = []
        self.grade = grade
    
    def add_phone(self, phonetype, phonenumber):
        self.phone.append(Phone(phonetype, phonenumber))

    def print(self):      # Value that is returned if print is called on the object
        output = self.firstname + " " + self.lastname + "\n" 
        output += "Birthday: " + self.birthday + "\n" 
        output += "Email: " + self.email + "\n" 
        output += "Grade: " + self.grade + "\n" 
        for number in self.phone:
            output += "Phone: " + str(number) + "\n"
        print(output)
        
class Phone:
    def __init__(self, phonetype, phonenumber):
        self.phonetype = phonetype
        self.phonenumber = phonenumber

    def __str__(self):
        return str(self.phonenumber) + " " + "(" + self.phonetype + ")"


dominik = Student('Dominik', 'Bette', '24.05.1993', 'test@web.de', '1')
dominik.add_phone('mobile', '1241118')
dominik.add_phone('home', '12428321118')

dominik.print()