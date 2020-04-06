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
credentials = Credentials(username==os.getenv('username'), password=os.getenv('password')) 
client = AmphoraDataRepositoryClient(credentials)
amphora_api = a10a.AmphoraeApi(client.apiClient)
