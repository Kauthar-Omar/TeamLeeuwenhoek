
import hashlib

def hamming_distance(slack,twitter):
    return sum(c1 != c2 for c1, c2 in zip(slack, twitter))





name= 'Name: Kheira Lakhdari,'
email= 'Email: kirabasma12@gmail.com,'
slack= '@Kheira,'
biostack= 'Biostack: software development / Data science,'
twitter= '@Kheira,'



print (name, email, slack, biostack, twitter, hamming_distance(slack,twitter))

