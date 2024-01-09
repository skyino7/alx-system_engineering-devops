# Add a custom HTTP header with Puppet
exec {'update':
  command => '/usr/bin/apt-get update'
}

package {'nginx':
  ensure => installed
}

file_line {'header':
  ensure => present,
  path  => '/etc/nginx/sites-available/default'
  line  => "server \tadd_header X-Served-By ${hostname};",
  after => 'server_name _;',
  require => Service['nginx']
}

service { 'nginx':
  ensure => 'running',
  enable => true,
  require => Package['nginx'],
}