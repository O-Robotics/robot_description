from setuptools import setup

package_name = 'robot_description'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=[],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/display.launch.py']),
        ('share/' + package_name + '/urdf', ['urdf/robot.urdf.xacro']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Li Ziye',
    maintainer_email='you@example.com',
    description='Robot description package with URDF',
    license='MIT',
    tests_require=['pytest'],
    entry_points={},
)