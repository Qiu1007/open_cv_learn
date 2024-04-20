import time
from datetime import datetime 
time_Str=time.time()
date_str=datetime.timestamp(datetime.now())
print("time    ",time_Str)
print("datetime",date_str)