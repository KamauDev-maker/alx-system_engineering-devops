# fix the limit nginx.
exec { 'fix':
command => 'sed -i "/ULIMIT=/c\ULIMIT=\"-n 2000\"" /etc/default/nginx',
path    => '/bin',
}
service { 'nginx':
ensure    => running,
subscribe => Exec['fix'],
}
