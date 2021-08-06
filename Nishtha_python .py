#!/usr/bin/env python
name = ( "Nishtha Malhotra" )
email = ( "nishtham17@gmail.com" )
slack_username = ( "@Nishtha" )
biostack = ( "genomics/transcriptomics/data science/software development/vaccine informatics" )
twitter_handle = ( "@nishu_malhotra" )

s1 = 'slack_username'
s2 = 'twitter_handle'

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

print ( name , email , slack_username , biostack , twitter_handle , hamming_distance(s1, s2), sep = ',' )
