import requests

url = "http://www.omdbapi.com/?i=tt3896198&apikey=72016fef"

print(requests.get(url).text)
