import re
import sys
import requests
import pandas as pd
from google.colab import files

url = sys.argv[1]
file_name = sys.argv[2]

website = requests.get(url)
html = website.text

emails = re.findall(r'[\w\.-]+@[\w\.-]+', html)

# Converting into csv format using panda libs
df = pd.DataFrame(emails, columns=["Email"])
df.to_csv('email.csv', index=False)

# Saving the emails into the csv at provided location.
files.download(file_name)