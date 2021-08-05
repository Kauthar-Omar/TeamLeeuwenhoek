#task 1
name = "Kasturi Pradhan"
email = "kasturi.irl@gmail.com"
Slack_username = "@Kasturi"
biostack = "Genomics, Transcriptomics, Data Science, Drug development, Epigenomics, Medical Chemistry and Cheminformatics ,Vaccine informatics, Public health and Genomic Epidemiology"
twitter_handle = "@kastumuchmess"

#updated task
s1 = '@Kasturi'
s2 = '@kastumuchmess'

def hamming_distance(s1,s2):
    return sum(c1 !=c2 for c1, c2 in zip(s1,s2))



#final output
print ( name , email , Slack_username , biostack , twitter_handle ,hamming_distance(s1 , s2), sep = ',' )

