#include<iostream>
#include<string>
#include<cstring>
using namespace std;

int main () {

    int i, length, hamming_distance=0;
    string name, email, biostack;

    name = "Prathamesh Bobale";
    email = "gmsbin02.prathamesh.bobale@gnkhalsa.edu.in";
    char slack_username[] = {"Pratham99"};
    biostack = "Genomics/Software/Transcriptomics";
    char twitter_handle[] = {"pbobale99"};
    
    length = strlen(twitter_handle);
    for(i = 0; i < length; i++)
    {
        if(slack_username[i] != twitter_handle[i])
        {
            hamming_distance++;
        }
    }  // for computing hamming distance


    cout<<name<<","<<email<<",@"<<slack_username<<","<<biostack<<",@"
    <<twitter_handle <<","<<hamming_distance;

    return 0;
}