## GET METHOD IN REQUESTS MODULE
import requests
# r = requests.get('https://httpbin.org/get' , params={'a':10 , 'value':'saarthak'})
# print(f"status code{ r.status_code}")
# print(r.text)
# print(r.headers)

# print(r.json(), type(r.json()))
# print(r.encoding)
# print(r.url) 

## PUT METHOD IN REQUESTS MODULE
# import requests
# # R = requests.get('https://httpbin.org/get' , params={'id':10})
# r = requests.put('https://httpbin.org/put' , params = {'key':'ethical' ,'value':'hacker' })
# # if (r.status_code==200):
# #     print("success")
# else:
#     print("failed")
# print(r.status_code)
# print(r.headers)
# print("**")
# print(r.text)
# print(r.url)
# print(R.text)


## POST METHOD 
# payload={
#     'id': 100 ,
#     'user': "saarthak"
    
# }
# r = requests.post("https://httpbin.org/post" , json=payload)
# print(r.text)

##delete 

# r = requests.delete("https://httpbin.org/delete" , params={'id':100,'users':'saarthak'})
# print(r.text)

## cookie in  request 
# s = requests.session()


# r = s.get("https://httpbin.org/cookies/set/session_id/aab1123"  )
# a = {"username":"saarthak" ,"pass":"0909"}
# r1 = s.get("https://httpbin.org/get" , params=a) 
# # print(r.cookies)
# # print(s.cookies)

# print(r1.text)


# import requests

# s = requests.Session()

# # Server sets a cookie
# s.get("https://httpbin.org/cookies/set/session_id/aab1123")

# # Session has stored the cookie
# print(s.cookies)

# # Send the cookie back to the server
# r = s.get("https://httpbin.org/cookies")

# print(r.json())

r = requests.get('https://httpbin.org/get' , auth=("saa", "0909"))
print(r.status_code)
