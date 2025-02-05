from setuptools import setup, find_packages
setup(
    name = 'IoTVision',
    version='0.1',
    packages = find_packages(),
    install_requires = [
        'opencv-python==4.10.0.84'
    ]
)