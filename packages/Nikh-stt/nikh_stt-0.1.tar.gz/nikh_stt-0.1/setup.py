from setuptools import setup,find_packages

setup(
    name='Nikh-stt',
    version='0.1',
    authoy='Nikhil Patidar',
    autor_email='nickpatidar4@gmail.com',
    description='This is speeh to text package created by nikhil patidar'
)
packages=find_packages(),
install_requirements=[
    'selenium',
    'webdriver_manager'
]
