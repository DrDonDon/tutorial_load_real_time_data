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

# Define model function
def time_product(date_time):
  time_hour = date_time.hour
  time_minute = date_time.minute
  time_second = date_time.second

  time_prod = time_hour * time_minute * time_second
  
  return time_prod

#####################################

# Run model
time_now = date_time.utcnow()
time_prod = time_product(time_now)

# Create Amphora
# Define metadata for Amphora
sep=" "
amphora_description = "This is an Amphora for a tutorial on how to make Amphoras"
amphora_tnc = "Creative_Commons_4p0"
amphora_name = "Tutorial: How to make and upload an Amphora"
amphora_labels = ["tutorial,timeseries"]
amphora_price = 0   # Monthly price of Amphora
amphora_lat = -27.45714
amphora_lon = 153.07106

## Create an Amphora 
amphora = client.create_amphora(name = amphora_name, lat = amphora_lat, lon = amphora_lon, 
                         price = amphora_price, description = amphora_description, 
                         terms_and_conditions_id = amphora_tnc, labels = amphora_labels)

# Save Amphora ID for later
File_object = open("Amphora_id.txt","w") 
File_object.write(amphora.amphora_id)
File_object.close()

# Now create signal 
amphora.create_signal("timeProduct",attributes = {"units": "HMS"})
signalStore=[]
signalStore.append({"t": time_now, "timeProduct": time_prod})

# Push signal
amphora.push_signals_dict_array(Signals) 
