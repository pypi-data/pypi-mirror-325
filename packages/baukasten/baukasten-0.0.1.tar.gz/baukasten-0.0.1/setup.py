# vim: ts=8:sts=8:sw=8:noexpandtab
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import pathlib
import setuptools
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / 'README.md').read_text()

# Load requirements from requirements.txt
def load_requirements():
    requirements = (HERE / 'requirements.txt').read_text(encoding='utf-8').splitlines()
    return [line.strip() for line in requirements if line.strip() and not line.startswith("#")]

# Returns the only folder in the src directory (dirs with dots are ignored)
def get_package_name():
    src_dir = HERE / "src"
    folders = [f for f in src_dir.iterdir() if f.is_dir() and "." not in f.name]

    if len(folders) != 1:
        raise RuntimeError(
            f"Expected exactly one folder in 'src' (ignoring dirs with dots), found: {folders}"
        )

    return folders[0].name  # Return the folder name as the package name

# This call to setup() does all the work
setup(
    name="baukasten",
    version="0.0.1",
    description="A plugin framework.",
    long_description=README,
    long_description_content_type='text/markdown',
    url="https://github.com/bytebutcher/python-baukasten",
    author="bytebutcher",
    license='GPL-3.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    packages=setuptools.find_packages(),
    install_requires=load_requirements(),
    include_package_data=True
)
