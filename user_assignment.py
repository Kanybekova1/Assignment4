from datetime import datetime
class User:
    def __init__(self,user_id:int,name:str,surname:str,email:str,password:int,birthday:datetime):
        self.user_id=user_id
        self.name=name
        self.surname=surname
        self.email=email
        self.password=password
        self.birthday = birthday 

    def get_details(self):
        return (
                    f"User ID: {self.user_id}, "
                    f"Name: {self.name} {self.surname}, "
                    f"Email: {self.email}, "
                    f"Birthday: {self.birthday.strftime('%Y-%m-%d')}"
                )    
    def get_age(self):
        age = datetime.today().year-self.birthday.year
        return age
    