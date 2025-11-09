import os
import zipfile
import sys
import argparse

parser = argparse.ArgumentParser() 
parser.add_argument("-1", "--zippedfile", required=True, help="Zipped file")
args = vars(parser.parse_args())

zip_file = args['zippedfile']
file_name = zip_file

if os.path.exists(zip_file) == False:
    sys.exit("No such file exist in Dir")

def extract(zip_file):
    file_name = zip_file.split(".zip")[0]
    if zip_file.endswith(".zip"):

        curretn_working_dir = os.getcwd()
        new_dir = curretn_working_dir + "/" + file_name
        
        with zipfile.ZipFile(zip_file, 'r') as zip_object:
            zip_object.extractall(new_dir)
        print("Extract Done!")
    else:
        print("Not a zip file")

extract(zip_file)
