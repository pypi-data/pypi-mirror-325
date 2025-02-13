from setuptools import setup, find_packages
import platform
import pathlib

# Read the README for the long description
this_directory = pathlib.Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Choose the appropriate readline package based on the platform
if platform.system() == "Windows":
    readline_package = ['pyreadline3']
else:
    readline_package = ['readline']

setup(
    name="roysh",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'roysh=roysh:main',
        ],
    },
    author="Nishan Roy",
    author_email="nishanroy561@gmail.com",
    description="A Python-based shell with tab completion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nishanroy561/RoySH",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: System :: Shells",
    ],
    install_requires=readline_package,
    python_requires='>=3.6',
) 