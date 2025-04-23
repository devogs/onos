import json
import requests
import codecs
from dotenv import load_dotenv
import os

def activate_onos_applications(json_file_path, onos_ip, onos_port, onos_user, onos_password):
    """
    Reads a JSON-like file with potential encoding issues, activates ONOS applications.
    """

    try:
        # 1. Read the file, trying different encodings
        file_content = None
        possible_encodings = ['utf-8', 'latin-1', 'iso-8859-1']
        for encoding in possible_encodings:
            try:
                with open(json_file_path, 'r', encoding=encoding) as f:
                    file_content = f.read()
                print(f"File read successfully with encoding: {encoding}")
                break
            except UnicodeDecodeError:
                print(f"Failed to read with encoding: {encoding}")

        if file_content is None:
            print("Error: Could not read file with any of the tried encodings.")
            return

        # 2. Replace the problematic sequence
        file_content = file_content.replace("\\µ", "")

        # 3. Parse the JSON
        data = json.loads(file_content)

    except FileNotFoundError:
        print(f"Error: File not found: {json_file_path}")
        return
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format: {e}")
        return

    base_url = f"http://{onos_ip}:{onos_port}/onos/v1/applications"

    for app in data.get("applications", []):
        if app.get("state") == "ACTIVE":
            app_id = app.get("name")
            if app_id:
                activate_url = f"{base_url}/{app_id}/active"
                try:
                    response = requests.post(
                        activate_url,
                        auth=(onos_user, onos_password)
                    )
                    response.raise_for_status()
                    print(f"Successfully activated application: {app_id}")
                except requests.exceptions.RequestException as e:
                    print(f"Error activating application {app_id}: {e}")
            else:
                print("Warning: Application found with 'ACTIVE' state but missing 'name'.")

if __name__ == "__main__":
    load_dotenv()  # Load variables from .env

    onos_ip = os.getenv("ONOS_IP")
    onos_port = os.getenv("ONOS_PORT")
    onos_user = os.getenv("ONOS_USER")
    onos_password = os.getenv("ONOS_PASSWORD")
    json_file_path = os.getenv("JSON_FILE_PATH")

    # Basic error handling to ensure required variables are loaded
    if not all([onos_ip, onos_port, onos_user, onos_password, json_file_path]):
        print("Error: Not all required environment variables are set in .env file.")
        print("Please check your .env file and ensure ONOS_IP, ONOS_PORT, ONOS_USER, ONOS_PASSWORD, and JSON_FILE_PATH are defined.")
        exit(1)  # Exit the script with an error code

    try:
        onos_port = int(onos_port)  # Convert ONOS_PORT to integer
    except ValueError:
        print(f"Error: Invalid ONOS_PORT value: {onos_port}.  Please ensure it is an integer.")
        exit(1)

    activate_onos_applications(json_file_path, onos_ip, onos_port, onos_user, onos_password)