
from setuptools import setup, find_packages

setup(
    name='myinsuranceapp',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example My insurance App',
    long_description='An example My insurance App',
    install_requires=['numpy'],
    url='https://github.com/RincyIssac/Risun_Myinsuranceapp.git',
    author='RiSUN',
    author_email='dummy@bootcamp.com'
)
