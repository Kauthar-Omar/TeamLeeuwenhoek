import java.io.*;

public class Pratham99_javascript {
    
    public static void main (String [] args){
        
        int i, length, hamming_distance=0;
        String name, email, slack_username, biostack, twitter_handle;
        
        name = "Prathamesh Bobale";
        email = "gmsbin02.prathamesh.bobale@gnkhalsa.edu.in";
        slack_username = "Pratham99";
        biostack = "Genomics/Software/Transcriptomics";
        twitter_handle = "pbobale99";
        
        length = twitter_handle.length();
        for (i=0; i<length; i++){
            
            if (slack_username.charAt(i)!= twitter_handle.charAt(i))
            {
                hamming_distance++;
            } 
        }
        
        System.out.println(name + "," + email + ",@" + slack_username + "," + biostack
        + ",@" + twitter_handle + "," + hamming_distance );
    }
    
}