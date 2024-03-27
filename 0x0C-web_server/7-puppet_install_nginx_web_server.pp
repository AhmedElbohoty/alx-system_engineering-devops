# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# To configure Nginx, stop it temporarily.
service { 'nginx':
  ensure  => stopped,
  enable  => false, # Disable auto start at boot time
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/var/www/html/404_page.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index  index.html;

    location /redirect_me {
        return 301 https://www.google.com/;
    }

    error_page 404 /404_page.html;
    location = /404_page.html {
        internal;
    }
}",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Start Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}

