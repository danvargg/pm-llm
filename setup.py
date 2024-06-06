"""Setup file for the fightcamp package."""
from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='pm-agent',
    version='1.0.0',
    description='PM Agents',
    author='Daniel Vargas',
    # maintainer_email='daniel.vargas@joinfightcamp.com',
    packages=['rag'],
    install_requires=requirements
)
