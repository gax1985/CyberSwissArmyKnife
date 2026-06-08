"""

Hello, dearest reader!

This Python application aims to win the hearts and mostly the minds of yourselves, dearest users. The way it does this
is by completing the following :
1. a Langflow endpoint is located, and specified.
2. A JSON Payload inside of a Header is created for the Langflow API
3. The header gets sent to the Langflow API
4. ... a Response is received!
"""
# Now, let us start with the fun! Let us begin with importing the libraries we need for this task :

"""
A Library to help shut down the script gracefully :
"""
import sys
"""
... a library for handling .JSON files : 
"""

import json

"""
... a library for handling HTTP requests and HTTP errors :
"""
import urllib.request
import urllib.error

########################################################################################################################

## Now, we proceed with the creation of our variables, which will contain :

base_url = "http://localhost:7860"
flow_id  = "2420bba8-da64-48e3-8cc3-f11ecc8babd4"
api_endpoint = f"{base_url}/api/v1/run/{flow_id}"



class ThePioneer():
    def __init__(self):
        pass




class TheNetRequester:
    def __init__(self):
        pass

    def send_payload(self, data_bytes, endpoint_url):
        print(f"[*] Firing payload to Langflow API...")

        # Your newly minted Langflow API Key
        langflow_api_key = "sk-w4LPxywbhMcRshVFVfS3IB4BMyKWT_sLB6yvHGLy54k"

        # We inject the Authorization badge into the headers
        headers = {
            "Content-Type": "application/json",
            "x-api-key": langflow_api_key
                    }

        ## ... next, we create a Request object, defining the URL, data, and headers
        req = urllib.request.Request(url=endpoint_url, data=data_bytes, headers=headers)

        ## We create a Try statement in order to facilitate debugging :
        try:
            with urllib.request.urlopen(req) as response:
                response_data = json.loads(response.read().decode("utf-8"))
                print(f"[+] PIPELINE SUCCESS!")
                return response_data

        except urllib.error.HTTPError as e:
                print(f"[-] HTTP Error: {e.code} - {e.reason}")
                error_body = e.read().decode('utf-8')
                print(f"Error Body: {error_body}")
                sys.exit(1)

        except urllib.error.URLError as e:
            # - This catches Network errors (like Langflow being turned off)
            print(f"[-] NETWORK FAILURE: {e.reason}")
            sys.exit(1)




def main():

    # Let us do TheNetRequester Class instance :
    net_requester = TheNetRequester()
    goods = {
        "input_value": "EXECUTE PIPELINE",
        "output_type": "chat",
        "input_type": "chat"
    }
    packed_goods = json.dumps(goods).encode("utf-8")
    request = net_requester.send_payload(packed_goods,api_endpoint)
    print(f"{request}")






if __name__ == "__main__":
    main()
