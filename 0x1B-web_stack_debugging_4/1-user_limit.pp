# Change the OS configuration so that it is possible to login with the
# holberton user and open a file without any error message.

$command_path = '/usr/local/bin/:/bin/'

exec { 'increase-hard-limit':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => $command_path
}

exec { 'increase-soft-limit':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => $command_path
}
