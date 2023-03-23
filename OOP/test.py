# Решения 8 таска:
class Password: 
    
    def __init__(self, pass_name): 
        self.pass_name = pass_name 

    def validate(self):
        x = self.pass_name
        for a in x:
            if x=='#' and x=='@' and x=='&' and x=='$' and x=='%' and x=='!' and x=='~' and x=='*':
                print('Your password should have some symbols')
            elif x != str not in x:
                print('Password should contain letters as well')
            elif x != int not in x:
                print('Password should contain numbers too')
            elif len(a) < 8 and len(a) > 15:
                print('Password should be longer than 8, and less than 15')
            else:
                print('Ваш пароль сохранен.')

    def __repr__(self):
        return str(self.pass_name)
    
    def __str__(self):
        return self.validate(self.pass_name)
    
obj = Password('112fffgg') 
print(obj) 