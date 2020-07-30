import os
str2 = "19921003"
str3 = "12.nc"
try:
    str4 = "rsync -avzh /mnt/podaac_drive/allData/merged_alt/L4/cdr_grid/ssh_grids_v1812_"+str2+str3 +" /home/rghoshal/Desktop/ugpcode/"
    os.system(str4)    