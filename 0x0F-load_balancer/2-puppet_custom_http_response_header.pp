# Install nginx package
package { 'nginx':
  ensure => installed,
}


file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;
        
        add_header X-Served-By \$hostname;
        
        root /var/www/html;
        
        index index.html;
        
        location /redirect_me {
            return 301 https://www.google.com/;
        }
        
        error_page 404 /404_page.html;
        location = /404_page.html {
            internal;
        }
    }
  ",
  notify  => Service['nginx'],
}

# Create index page 
file { '/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!\n",
}

# Create error page
file { '/var/www/html/404_page.html':
  ensure  => present,
  content => "Ceci n'est pas une page\n",
}

# Ensure nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
