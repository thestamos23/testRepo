
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
swagger_client.configuration.host = "https://win915.qasymphony.support:8443";
api_instance = swagger_client.LoginApi()
grant_type = 'password' # str | always use <em>grant_type=password</em> (optional) (default to password)
username = 'timtutten@qasymphony.com' # str | Your qTest Manager username (optional)
password = 'T1mmysymphony' # str | Your qTest Manager password (optional)
authorization = 'Basic dHR1dHRlbnFhczo=' # str | Basic + [base64 string of \"<strong>your qTest site name and colon</strong>\"]  Example: qTest Manager site is: apitryout.qtestnet.com then site name is: apitryout + ':', then Authorization is: Basic YXBpdHJ5b3V0Og== (optional)

try: 
    # Log in
    api_response = api_instance.post_access_token(grant_type=grant_type, username=username, password=password, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->post_access_token: %s\n" % e)

