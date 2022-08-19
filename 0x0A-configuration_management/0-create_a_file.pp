#creates a file using puppet manifest

$file = '/tmp/school'

file { $file:
  ensure  => 'file',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744'
}

