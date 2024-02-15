#Puppet
exec { 'replace_extension':
  command => '/bin/sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  path    => '/usr/bin:/usr/sbin:/bin',
  notify  => Exec['restart_apache_service'],
}

exec { 'restart_apache_service':
  command     => '/usr/sbin/service apache2 restart',
  refreshonly => true,
}
