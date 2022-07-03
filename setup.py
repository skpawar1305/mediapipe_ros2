from glob import glob
import os
from setuptools import setup

package_name = 'mediapipe_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('./launch/*.launch.py')),
        (os.path.join('share', package_name, 'keypoint_classifier_hands'), glob('keypoint_classifier_hands/*')),
        (os.path.join('share', package_name, 'keypoint_classifier_pose'), glob('keypoint_classifier_pose/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='skpawar1305',
    maintainer_email='skpawar1305@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hands = ' + package_name + '.hands:main',
            'pose = ' + package_name + '.pose:main',
        ],
    },
)
