# Make changes to ssh configuration file
include stdlib
file_line { 'IdentityFile ~/.ssh/school':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  # If the line is not found in the file, Puppet will add it to the file
  replace => true,
}

file_line { 'PasswordAuthentication no':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  # If the line is not found in the file, Puppet will add it to the file
  replace => true,
}
