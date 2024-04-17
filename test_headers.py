import requests

url = "https://www.google.com"
response = requests.head(url)
print(response.headers) # prints the entire header as a dictionary
#print(response.headers["Content-Length"]) # prints a specific section of the dictionary
print('***')
url = "https://raw.githubusercontent.com/jlhumbe/example_data/main/testfile.json"
response = requests.head(url)
print(response.headers) # prints the entire header as a dictionary
#print(response.headers["Content-Length"]) # prints a specific section of the dictionarybreakpoint()
