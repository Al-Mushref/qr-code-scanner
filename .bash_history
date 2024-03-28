sudo apt-get install ros-noetic-visp-auto-tracker
sudo apt update
sudo apt-get install ros-noetic-visp-auto-tracker
ls
source ros_entrypoint.sh 
cd /opt/ros/noetic/share/visp_auto_tracker/
ls
roslaunch visp_auto_tracker tracklive_usb.launch
ls
cd launch/
ls
cd ..
sudo apt-get install ros-noetic-visp-auto-tracker
ls
cd ..
cd share
ls
cd visp_auto_tracker/
ls
clear
ls
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
source devel/setup.bash
ls
cd src/
ls
cd ~/catkin_ws/
ls
catkin_make
clear
cd ..
ls
rmdir catkin_ws/
rmdir  catkin_ws/src/
rmdir catkin_ws/
ls
$ source /opt/ros/noetic/setup.bash
source /opt/ros/noetic/setup.bash
ls
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
source devel/setup.bash
echo $ROS_PACKAGE_PATH
ls
cd ~/catkin_ws/src
ls
catkin_create_pkg qr_code_reader rospy geometry_msgs
ls
cd qr_code_reader
mkdir scripts
cd scripts
touch qr_code_listener.py
rostopic list
cd /root
cd 
cd ..
source ros_entrypoint.sh 
rostopic list
cd ..
ls
cd root
ls
apt-get update
apt-get install git
git config --global user.name "Al-Mushref"
git config --global user.email "youremail@example.com"
git config --global user.email "yaman20214@gmail.com"
cd /root/catkin_ws/src/qr_code_reader 
git init
git add .
git commit -m "Initial commit of QR code listener"
git remote add origin https://github.com/Al-Mushref/qr-code-scanner.git
ls
git push -u origin main 
