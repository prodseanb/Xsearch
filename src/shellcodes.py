import csv
import io
import urllib.request

url = 'https://raw.githubusercontent.com/offensive-security/exploitdb/master/files_shellcodes.csv'
webpage = urllib.request.urlopen(url)
reader = csv.reader(io.TextIOWrapper(webpage))

for row in reader:
    print(", ".join(row))