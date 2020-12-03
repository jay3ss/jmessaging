import pathlib
from setuptools import find_packages, setup


here = pathlib.Path(__file__).parent
readme = (here/'README.md').read_text()

setup(
    name='jmessaging',
    author='Jay Ess',
    version='0.1.0',
    description='Make printing colorized messages to terminal easier',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/jay3ss/jmessaging',
    packages=find_packages(),
    license='MIT',
    include_package_data=True
)
