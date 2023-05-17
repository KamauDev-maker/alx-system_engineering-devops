file { '/var/www/html/wp-settings.php':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => replace(
    template('your_module/wp_settings.php.erb'),
    '.phpp',
    '.php',
    'g',
  ),
}
