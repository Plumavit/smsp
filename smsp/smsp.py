import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '+56934034263',
  'message': 'Hello world',
  'key': 'textbelt',
})
print(resp.json())
