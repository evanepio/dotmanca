# -*- mode: ruby -*-
# vi: set ft=ruby :
VAGRANTFILE_API_VERSION = "2"

# Found: http://askubuntu.com/questions/488529/pyvenv-3-4-error-returned-non-zero-exit-status-1
$workaround = <<WORKAROUND_FOR_PYVENV_NOT_WORKING_IN_TRUSTY
pyvenv-3.4 --without-pip djangoVENV
source ./djangoVENV/bin/activate
wget https://pypi.python.org/packages/source/s/setuptools/setuptools-3.4.4.tar.gz
tar -vzxf setuptools-3.4.4.tar.gz
cd setuptools-3.4.4
python setup.py install
cd ..
wget https://pypi.python.org/packages/source/p/pip/pip-1.5.6.tar.gz
tar -vzxf pip-1.5.6.tar.gz
cd pip-1.5.6
python setup.py install
cd ..
deactivate
rm -R setuptools-3.4.4*
rm -R pip-1.5.6*
WORKAROUND_FOR_PYVENV_NOT_WORKING_IN_TRUSTY

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "hashicorp/trusty32"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/20150506/trusty-server-cloudimg-i386-vagrant-disk1.box"

  config.vm.network :forwarded_port, guest: 8000, host: 8000
  config.vm.synced_folder(".", "/vagrant")

  config.vm.synced_folder 'salt/roots', '/srv'

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", "2048"]
  end

  config.vm.provision "salt" do |salt|
    salt.minion_config = "salt/minion.conf"
    salt.run_highstate = true
    salt.verbose = true
  end

  config.vm.provision "shell", inline: $workaround, privileged: false
end
