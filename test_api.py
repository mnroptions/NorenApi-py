from api_helper import NorenApiPy
import logging

#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#credentials
user    = "POORNA"
pwd     = "3906e2afbfffe683f5d80264e7e5c3511c18215beade570067f5d44d0e3bf7a4"
factor2 = "AAAAA1234A"
vc      = "NOREN_WEB"
app_key = "1.0.9"
imei    = "ag3tbbbb33"

#make the api call
ret = api.login(userid=uid, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)

print(ret)

