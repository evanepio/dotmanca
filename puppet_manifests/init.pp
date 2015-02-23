class {'postgresql::globals':
    version => '9.3',
    manage_package_repo => true,
    encoding => 'UTF8',
    locale  => 'it_IT.utf8'
}->
class { 'postgresql::server':
    listen_addresses => '*'
}

class { 'postgresql::server::contrib':
    package_ensure => 'present'
}
