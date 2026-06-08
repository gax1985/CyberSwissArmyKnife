

import json
# Here , we create another class specifically for turning the file's contents to JSON :

class ThePayloadPacker():
    def __init__(self): # This class is responsible for packing the ingested file content into a JSON payload.
        pass

## The following function creates a dictionary for the payload, which will be delivered to the Langflow instance :

    def packed_goodies(self,raw_text):
        print("[*] The Payload Packer is currently working on your Langflow-wrapped JSON schema...")

        payload_dict = {
            "input_value" : raw_text,
            "output_type": "chat",
            "input_type": "chat"
        }

        data_bytes = json.dumps(payload_dict).encode("utf-8")
        return data_bytes


    # Packer = ThePayloadPacker()
    # packed_goods = Packer.packed_goodies(raw_text=precious_contents)
