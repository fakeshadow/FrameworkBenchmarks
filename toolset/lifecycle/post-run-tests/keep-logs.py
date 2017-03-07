#!/usr/bin/python
#
# Archives, to the specified folder, the logged output generated by a benchmark 
# run.  
#
# @author A. Shawn Bandy
import os
import zipfile
import datetime
import shutil
# Follows closely from:
# http://stackoverflow.com/a/34153816
#
# Paths to the log folders are generated by TFB and where those files 
# should be archived.
#
path_in = os.path.abspath(os.path.normpath(os.path.expanduser(os.path.join( \
    os.environ['TFB_REPOPARENT'], os.environ['TFB_REPONAME'], \
    'results'))))
date_time = datetime.datetime.now()
dt_folder = date_time.strftime('%Y%m%d%H%M%S')
path_out = os.path.abspath(os.path.join(os.environ['TFB_LOGSFOLDER'], \
    dt_folder))

if not os.path.exists(path_out):
  os.makedirs(path_out)

zip_file = zipfile.ZipFile(path_out + '/results.zip', 'w', zipfile.ZIP_DEFLATED)

for root, dirs, files in os.walk(path_in):
  for file in files:
    zip_file.write(os.path.join(root, file))

zip_file.close()
