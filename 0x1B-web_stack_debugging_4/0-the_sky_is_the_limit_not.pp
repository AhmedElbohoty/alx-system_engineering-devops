exec { 'Fix':
  command => 'sed -i "s/^ULIMIT=\"-n 15\"/ULIMIT=\"-n 8192\"/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

service { 'nginx':
  ensure    => 'stopped',
  enable    => false
}

service { 'nginx':
  ensure    => 'running',
  enable    => true
}
