#Puppet to make changes to our configuration file.
file_line { 'Turn off passwd auth':
  ensure => present,
  line   => 'PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config',
}

file_line { 'Declare identity file':
  ensure => present,
  line   => '/etc/ssh/ssh_config',
  path   => 'IdentityFile ~/.ssh/school'
}
