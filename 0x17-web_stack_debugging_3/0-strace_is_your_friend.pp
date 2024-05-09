# Fix the bug
exec { 'Fix 500 bug':
  provider => 'shell',
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
