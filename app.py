from dotenv import load_dotenv
load_dotenv()

import os


password = os.getenv('PASSWORD')
password_BLAH = os.getenv('BLAH')

print(password)
print(password_BLAH)