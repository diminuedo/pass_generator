import random
import time

a = 'qwertyuiopasdfghjklzxcvbnm'
b = 'QWERTYUIOPASDFGHJKLZXCVBNM'
c = '1234567890'
d = '!@$%^&*()'

all = a + b + c + d
lenght = 8
password = "".join(random.sample(all,lenght))
print('Идет генерация пароля...')
time.sleep(3)
print(password)

input()
