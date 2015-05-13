# -*- mode: ruby -*-
# vi: set ft=ruby :
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "hashicorp/trusty32"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/20150506/trusty-server-cloudimg-i386-vagrant-disk1.box"

  config.vm.network :forwarded_port, guest: 80, host: 8000
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
end
