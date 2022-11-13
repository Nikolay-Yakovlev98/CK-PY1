import random
import string
def get_random_password(long_) -> str:

   lowercase = string.ascii_lowercase
   uppercase = string.ascii_uppercase
   digits = string.digits
   variety = uppercase + lowercase + digits
   password = ''.join(random.sample(variety, long_))
   return password

long_password = 8
print(get_random_password(long_password))
