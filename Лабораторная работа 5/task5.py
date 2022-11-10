import random

def get_random_password() -> str:
   len_ = 8
   ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
   ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   digits = '0123456789'
   variety = ascii_lowercase + ascii_uppercase + digits
   password = ''.join(random.sample(variety, len_))
   return password

print(get_random_password())
