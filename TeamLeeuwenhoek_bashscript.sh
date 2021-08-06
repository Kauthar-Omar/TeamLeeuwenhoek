#!/usr/bin/env bash
#Note final csv file generated is TeamLeeuwenhoek.csv intermediate files are deleted.

#To clone the repo.
git clone https://github.com/Kauthar-Omar/TeamLeeuwenhoek

cd TeamLeeuwenhoek #Moving into directory to enable script running.

#Running all scripts and saving output.
# Bash
bash Kauthar_bashscript.sh > outputrecord.csv

# Python
for file in *.py
do
  python $file >> outputrecord.csv
done

# Perl.
perl Kauthar_perlscript.pl >> outputrecord.csv

# java
javac Pratham99_javascript.java
java Pratham99_javascript >> outputrecord.csv

# R
Rscript Kauthar_Rscript.R >> outputrecord.csv

# c++ script.
g++ Pratham99_c++script.cpp
./a.out >> outputrecord.csv

#Generating final output file to save names
#Adding header line
echo 'Name,Email,Slack_username,Biostack,Twitter_handle,Hamming_distance' > TeamLeeuwenhoek.csv
#Sorting names alphabetically and selecting unique names as
#some teammates created more than 1 scripts to avoid name repetition.
sort outputrecord.csv | uniq --check-chars=20 >> TeamLeeuwenhoek.csv

#removing the intermediate file to remain with one .csv file
rm outputrecord.csv

# Creating a copy of the csv file in the path you are running the script from for ease in viewing.
cp TeamLeeuwenhoek.csv ../
