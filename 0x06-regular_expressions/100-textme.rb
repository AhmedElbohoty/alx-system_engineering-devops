#!/usr/bin/env ruby
RECEIVER = ARGV[0].scan(/(?<=from:).*?(?=\])/)
SENDER = ARGV[0].scan(/(?<=to:).*?(?=\])/)
FLAGS = ARGV[0].scan(/(?<=flags:).*?(?=\])/)

puts [RECEIVER, SENDER, FLAGS].join(',')