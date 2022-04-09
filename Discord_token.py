import os,requests
from colorama import Fore
def token(email, password):
    data={
        'email': email, 
        'password': password, 
        'undelete': "false"
        }
    he={
        "content-type": "application/json",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
        }
    req = requests.post('https://discord.com/api/v9/auth/login', json=data, headers=he)
    if req.status_code == 200:
        token = req.json()['token']
        print(f"{Fore.WHITE}[ {Fore.LIGHTMAGENTA_EX}*{Fore.WHITE} ] Token >> {Fore.LIGHTMAGENTA_EX}{token}")
    elif "PASSWORD_DOES_NOT_MATCH" in req.text:
        print(f'\n{Fore.WHITE}[ {Fore.RED}-{Fore.WHITE} ] Invalid Password')    
    elif "captcha-required" in req.text:
        print(f'\n{Fore.WHITE}[ {Fore.RED}-{Fore.WHITE} ] Discord Returned Captcha{Fore.RED},{Fore.WHITE} Try Again')   
    else:
        print(f'{Fore.WHITE}[ {Fore.RED}-{Fore.WHITE} ] Error{Fore.RED},{Fore.WHITE} Try Again ')
if __name__ == "__main__":
    os.system("cls")
    os.system("title Discord token by : @ilord4tb - Lord4tb .#4465")
    print(f"{Fore.WHITE}[ {Fore.LIGHTMAGENTA_EX}*{Fore.WHITE} ] Discord token {Fore.LIGHTMAGENTA_EX}>{Fore.WHITE} by : {Fore.LIGHTMAGENTA_EX}@{Fore.WHITE}ilord4tb {Fore.LIGHTMAGENTA_EX}-{Fore.WHITE} Lord4tb .{Fore.LIGHTMAGENTA_EX}#4465{Fore.WHITE}\n")
    email = input(f"{Fore.WHITE}[ {Fore.LIGHTMAGENTA_EX}+{Fore.WHITE} ] Enter your email :{Fore.LIGHTMAGENTA_EX} ")
    password = input(f"{Fore.WHITE}[ {Fore.LIGHTMAGENTA_EX}+{Fore.WHITE} ] Enter password :{Fore.LIGHTMAGENTA_EX} ")
    token(email, password)