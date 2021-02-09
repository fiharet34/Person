from mimesis import Generic
from tkinter import *
from mimesis.enums import Gender
g = Generic('ru')
#print(dir(g.person))
print('ID -', g.address.street_number())
print('Фамилия -', g.person.surname())
print('Имя -', g.person.name(gender=Gender.MALE))
print('Отчество -', g.person.last_name())
print('Пол -', g.person.sex())
print('Возраст -', g.person.age())
print('Город -', g.address.city())
print('Улица -', g.address.street_name())
print('Телефон -', g.person.telephone())
print('Email -', g.person.email())

#root = Tk()
#root.geometry("485x630")
#root.title("Человек")
#root.mainloop()