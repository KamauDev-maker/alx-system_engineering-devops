file_line { 'update_ulimit':
	path	=> '/etc/default/nginx',
	line	=> 'ULIMIT="-n 3072"',
	match	=> '^ULIMIT=.*',
	notify 	=> Exec['restart_nginx'],
	require => Package['nginx'],
}
 exec { 'restart_nginx':
	command		=> 'service nginx restart',
	refreshonly	=> true,
	path		=> ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
	subscribe	=> File_line['update_ulimit'],
	require		=> Package['nginx'],
}
