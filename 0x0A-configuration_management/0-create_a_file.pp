# create a file in /tmp.

# Requirements:
# - File path is /tmp/school
# - File permission is 0744
# - File owner is www-data
# - File group is www-data
# - File contains I love Puppet
file { '/tmp/school':
  path    => '/tmp/school',
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
}
