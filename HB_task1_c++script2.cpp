#include<iostream>
using namespace std;

#include<fstream>

int main ()
{
    fstream myfile;
    myfile.open("hackbio_task1.csv", ios::out);
    if (myfile.is_open())
    {
        myfile <<"Name"<<","<<"Email"<<","<<"Username"<<","<<"Biostack\n";
        myfile <<"Prathamesh Bobale"<<","<<"gmsbin02.prathamesh.bobale@gnkhalsa.edu.in"<<","<<"@Pratham99"
        <<","<<"Genomics/Software";
        myfile.close();
    }

    return 0;
}