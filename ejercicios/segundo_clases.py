#Crear una clase Student que tiene los siguientes atributos: name, age y grades (una lista de números)

class Student:
    name=str
    age=int
    grades=[1,2,3,4,5,6,7,8,9]

#Crear un constructor que inicialice los atributos

    def __init__(self,name,age,grades):
        self.name:str=name
        self.age:int=age
        self.grades:[]=grades

#Crear un método llamado add_grade que recibe un número como parámetro y lo agrega a la lista grades.

    def add_grade(self,grades_list):
        if self.grades_list in self.grades:
            return "grado agregado"
        else:
         self.grades.append(grades_list)
         grades_list.grade_list2.append(self)
        return "grado agregado"

#Crear otro método llamado average_grade que calcule y retorne la nota promedio de la lista de notas grades
    def average_grade(self,nota:[]):
        for i in range(nota):
            if nota <= 2.5:
                return "la nota perdida es " + i in nota
            else:
                return "no hay nota perdida"


a=Student.add_grade([])
print(a)

a=Student.__init__("juan",19)


print(a)

