# Project: Human in the loop control of Multi Agent Systems

## Software in the loop simulation of crazyflie 2.0

Steps to start the launch file of crazyflie 2.0.
Start with the script that will launch Gazebo. The launch file maybe crazyflie_sim.launch .

$ cd '/home/shetty/catkin_ws/src/crazyflie_ros/crazyflie_2.0/crazyflie_gazebo/launch' 

$ ls

$ roslaunch crazyflie_sim.launch


Next, open the script containing python programs for various tasks:		

$ cd '/catkin_ws/src/crazyflie_ros/crazyflie_2.0/crazyflie_gazebo/scripts'

$ ./run_cfs.sh

After running the above script, gyrobias found must be printed on the screen.

Then,run the python programs for several tasks such as testing the vertical trajectory, helix trajectory, waypoint navigation,etc.

$ cd '/catkin_ws/src/crazyflie_ros/crazyflie_2.0/crazyflie_gazebo/scripts'

$ ls

$ python vertical_trajectory.py 


## Real time Human in the loop control of DJI Tello EDU drone
* Multi agent system consists of master controller sending signals to slaves.
* In this project, Laptop acts as a master and Tello EDU drone would be the slave.
* Tasks to be completed: high level trajectory, waypoint navigation, helix trajectory.


### Steps to run python scripts
* $ python3.12 -m venv venv
* $ source venv/bin/activate
* $ pip install djitellopy
* $ pip freeze > requirements.txt
* $ python drone_simple.py