# Import Amphora librarys
import amphora_client as a10a
from amphora_client.configuration import Configuration
from amphora_extensions.file_uploader import FileUploader

# Import non-Amphora librarys
from array import array 
import os
import numpy as np
import time
from datetime import datetime, timedelta


# Login to amphoradata.com
configuration = Configuration()
configuration.host = "https://app.amphoradata.com"
auth_api = a10a.AuthenticationApi(a10a.ApiClient(configuration))
token_request = a10a.TokenRequest(username=os.getenv('username'), password=os.getenv('password')) 
amphora_api = a10a.AmphoraeApi(a10a.ApiClient(configuration))

# Define model function

# Define create Amphora function

#####################################

# Run model

# Create Amphora
