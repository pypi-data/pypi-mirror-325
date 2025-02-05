from setuptools import setup, find_packages

with open("README.md","r",encoding="utf-8") as f:
    description = f.read()

setup(
    name = 'IoTVision',
    version='0.2',
    packages = find_packages(),
    install_requires = [
        'opencv-python==4.10.0.84'
    ],
    long_description=description,
    long_description_content_type="text/markdown"
)