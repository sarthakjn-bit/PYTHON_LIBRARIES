# ## GET METHOD IN REQUESTS REQUESTS
# import requests
# r = requests.get('https://httpbin.org/get' , params={'a':10 , 'value':'saarthak'})
# print("  GET METHOD OUTPUT ")

# print(f"status code{ r.status_code}")
# print(r.text)
# print(r.headers)
# print(r.json(), type(r.json()))
# print(r.encoding)
# print(r.url) 

# ## POST METHOD IN REQUEST REQUESTS
# import requests

# payload={
#     'id': 100 ,
#     'user': "saarthak"
    
# }
# r = requests.post("https://httpbin.org/post" , json=payload)
# print("POST METHOD")

# print(f"status code{ r.status_code}")
# print(r.text)
# print(r.headers)
# print(r.json(), type(r.json()))
# print(r.encoding)
# print(r.url) 



# ## PUT METHOD IN REQUESTS REQUESTS
# import requests
# r = requests.put('https://httpbin.org/put' , params = {'key':'ethical' ,'value':'hacker' })

# print("PUT METHOD ")
# print(r.status_code)
# print(r.headers)
# print("**")
# print(r.text)
# print(r.url)

# ## DELETE METHOD IN REQUESTS
# import requests
# r = requests.delete("https://httpbin.org/delete" , params={'id':100,'users':'saarthak'})
# print("DELETE METHOD")

# print(r.text)
# print(f"status code{ r.status_code}")
# print(r.headers)
# print(r.json(), type(r.json()))
# print(r.encoding)
# print(r.url) 

