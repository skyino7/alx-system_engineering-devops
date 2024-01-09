exec {'update_system':
  command => '/usr/bin/apt-get -y update',
}

package {'nginx':
  ensure => 'installed',
}

package { 'augeas-tools':
  ensure => 'installed',
}


service {'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

file {'/var/www/html/index.html':
  content => 'Hello World!',
}

# Use Augeas to add the custom header
augeas { 'nginx_custom_header':
  context => '/files/etc/nginx/sites-available/default',
  changes => [
    "set server[last()]/location[last()]/add_header X-Served-By ${hostname}",
  ],
  require => [Package['nginx'], Service['nginx']],
}
