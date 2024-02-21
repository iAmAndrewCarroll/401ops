# Ops Challenge 33

Ops Challenge 33 is designed to interact with the VirusTotal API for malware detection and analysis. The project includes a main script (`the-demo-33.py`) that interfaces with `virustotal-search.py`, allowing users to query the VirusTotal database with specific file hashes.

## Setup

Before running the scripts, ensure the following setup steps are completed:

1. **Python Environment**: Ensure Python 3 is installed on your system.

2. **VirusTotal API Key**: Obtain a free API key from [VirusTotal](https://virustotal.com).

3. **Environment Variable Setup**: 
   - Create a `.env` file in the same directory as the scripts.
   - Add your VirusTotal API key to the `.env` file in the format:
     ```
     API_KEY_VIRUSTOTAL=your_virustotal_api_key_here
     ```

4. **Dependencies**: 
   - Install required Python packages (if any, such as `requests` for `virustotal-search.py`):
     -  `pip install requests`

## Scripts

### `the-demo-33.py`

This script is the primary interface for the challenge. It constructs and executes a command to run `virustotal-search.py` with the necessary parameters.

#### Usage

To run the script with a specific hash:
```
./the-demo-33.py <hash_value>
```

If no hash is provided, the script will use a default hash.

### `virustotal-search.py`

This script, obtained from the provided GitHub repository, handles querying the VirusTotal API. It is executed by `the-demo-33.py` and should not be run directly unless for testing individual functionality.

## Running the Project

Navigate to the project directory and run the following command to check a hash against the VirusTotal database:

```
./the-demo-33.py <hash_value>**
```

Replace `<hash_value>` with the hash you want to check. If you don't provide a hash, the script will use a default value.

## Notes

- Ensure both scripts (`the-demo-33.py` and `virustotal-search.py`) are in the same directory.
- The scripts should have execution permissions. Use `chmod +x` if necessary.
- Keep your API key confidential and do not share the `.env` file.
