# Update the soft limit for the 'holberton' user
exec { 'update_soft_limit':
  command  => "sed -i 's/^holberton soft nofile.*/holberton soft nofile 8192/' /etc/security/limits.conf",
  provider => shell,
}

# Update the hard limit for the 'holberton' user
exec { 'update_hard_limit':
  command  => "sed -i 's/^holberton hard nofile.*/holberton hard nofile 8192/' /etc/security/limits.conf",
  provider => shell,
}
