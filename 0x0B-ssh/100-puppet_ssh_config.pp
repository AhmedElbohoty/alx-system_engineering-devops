# Make changes to ssh configuration file
file { '/home/username/.ssh/config':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  mode   => '0600',
  content => "
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
  ",
}
