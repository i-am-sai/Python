import requests

response = requests.get("https://loans.zerodhacapital.com/")

print(response.status_code) # 200
print(response.headers) # response headers

# print(response.json()) # response body parsed as JSON

# POST request — send data
# payload = {"name": "test-repo", "private": False}
# headers = {"Authorization": "Bearer your_token_here"}

# response = requests.post(
#     "https://api.github.com/user/repos",
#     json=payload,
#     headers=headers
# )
# print(response.status_code)     # 201 Created

