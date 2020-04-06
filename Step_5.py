# Import Amphora librarys
from amphora.client import AmphoraDataRepositoryClient, Credentials
import amphora_api_client as a10a
from amphora_api_client.rest import ApiException
from amphora_api_client.configuration import Configuration

# Import non-Amphora librarys
from array import array 
import os
import numpy as np
import time
from datetime import datetime, timedelta


# Login to amphoradata.com
credentials = Credentials(username=os.getenv('username'), password=os.getenv('password'))
client = AmphoraDataRepositoryClient(credentials)
amphora_api = a10a.AmphoraeApi(client.apiClient)

# Get existing Amphora ID
File_object = open("Amphora_id.txt","r") 
Amphora_id = File_object.read()
File_object.close()


# Define model function
def time_product(date_time_obj):
  time_hour = date_time_obj.hour
  time_minute = date_time_obj.minute
  time_second = date_time_obj.second

  time_prod = time_hour * time_minute * time_second
  
  return time_prod

#####################################

# Run model
time_now = datetime.utcnow()
time_prod = time_product(time_now)

# Now create signal 
signalStore=[]
signalStore.append({"t": time_now, "timeProduct": time_prod})

# Push signal
amphora = client.get_amphora(Amphora_id)
amphora.push_signals_dict_array(signalStore)
