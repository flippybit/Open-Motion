# ROS workflows

## Create a new Workspace
the workspace is where all your robot related packages live in.

1.  Create a catkin workspace `mkdir -p my_workspace/src`


## Add a package to your workspace folder
### From git 
   0. git clone the package into your workspace folder
```bash
cd ~/catkin_ws/src
git clone https://github.com/jmeyer1292/fake_ar_publisher.git
```
1.  Use `catkin build` **must be used inside catkin workspace**
2.  Once built source the devil `source devel/setup.bash`
3.  run `rospack find fake_ar_publisher` to verify the new packages are visible to ROS

## Create a new package 

1. create a package


## usefull catkin commands 
*  `catkin list`
*  `catkin build`
*  