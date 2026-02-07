class User:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def age_control(self):
        if self.age < 18:
            return 'Сначала получи паспорт, а потом уже баб ***'
        else:
            return 'Красавчик, можешь проходить на тусу'

print('Added something new, just check the commit')