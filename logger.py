#!/usr/bin/env python3

from datetime import datetime
# datetime object containing current date and time

def logger(data):
    now = datetime.now()
    now = now.strftime('%d/%m/%Y %H:%M:%S')

    with open('temp_logs.log', 'a+') as log:
        data = (now + '\t' + str(data) + '\n')
        log.write(data)