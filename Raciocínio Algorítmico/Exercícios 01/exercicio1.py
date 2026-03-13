# I searched for the library to extract the current datetime
import datetime
current_datetime = datetime.datetime.now().year


def calculate_age(birth_year):
    age = current_datetime - birth_year
    return age


print (r"""    ___      _         _         _                   _       _    _         _     
  / __|__ _| |__ _  _| |__ _ __| |___ _ _ __ _   __| |___  (_)__| |__ _ __| |___ 
 | (__/ _` | / _| || | / _` / _` / _ \ '_/ _` | / _` / -_) | / _` / _` / _` / -_)
  \___\__,_|_\__|\_,_|_\__,_\__,_\___/_| \__,_| \__,_\___| |_\__,_\__,_\__,_\___|
  """)
birth_year = int(input("Digite o seu ano de nascimento: "))
print (f"Sua idade é: {calculate_age(birth_year)} anos")