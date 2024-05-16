# Change the OS configuration so that it is possible to login with the
# holberton user and open a file without any error message.

$user = 'holberton'
$limi = '50000'
$command_path = '/usr/local/bin/:/bin/'

exec { "increase-hard-file-limit-for-${user}-user":
  command => "sed -i \"/${user} hard/s/5/${limi}/\" /etc/security/limits.conf",
  path    => $command_path,
}

exec { "increase-soft-file-limit-for-${user}-user":
  command => "sed -i \"/${user} soft/s/4/${limi}/\" /etc/security/limits.conf",
  path    => $command_path,
}
