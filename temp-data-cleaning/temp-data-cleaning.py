#!/usr/bin/env python3
import os
import sys
import time
import schedule

def dataops_upload_cleaning():
    print("Cleaning Dataops failed upload job file:")
    os.system('find /tmp/dataops/ ! -path /tmp/dataops/ -mtime +1 -type d | xargs rm -rf')
    print("Done")

schedule.every().day.at("23:00").do(dataops_upload_cleaning)

while True:
    schedule.run_pending()
    time.sleep(1)

