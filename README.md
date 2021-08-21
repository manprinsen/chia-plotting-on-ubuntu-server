## 🌱 About

I would like to share my (little) knowledge about getting started with chia plotting on ubuntu server (21.04).

## ⚠️ Disclaimer

This repository will help a novice Linux user quickly getting started with chia plotting on Ubuntu Server 21.04. Since i am just learning github - there will be hard codes parameters which you need to change to match your environment.

## 👌 Step by step guide

* ⬇️ You need a fresh Ubuntu Server 21.04 installation with the SSH feature enabled. The following links will guide you through the download process, installation and on how to create a bootable USB stick:
  https://ubuntu.com/tutorials/install-ubuntu-server#1-overview
  https://releases.ubuntu.com/21.04/ubuntu-21.04-desktop-amd64.iso

* ♿ Once the Ubuntu Server is up and running, go to your development machine and connect to your new Ubuntu Server through SSH. For example:

  ```bash
  ssh your_user_name@your_servers_local_ip_address
  ```

- 🏛️ To configure a local static ip address, please follow this link: https://linuxize.com/post/how-to-configure-static-ip-address-on-ubuntu-20-04/

- 😀 Now we are one step closer to start plotting on our server

- 📁 Create a folder called chia in your home directory 

  ```bash
  cd ~
  mkdir chia && cd chia
  ```

- 🔄 Install a neat tool called `progress`, which will monitor system processes like `cp` `mv` `rsync` etc 

  ```bash
  sudo apt install progress
  ```

  📶 For example, to view file transfers in real time we execute

  ```bash
  progress -w
  ```

- 💽 ⛏️ MadMax chia plotter needs to be installed within the directory `chia` directory we created earlier (~/chia). Issue the commands below to install the MadMax chia plotter  

  ```bash
  sudo apt install -y libsodium-dev cmake g++ git build-essential
  # Checkout the source and install
  git clone https://github.com/madMAx43v3r/chia-plotter.git 
  cd chia-plotter
  
  git submodule update --init
  ./make_devel.sh
  ./build/chia_plot --help`
  
  # Code is copied from https://github.com/madMAx43v3r/chia-plotter
  ```

* ⏰ A few moments later

* 🪄 Now it's time to download my magical program  

  ```bash
  wget https://raw.githubusercontent.com/manprinsen/chia-plotting-on-ubuntu-server/main/program.py && sudo chmod 777 program.py
  ```

* ✋ Before we run the program, we need to enter the a correct Pool Key and Farmer Key within the program.
  The variables `poolKey` and `farmerKey` will be found in the beginning of the file

  ```python
  sudo nano program.py
  # ==> below is example output from the file
  #!/usr/bin/env python3
  ...
  poolKey = "enter your own key"
  farmerKey = "enter your own key"
  ...
  ```

  To save the changes simply execute the following key combination `ctrl + x` followed by `y (to save)` and hit  `enter`

* 🚀 To run the program, simply issue the following command

  ```bash
  ./program.py
  ```

  You will be greeted with the following screen

  ```python
   --------------------------------------------
  |                                            |
  |   W E L C O M E  T O  M Y  P R O G R A M   |
  |                                            |
  |   Select one of the following options:     |
  |                                            |
  |   [ 1 ]   - Mount Drive                    |
  |   [ 2 ]   - Mount Ram Drive                |
  |   [ 3 ]   - Unmount Drive                  |
  |   [ 4 ]   - Delete All File In Drive       |
  |   [ 5 ]   - Turn Off System Swap           |
  |   [ 6 ]   - Turn On High Performance       |
  |   [ 7 ]   - Open Screen Session            |
  |   [ 8 ]   - List Disk Infomation           |
  |   [ 9 ]   - Start MadMax Plotter           |
  |   [ 10 ]  - Start Plot Mover               |
  |   [ 11 ]  - View Move Processes            |
  |   [ q ]   - Quit Program                   |
  |                                            |
  |                                            |
  |                                            |
  |                                            |
   --------------------------------------------
  ```

* 🙏 I dont know it it's just be, but I have a hard time remembering a bunch of shell commands. So the main purpose  of this program is the handle this for you. 

  #### From now on you will only need to SELECT which task you want run, which, from my perspective, makes Ubuntu Server USER FRIENDLY!!

* 🏳️ I appreciate any feedback, especially feedback from Linux guru's
