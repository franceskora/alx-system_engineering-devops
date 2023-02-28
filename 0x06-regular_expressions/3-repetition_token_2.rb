#!/usr/env ruby
# Match "hbtn, hbttn, hbttttn" not "hbn"

puts ARGV[0].scan(/hbt+n/).join
