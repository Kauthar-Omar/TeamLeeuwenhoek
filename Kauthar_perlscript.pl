#!/usr/bin/env perl

$name = 'Kauthar Omar';
$email = 'kauthyomar@gmail.com';
$slack_username = '@Kauthar';
$biostack = 'genomics/transcriptomics';
$twitter_handle = '@K__Omar';
$hamming_distance = hd($slack_username, $twitter_handle);

sub hd {
  ($k,$l) = @_;
  $len = length ($k);
  $num_mismatch = 0;

  if ( length($k) ne length($l) ) {
    print "Strings need to be of equal length to calculate hamming_distance";
  } else {
    # Calculating hamming_distance.
    for ($i=0; $i<$len; $i++)
    {
     ++$num_mismatch if substr($k, $i, 1) ne substr($l, $i, 1);
    }

    return $num_mismatch;

  }

}

print "$name,$email,$slack_username,$biostack,$twitter_handle,$hamming_distance";
