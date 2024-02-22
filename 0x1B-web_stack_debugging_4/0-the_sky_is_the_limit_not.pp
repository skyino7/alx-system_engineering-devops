#Modify the ULIMIT value
exec { 'adjust_nginx_ulimit':
  command  => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 15000\"/' /etc/default/nginx",
  provider => shell,
}

# Restart the Nginx service
exec { 'restart_nginx':
  command  => 'service nginx restart',
  provider => shell,
}
