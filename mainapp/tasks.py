
import csv
import random
from datetime import time
from subprocess import PIPE, Popen

from celery import shared_task
from django.db import connection


@shared_task(bind=True)
def run_script1_and_save_output(self):
    
    arg1 = random.randint(1, 9)
    arg2 = random.randint(1, 9)
    print(arg1)
    print(arg2)
    process = Popen(['python', 'myscripts.py',str(arg1),str(arg2)], stdout=PIPE)
    output, error = process.communicate() # Get the script's output

    # Parse the CSV data and extract the columns you need
    csv_data = output.decode()
    csv_reader = csv.reader(csv_data.split('\n'))
    print(csv_reader)
    # for row in csv_reader:
        # col1 = 1
        # col2 = 2
        # ...
    col1 = 1
    col2 = 2
        # Save the extracted data to a database
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO myproject (one,two) VALUES (%s, %s)", [col1, col2])
    return 'Done'
