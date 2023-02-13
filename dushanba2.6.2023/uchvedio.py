import requests
data={
    'q':'Andijon'
}
res=requests.get("https://www.google.com/search?q",params=data)
print(res.text)