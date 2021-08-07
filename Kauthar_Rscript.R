#/usr/bin/env Rscript

name <- 'Kauthar Omar'
email <- 'kauthyomar@gmail.com'
slack_username <- '@Kauthar'
biostack <- 'Genomics/Transcriptomics'
twitter_username <- '@K__Omar'

#calculating hamming distance.
s <- c('@', 'K', 'a', 'u', 't', 'h', 'a', 'r')
t <- c('@', 'K', '_', '_', 'O', 'm', 'a', 'r')

hamming_distance <- sum(s != t)

#Atternatively it can be calculated using DescTools.
#install.packages("DescTools")
#library(DescTools)
#hamming_distance <- StrDist(slack_username, twitter_username, method="hamming")

cat(name, email, slack_username, biostack, twitter_username, hamming_distance, "\n", sep = ',')
