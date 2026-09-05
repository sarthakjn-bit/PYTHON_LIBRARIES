## REQUEST LIBRARY IN PYTHON
 ** Request Library In Python -   used to send Http request to website and ** communicate with APIs and WEBSITE** . 

** WE USE MULTIPLE HTTP METHOD 
   -> GET METHOD 
   -> POST METHOD
   -> PUT METHOD 
   -> DELETE METHOD 

** PARAMETERS AND PAYLOADS 
 -> PARAMATERS - ARE THE STRING OR INPUT STRING USED IN URL FOR SENDING DATA TO SERVER . 
 -> PAYLOADS - ARE THE DATA USED TO SEND IN JSON BODY TO SERVER .

 ** COOKIES , SESSION , AUTHENTICATION

 ->COOKIES - COOKIES ARE THE SMALL PEICE OF DATA SENT BY THE SERVER AND STORE IN USER BROWSER . 
 ->SESSION -  MAINTAINS STATE BETWEEN MULTIPLE REQUESTS, USUALLY USING COOKIES . (USUALLY SESSION ID USED)
 ->AUTHENTICATION - AUTHENTICATION IS THE SECURITY MEASURE USED BY APPLICATION TO VALIDATE USER 

 ** PROPERTIES  USED IN REQUEST ARE 

 1. response.url            - show url 
 2. response.STATUS_CODE    - show http status
 3. response.JSON()         - show response in json parse format
 4. response.TEXT           - show response in body as text format 
 5. response.HEADERS        - show reesponse  header
 6. response.encoding       - show encoding type


** FUNCTION USED IN REQUESTS 
1. requests.post()
2. requests.put()
3. requests.delete()
4. requests.get()
5. requests.Session()
   
