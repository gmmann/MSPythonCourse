# # # .env file
# # DATABASE = Sample Connection String


# app.py
from dot_env import load_dotenv
import os
load_dotenv()
database = os.getenv('DATABASE')
print(database)