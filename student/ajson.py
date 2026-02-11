import json

json_string = '''
{
    "id": 1,
    "title": "The Great Gatsby"
}
'''


book = json.loads(json_string)

print(book['title'])
print(book)