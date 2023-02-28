#!/usr/bin/env ruby
# Match "hbtn, htn" not "hbbtn or hbbtn"

puts ARGV[0].scan(/hb?tn/).join
