# Make changes to ssh configuration file
file { '~/.ssh/config':
  ensure  => file,
  path    => '~/.ssh/config',
  owner   => 'ubuntu',
  mode    => '0600',
  content => '
Host 100.25.46.141
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
',
}
