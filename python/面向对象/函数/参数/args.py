class Person(object):
    def __init__(self,name,gender,birth,**kwags):
        self.name=name
        self.gender=gender
        self.birth=birth
        for key,value in kwags.items():
            setattr(self,key,value)

xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student', job2='Student')

print xiaoming.name
print xiaoming.job
print xiaoming.job2