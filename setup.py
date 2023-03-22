# setup.py template
# run with python setup.py install

from setuptools import setup, find_packages
import os


def read_inputs():
    return open(os.path.join(os.getcwd(),"requirements.txt")).readlines()


setup(
    name="NV35_audio_validations",
    version="0.0.1",
    include_package_data=True,
    install_requires=read_inputs(),
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        nv35=nv35:tests
    """,
)
