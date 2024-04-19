# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do | config |
    config.vm.provider "virtualbox" do | vb|
        vb.memory = "1024"
        vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    end
    config.vm.box_check_update = false

boxes = [
    # You can modify the nodes list here for as many virtual boxes you want
    # if you add hosts here.. update the hosts file too for ansible
    {:name => "dev", :ip => "192.168.56.11", host_port:8991},
]

    boxes.each do |opts|
        config.vm.define opts[:name] do |box|
            box.vm.box = "ubuntu/bionic64"
            box.vm.hostname="#{opts[:name]}.homelab.com"
            box.vm.network "private_network", ip: opts[:ip]
            box.vm.provision "shell", path: "vagrant/bootstrap.sh"
            if (opts[:name] == "dev")
                box.vm.synced_folder "./", "/home/vagrant/apps"
                # box.vm.provision "file", source: "vagrant/key_gen.sh", destination: "/home/vagrant/"
                box.vm.network :forwarded_port, guest: 8001, host: opts[:host_port]
            end
        end
    end
end
