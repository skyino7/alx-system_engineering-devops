#Puppet to make changes to our configuration file.
File_line { 'Turn off passwd auth':
  ensure => present,
  line   => 'PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config',
}

File_line { 'Declare identity file':
  ensure => present,
  line   => '/etc/ssh/ssh_config',
  path   => 'IdentityFile ~/.ssh/school'
}
