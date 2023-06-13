import pathlib
from setuptools import find_packages, setup

from jmessaging import __version__ as version


here = pathlib.Path(__file__).parent
readme = (here / "README.md").read_text().splitlines()
extras_require = {"dev": (here / "requirements-dev.txt").read_text()}

setup(
    name="jmessaging",
    author="Jay Ess",
    version=version,
    description="Make printing colorized messages to terminal easier",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/jay3ss/jmessaging",
    packages=find_packages(),
    license="MIT",
    include_package_data=True,
    extras_require=extras_require,
)
