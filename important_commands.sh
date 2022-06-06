sudo apt-get install python3-catkin-tools

sudo apt install python3-vcstool

echo 'export RPGQ_PARAM_DIR=/home/therealyou/agile_autonomy_ws/catkin_aa/src/rpg_flightmare' >> ~/.bashrc

pip install open3d

wget -c https://github.com/intel-isl/Open3D/releases/download/v0.12.0/open3d-app-0.12.0-Ubuntu_20.04.deb
sudo apt-get install ./open3d-app-0.12.0-Ubuntu_20.04.deb

pip install rospkg pyquaternion open3d opencv-python


# https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/
sudo apt-get install ros-noetic-gazebo-ros-pkgs ros-noetic-gazebo-ros-control

# http://wiki.ros.org/roslaunch/XML/remap
