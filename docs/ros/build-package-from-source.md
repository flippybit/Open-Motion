# Download and build a package from source

   0. git clone the package into your workspace folder
```bash
cd ~/catkin_ws/src
git clone https://github.com/jmeyer1292/fake_ar_publisher.git
```
1.  Create a catkin workspace `mkdir -p my_workspace/src`
2.  Use `catkin build` **must be used inside catkin workspace**
3.  Once built source the devil `source devel/setup.bash`
4.  run `rospack find fake_ar_publisher` to verify the new packages are visible to ROS
   
