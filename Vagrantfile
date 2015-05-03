# -*- mode: ruby -*-
# vi: set ft=ruby :
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "hashicorp/precise32"
  config.vm.box_url = "https://vagrantcloud.com/hashicorp/boxes/precise32/versions/1.0.0/providers/virtualbox.box"

  config.vm.network :forwarded_port, guest: 8000, host: 8000
  config.vm.synced_folder(".", "/vagrant")

  config.vm.synced_folder 'salt/roots', '/srv'

  config.vm.hostname = "vagrant.example.com"

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", "2048"]
  end

  config.vm.provision "salt" do |salt|
    salt.minion_config = "salt/minion.conf"
    salt.run_highstate = true
    salt.verbose = true
  end
end
