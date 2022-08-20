#Using Puppet, create a manifest that kills a process named killmenow.

exec { 'kills a process killmenow':
   command => 'pkill -15 killmenow',
   provider => shell,
}
