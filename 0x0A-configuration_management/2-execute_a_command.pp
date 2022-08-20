# Kills the killmenow process using puppet manifest.

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/'
}
