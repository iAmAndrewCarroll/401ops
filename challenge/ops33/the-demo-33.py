#!/usr/bin/env python3

# The below demo script works in tandem with virustotal-search.py from https://github.com/eduardxyz/virustotal-search, which must be in the same directory.
# Set your environment variable first to keep it out of your script here.

import os
from dotenv import load_dotenv

load_dotenv()
# print("Loaded API Key: ", os.getenv('API_KEY_VIRUSTOTAL'))

apikey = os.getenv('API_KEY_VIRUSTOTAL') # Set your environment variable before proceeding. You'll need a free API key from virustotal.com so get signed up there first.
hash = 'D41D8CD98F00B204E9800998ECF8427E' # Set your hash here. 

# print("API Key: ", apikey)

# This concatenates everything into a working shell statement that gets passed into virustotal-search.py
query = 'python3 /Users/andrewcarroll/401ops/challenge/ops33/virustotal-search.py -k ' + str(apikey) + ' -m ' + str(hash)

# print("Executing Command: ", query)

os.system(query)