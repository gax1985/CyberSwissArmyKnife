#!/usr/bin/env python3
"""
Langflow API Trigger & Debugging Probe
--------------------------------------
This script acts as a REST API client to manually trigger a local Langflow pipeline.
It reads a local text document, formats it into a JSON payload, and POSTs it to
the Langflow execution endpoint. It includes robust error handling to differentiate
between connection failures and internal server errors.

USAGE:
    python trigger_langflow.py <FLOW_ID> <DOCUMENT_PATH>

EXAMPLE:
    python trigger_langflow.py my-flow-uuid-123 "Source-Documents/my_document.txt"
"""

# 'json' is used to convert Python dictionaries into JSON strings (and vice versa) for web APIs.
import json

# 'sys' allows us to interact with the underlying system, primarily to read command-line arguments and exit.
import sys

# 'urllib.request' is Python's built-in module for opening HTTP URLs.
# OPTION: Many teams prefer the third-party 'requests' library (e.g., requests.post())
# because it is less verbose, but using 'urllib' means this script requires ZERO external dependencies to run in NixOS/WSL.
import urllib.request

# We import specific error classes to handle network failures gracefully.
from urllib.error import URLError, HTTPError

# ==========================================
# CONFIGURATION
# ==========================================
# The base URL for your local Langflow instance.
BASE_URL = "http://localhost:7860"


def run_flow(flow_id: str, document_path: str):
    """
    Triggers a Langflow flow with the content of a specified document.

    Args:
        flow_id (str): The UUID of the Langflow flow to run.
        document_path (str): The local file path of the document to inject.
    """
    # Construct the full API URL from the base and the flow_id.
    langflow_api_url = f"{BASE_URL}/api/v1/run/{flow_id}"

    print(f"[*] Initializing trigger for document: '{document_path}'")
    print(f"[*] Target Langflow API: {langflow_api_url}")

    # ==========================================
    # PHASE 1: DATA INGESTION
    # ==========================================
    try:
        # We open the file in 'r' (read) mode with utf-8 encoding to prevent issues with special characters.
        # OPTION: If you were uploading images or PDFs, you would use 'rb' (read binary) mode.
        with open(document_path, 'r', encoding='utf-8') as file:
            # .read() loads the entire file into memory as a single string.
            document_text = file.read()
            print(f"[+] Successfully loaded document ({len(document_text)} characters).")

    except FileNotFoundError:
        # If the file isn't in the same directory as the script, we catch the error, warn the user, and exit cleanly.
        print(f"\n[!] CRITICAL: Document not found at '{document_path}'.")
        print("[!] Hint: Ensure the path is correct and you are running the script from the project root.")
        sys.exit(1)  # Exit code 1 signals to the OS (or Jenkins/GitLab) that the script failed.

    # ==========================================
    # PHASE 2: PAYLOAD CONSTRUCTION
    # ==========================================

    # Langflow expects a specific JSON schema. The 'input_value' is the actual data we are passing.
    # The 'output_type' and 'input_type' tell Langflow to treat this as a standard chat interaction.
    # OPTION: You can inject overriding variables into specific nodes using a "tweaks" dictionary here.
    payload = {
        "input_value": document_text,
        "output_type": "chat",
        "input_type": "chat"
    }

    # APIs communicate in bytes. json.dumps() turns the Python dict into a JSON string.
    # .encode('utf-8') converts that string into raw bytes ready to be sent over the network.
    data = json.dumps(payload).encode('utf-8')

    # We construct the HTTP request.
    # CRITICAL: Because we include the 'data=' parameter, urllib automatically makes this a POST request instead of a GET request.
    # We must explicitly set the 'Content-Type' header to 'application/json' so Langflow knows how to parse our bytes.
    req = urllib.request.Request(langflow_api_url, data=data, headers={'Content-Type': 'application/json'})

    print(f"[*] Pinging Langflow API...")

    # ==========================================
    # PHASE 3: EXECUTION & DEBUGGING
    # ==========================================
    try:
        # We fire the request.
        # OPTION: You can add 'timeout=10' inside urlopen() to ensure the script doesn't hang forever if the server is unresponsive.
        with urllib.request.urlopen(req) as response:

            # .getcode() grabs the HTTP status (e.g., 200 means OK, 201 means Created).
            status = response.getcode()
            print(f"[+] HTTP Status: {status} OK")

            # The server responds with bytes. We read them and decode them back into a utf-8 string.
            raw_response = response.read().decode('utf-8')

            # We parse the JSON string back into a workable Python dictionary.
            result = json.loads(raw_response)

            print("\n[+] Langflow Execution Complete. Raw Output snippet:")
            # We print just the first 500 characters of the formatted JSON so we don't flood the terminal.
            print(json.dumps(result, indent=2)[:500] + "\n...\n")
            print("[*] Check your OpenClaw directory for the SKILL.md file!")

    except HTTPError as e:
        # HTTPError catches responses where the server is ALIVE, but rejected our request.
        # Examples: 404 (Wrong URL UUID), 422 (Bad JSON Schema), 500 (Python crashed inside a Langflow node).
        print(f"\n[!] HTTP Error: {e.code} - {e.reason}")

        # We read the error body because Langflow often sends back a detailed JSON explanation of exactly which node failed.
        error_body = e.read().decode('utf-8')
        print(f"[!] Langflow Server returned: {error_body}")
        print("[!] Hint: Check the VSCodium terminal where Langflow is running for the Python traceback.")
        sys.exit(1)

    except URLError as e:
        # URLError catches routing issues where the script couldn't even reach the server.
        # Examples: Langflow isn't running, wrong port number, or DNS failures.
        print(f"\n[!] URL Error (Connection Failed): {e.reason}")
        print("[!] Hint: Is Langflow actually running on port 7860?")
        sys.exit(1)

    except Exception as e:
        # A generic catch-all for anything else (e.g., out of memory, keyboard interrupts).
        print(f"\n[!] Unexpected Runtime Error: {e}")
        sys.exit(1)


# This standard Python idiom ensures the code only runs if the script is executed directly.
if __name__ == "__main__":
    # We check sys.argv to see if the user provided the required command-line arguments.
    # sys.argv[0] is the script name itself, so we expect a total length of 3.
    if len(sys.argv) != 3:
        print("="*60)
        print(" Langflow Trigger Script - USAGE ERROR")
        print("="*60)
        print("\nThis script requires two command-line arguments to run:")
        print("  1. The Flow ID (UUID) of your Langflow pipeline.")
        print("  2. The path to the local text document to process.\n")
        # The f-string below gets the script name dynamically.
        print(f"Usage:\n  python {sys.argv[0]} <FLOW_ID> <DOCUMENT_PATH>\n")
        print("Example:\n  python trigger_langflow.py 1a2b3c-4d5e-6f7g-8h9i-j0k1l2m3n4o5 \"Source-Documents/pentest_log_01.txt\"")
        print("\n" + "="*60)
        sys.exit(1)

    # If the arguments are correct, we unpack them into variables.
    flow_id_arg = sys.argv[1]
    document_path_arg = sys.argv[2]

    # We pass the command-line arguments directly to our main function.
    run_flow(flow_id=flow_id_arg, document_path=document_path_arg)