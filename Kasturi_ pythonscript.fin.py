#task 1
name = "Kasturi Pradhan"
email = "kasturi.irl@gmail.com"
Slack_username = "@Kasturi"
biostack = "Genomics/Vaccine informatics"
twitter_handle = "@kastumuchmess"
#updated task
def hamming_distance(Slack_username, twitter_handle):
    return sum(c1 !=c2 for c1, c2 in zip(Slack_username, twitter_handle))
#final output
print ( name , email , Slack_username , biostack , twitter_handle ,hamming_distance(Slack_username, twitter_handle), sep = ',' )
