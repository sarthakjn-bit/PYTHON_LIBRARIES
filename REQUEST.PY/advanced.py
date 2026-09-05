import requests

s = requests.Session()

# Server sets a cookie
s.get("https://httpbin.org/cookies/set/session_id/aab1123")

# Session has stored the cookie
print(s.cookies)

# Send the cookie back to the server
r = s.get("https://httpbin.org/cookies")

print(r.json())




# # ## AUTHENTICATION IN REQUEST 
# import requests
# r = requests.get('https://httpbin.org/get' , auth=("saa", "0909"))
# print("AUTHENTICATION ")
# print(r.status_code)
# print(r.json())