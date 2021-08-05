#!/usr/bin/env perl

$name = 'Kauthar Omar';
$email = 'kauthyomar@gmail.com';
$slack_username = '@Kauthar';
$biostack = 'genomics/transcriptomics';
$twitter_handle = '@K__Omar';
$humming_distance = hd($slack_username, $twitter_handle);

sub hd {
  #String length is assumed to be equal.
  #For it to be humming_distance string length must be equal.
  ($k,$l) = @_;
  $len = length ($k);
  $num_mismatch = 0;

  for ($i=0; $i<$len; $i++)
  {
   ++$num_mismatch if substr($k, $i, 1) ne substr($l, $i, 1);
  }

  return $num_mismatch;
}

print "$name,$email,$slack_username,$biostack,$twitter_handle,$humming_distance";
