import os
from dotenv import load_dotenv

print(os.getenv("EMAIL"))

# settings.py
#load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

print(os.getenv("EMAIL"))
print(os.getenv("DATABASE_PASSWORD"))