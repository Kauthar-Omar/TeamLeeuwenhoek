#!/usr/bin/env bash

name='Kauthar Omar'
email='kauthyomar@gmail.com'
slack_username='@Kauthar'
biostack='genomics/transcriptomics'
twitter_handle='@K__Omar'

#hamming_distance calculation.
if [ ${#slack_username} == ${#twitter_handle} ]; then
  for (( i=0; i<${#slack_username}; ++i )); do
    if [ ${slack_username:$i:1} != ${twitter_handle:$i:1} ]; then
        let "distance++"
    fi
  done
else
  echo "Strings need to be of equal length to calculate hamming_distance"
fi

hamming_distance=$distance

echo ${name},${email},${slack_username},${biostack},${twitter_handle},${hamming_distance}
