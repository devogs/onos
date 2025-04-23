# ONOS Application Activation Script

This Python script facilitates the activation of ONOS applications using the northbound REST API.  It reads application information from a JSON file and activates those with the state "ACTIVE". Configuration parameters (IP address, port, etc.) are loaded from a `.env` file for improved management and security.

## Prerequisites

* Python 3.6 or higher
* Python libraries: `requests`, `python-dotenv`
* A JSON file containing ONOS application information (e.g., `applications.json`)
* A running ONOS instance

## Installation

1.  **Clone the repository (or download the code)**

    If you've cloned this repository, proceed to the next step. If you've downloaded the code, ensure you have all the necessary files (`app_activation.py`, `applications.json`).

2.  **Create a virtual environment (recommended)**

    It's highly recommended to work within a virtual environment to isolate project dependencies.

    ```bash
    python3 -m venv venv      # Create a virtual environment named "venv"
    source venv/bin/activate  # Activate the environment (Linux/macOS)
    venv\Scripts\activate      # Activate the environment (Windows)
    ```

3.  **Install dependencies**

    Install the required Python libraries using `pip`:

    ```bash
    pip install requests python-dotenv
    ```

## Configuration

1.  **Create a `.env` file**

    Create a file named `.env` in the same directory as your Python script (`app_activation.py`). This file will hold the configuration settings for your ONOS instance.

2.  **Set environment variables**

    Add the following variables to your `.env` file, replacing the placeholder values with the actual information for your ONOS setup:

    ```
    ONOS_IP=your_onos_ip        # IP address of your ONOS instance (e.g., 192.168.1.10)
    ONOS_PORT=8181               # ONOS REST API port (default is 8181)
    ONOS_USER=your_onos_user     # Username for ONOS authentication (e.g., onos)
    ONOS_PASSWORD=your_onos_password   # Password for ONOS authentication (e.g., rocks)
    JSON_FILE_PATH=applications.json  # Path to your JSON file (leave "applications.json" if it's in the same directory)
    ```

    **⚠️  Important (Security):**

    * Never commit your `.env` file containing sensitive information (like passwords) to a public repository. If you're using a public repository, consider alternative methods for secret management (system environment variables, secrets vaults, etc.).

## Usage

1.  **Execute the script**

    Once you've configured the `.env` file and are within the virtual environment (if used), run the Python script:

    ```bash
    python3 app_activation.py
    ```

    The script will:

    * Load configuration variables from the `.env` file.
    * Read application information from the JSON file (`applications.json`).
    * Iterate through the list of applications.
    * Activate applications with the state "ACTIVE" using the ONOS REST API.
    * Display success or error messages for each activation attempt.

## Error Handling

The script includes error handling for:

* Missing files (`applications.json` or `.env`).
* JSON format errors in `applications.json`.
* Connection errors to the ONOS API.
* Missing or incorrect values in the `.env` file.

## Example `applications.json` File

```json
{
  "applications": [
    {
      "name": "org.onosproject.lldp",
      "state": "ACTIVE"
    },
    {
      "name": "org.onosproject.openflow",
      "state": "INSTALLED"
    },
    {
      "name": "org.onosproject.drivers.bmv2",
      "state": "ACTIVE"
    }
  ]
}