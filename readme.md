# Instruction

## Install Dependencies
you can install the dependencies by running this command 
>pip install -r requirements.txt

## Run Django
>python manage.py runserver 0:8000

## Generate Client_ID and client_secret
before you register app to get client_id and client_secret, you have to log in as user, you can create user by following command
>python manage.py createsuperuser

after that, you can login to the application with following URL
>http://localhost:8000/admin

then, to generate client id you can follow the URL
>http://localhost:8000/o/applications

now, you can retrieve the client_id and client_secret to get the token

## Register new user using API
to create new user, you can follow this url (you can use postman or Curl)
using POST :
>http://localhost:8000/authentication/register

request body :
  * username : <:your username>
  * password : <:your password>
  * client_id : <client_id>
  * client_secret : <client_secret>

if the request success, you will get the token to request data.

## Get Token
using POST :
>http://localhost:8000/authentication/token
request body :
  * username : <:your username>
  * password : <:your password>
  * client_id : <client_id>
  * client_secret : <client_secret>

## Refresh Token
using POST :
>http://localhost:8000/authentication/token/refresh
request body :
  * refresh_token : <refresh token>
  * client_id : <client_id>
  * client_secret : <client_secret>
 
## Revoke Token
using POST :
>http://localhost:8000/authentication/token/refresh
request body :
  * refresh_token : <refresh token>
  * client_id : <client_id>
  * client_secret : <client_secret>
   
   
  
 

