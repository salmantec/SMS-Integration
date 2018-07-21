import urllib # Python URL functions
import urllib2 # Python URL functions

authkey = "" # Your authentication key.

mobiles = "9123456713" # Multiple mobiles numbers separated by comma.

message = "In this message Am using msg91 api" # Your message to send.

sender = "Salman" # Sender ID,While using route4 sender id should be 6 characters long.

route = "4" # Define route

# Prepare you post parameters
values = {
                  'authkey' : authkey,
                  'mobiles' : mobiles,
                  'message' : message,
                  'sender' : sender,
                  'route' : route
                  }
url = "" # msg91 API URL

postdata = urllib.urlencode(values) # URL encoding the data here.

req = urllib2.Request(url, postdata)

response = urllib2.urlopen(req)

output = response.read() # Get Response

print(output) # Print Response
