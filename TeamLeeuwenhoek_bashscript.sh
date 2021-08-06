#!/usr/bin/env bash
#To run this script sudo password required for running c++ script.
#Note final csv file generated is TeamLeeuwenhoek.csv intermediate files are deleted.

#To clone the repo.
git clone https://github.com/Kauthar-Omar/TeamLeeuwenhoek

#Running all scripts and saving output.
# Bash
bash Kauthar_bashscript.sh > outputrecord.csv

# Python
python Abdulafiz_Pythonscript.py >> outputrecord.csv
python Task1halakpython.py >> outputrecord.csv
python Adams_pythonscript.py >> outputrecord.csv
python kheira_pythonscript.py >> outputrecord.csv
python Kasturi_pythonscript.py.py >> outputrecord.csv
python 'Rhoda_task1_ pythoscript.py' >> outputrecord.csv

# Perl.
perl Kauthar_perlscript.pl >> outputrecord.csv

# c++ script.
sudo g++ Pratham99_c++script.cpp
./a.out >> outputrecord.csv

#Generating final output file to save names
#Adding header line
echo 'Name,Email,Slack_username,Biostack,Twitter_handle,Hamming_distance' > TeamLeeuwenhoek.csv
#Sorting names alphabetically and selecting unique names as
#some teammates created more than 1 scripts to avoid name repetition.
sort outputrecord.csv | uniq --check-chars=10 >> TeamLeeuwenhoek.csv

#removing the intermediate file to remain with one .csv file
rm outputrecord.csv
