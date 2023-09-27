import os
import warnings
warnings.simplefilter("ignore")

directory = r"E:"

key_path = os.path.join(directory,"openapikey.txt")

try:
    with open(key_path,"r") as f:
        openapi_key = f.read()
        print(openapi_key)
except FileNotFoundError:
    print(f"{key_path} not found")
except Exception as e:
    print(f"An error occured {e}")
    
os.environ['OPENAI_API_KEY'] = openapi_key