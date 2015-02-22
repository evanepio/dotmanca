# -*- mode: ruby -*-
# vi: set ft=ruby :
$provisionScript = <<PROVISION_SCRIPT

echo Start Provisioning

wget https://apt.puppetlabs.com/puppetlabs-release-precise.deb
sudo dpkg -i puppetlabs-release-precise.deb
sudo apt-get update

sudo apt-get install puppet

echo Puppet provisioned

mkdir -p /etc/puppet/modules;
function install_module {
folder=`echo $1 | sed s/.*-//`
if [ ! -d /etc/puppet/modules/$folder ]; then
  puppet module install $1
fi
}
PROVISION_SCRIPT

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "hashicorp/precise32"
  config.vm.box_url = "https://vagrantcloud.com/hashicorp/boxes/precise32/versions/1.0.0/providers/virtualbox.box"

  config.vm.network :forwarded_port, guest: 8000, host: 8000
  config.vm.synced_folder(".", "/vagrant")

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", "2048"]
  end

  config.vm.provision "shell", inline: $provisionScript

  # config.vm.provision "puppet" do |puppet|
    # puppet.manifests_path = "puppet_manifests"
    # puppet.manifest_file = "default.pp"
  # end
end
