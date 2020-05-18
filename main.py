import requests

url_data = "https://sheetdb.io/api/v1/xr0f4qkl7w06c"
url_ans = "https://sheetdb.io/api/v1/ofsmne5uzeyh7"
r = requests.get(url=url_ans)
data = r.json()
print(data, '\n')

# questions = requests.get(url=url_ans).json()
# print(questions)

