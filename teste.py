import google.generativeai as genai

genai.configure(api_key="AIzaSyBtW3EGR3ORXazqo1rxz9V9GSIOFYnDrOY")

for m in genai.list_models():
    print(m.name)