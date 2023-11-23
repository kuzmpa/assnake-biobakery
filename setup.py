from typing import Union

from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

from assnake_biobakery.snake_module_setup import snake_module

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        snake_module.deploy_module()
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        snake_module.deploy_module()
        install.run(self)


setup(
    name='assnake-biobakery',
    version='0.0.1',
    packages=find_packages(),
    entry_points = {
        'assnake.plugins': ['assnake-biobakery = assnake_biobakery.snake_module_setup:snake_module']
    },
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    }
)