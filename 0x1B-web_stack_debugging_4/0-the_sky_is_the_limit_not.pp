exec { 'Fix':
  command => 'sed -i "s/^ULIMIT=\"-n 15\"/ULIMIT=\"-n 8192\"/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'Restart nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
