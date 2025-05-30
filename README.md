# robot_description

This ROS 2 package provides the URDF/Xacro robot model and launch files to publish the TF tree using `robot_state_publisher`.
While the current one is only for running through localization.

## Features

- Xacro-based robot description (`robot.urdf.xacro`)
- Generates URDF file from Xacro
- Launch file to start `robot_state_publisher`
- Publishes TFs for links such as `base_link`, `imu_link`, and `gps_link`


## Directory Structure
```
robot_description/
├── launch/
│  └── display.launch.py
├── urdf/
│  ├── robot.urdf.xacro
│  └── robot.urdf  # optional, generated from Xacro
├── package.xml
└── setup.py
```

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

## Monitoring

Generate a PDF visualization of the current TF tree (frames.pdf) for debugging the TF topology structure:
```
ros2 run tf2_tools view_frames
```

View the TF transformation (include translation and rotation) between base_link to imu_link in real time. But this require you run localization then you can view the transform.
```
ros2 run tf2_tools tf2_echo base_link imu_link
```

Check /tf topic (i.e. TF broadcast data) in real time:
```
ros2 topic echo /tf
```

