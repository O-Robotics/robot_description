# robot_description
URDF
## Prerequisite

You need to download package:
```
sudo apt update
sudo apt install ros-humble-xacro
```
 And go to the folder of xacro file and generate your URDF file:

```
cd ~/gnss_ws/src/robot_description/urdf
ros2 run xacro xacro robot.urdf.xacro -o robot.urdf
```

 Finally, source your workspace:
 ```
cd ~/gnss_ws
source install/setup.bash
```

## Build and run



```
cd ~/gnss_ws
colcon build --packages-select robot_description --event-handlers console_direct+
source install/setup.bash
ros2 launch robot_description display.launch.py
```
