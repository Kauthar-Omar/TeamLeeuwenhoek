#!/usr/bin/env python

name = ( "Nishtha Malhotra" )

email = ( "nishtham17@gmail.com" )

slack_username = ( "@Nishtha" )

biostack = ( "genomics/transcriptomics/data science/software development/vaccine informatics" )

twitter_handle = ( "@nishu_malhotra" )

def hamming_distance(slack_username, twitter_handle):
    i = 0
    count = 0
    
    while (i < len(slack_username)) :
        if (slack_username[i] != twitter_handle[i]) :
             count += 1
        i += 1 
    return count

print ( name , email , slack_username , biostack , twitter_handle , hamming_distance(slack_username, twitter_handle), sep = ',' )
