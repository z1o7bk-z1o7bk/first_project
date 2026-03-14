print('Hello from main!')
print(55)

from dotenv import load_dotenv 
import os  

def print_author():
    load_dotenv(dotenv_path='.env')
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}") 
print_author()
