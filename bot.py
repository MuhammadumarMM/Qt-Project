import requests

result = requests.get("https://random.dog/woof.json")

dog_url = result.json()['url']

with open("dog.jpg",'bw') as fl:
  dog = requests.get(dog_url)
  fl.write(dog.content)

# import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('dog.jpg', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'XmsYYowA8WJBfTUyf3WbFuXS'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)