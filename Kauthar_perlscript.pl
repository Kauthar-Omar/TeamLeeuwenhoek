#!/usr/bin/env perl

$name = 'Kauthar Omar';
$email = 'kauthyomar@gmail.com';
$slack_username = '@Kauthar';
$biostack = 'genomics/transcriptomics';
$twitter_handle = '@K__Omar';
$hamming_distance = hd($slack_username, $twitter_handle);

#hamming_distance function
sub hd {
  ($s,$t) = @_;
  $len = length ($s);
  $num_mismatch = 0;

  if ( length($s) ne length($t) ) {
    print "Strings need to be of equal length to calculate hamming_distance";
  } else {
    # Calculating hamming_distance.
    for ($i=0; $i<$len; $i++)
    {
     ++$num_mismatch if substr($s, $i, 1) ne substr($t, $i, 1);
    }

    return $num_mismatch;

  }

}

print "$name,$email,$slack_username,$biostack,$twitter_handle,$hamming_distance";
