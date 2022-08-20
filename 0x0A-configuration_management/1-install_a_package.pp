#Using Puppet, install flask from pip3

exec { 'install python packages':
   command ​=> ​'​pip3 install flask==2.1.0 flask_restful apiai​'​,
   path => ['/usr/bin/'],
}
