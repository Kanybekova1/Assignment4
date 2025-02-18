from user_assignment import User
from user_service import UserService
from userUtil import UserUtil
from datetime import datetime

if __name__=='__main__':
    name=input('Name:')
    surname=input('Surname:')

    user= User(UserUtil.generate_user_id(),name,surname, email=UserUtil.generate_email(name,surname,'example.com'), password=UserUtil.generate_password(), birthday=datetime(2005,9,2))

    print(user.get_details())
    print(f'Age: {user.get_age()}')

    UserService.add_user(user)
    print(UserService.find_user(user.user_id).get_details())
    print(f'Number of users: {UserService.get_number()}')
    print(UserUtil.generate_password())


