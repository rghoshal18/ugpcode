# Script for downloading ssh_grid data
import os
from datetime import date
from datetime import timedelta
curr = date(1993,1,5)
str1 = "rsync -avzh /mnt/podaac_drive/allData/merged_alt/L4/cdr_grid/ssh_grids_v1812_"
str2 = "12.nc /media/rghoshal/D4A6E10AA6E0EE44/UGP"
while curr< date(1996,1,1):
    str3 = str1 + ''.join(e for e in str(curr) if e.isalnum()) + str2
    try:
        os.system(str3)
        curr += timedelta(days=30)
    except:
        pass