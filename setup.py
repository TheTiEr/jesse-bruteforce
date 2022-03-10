from setuptools import setup, find_packages

# also change in version.py
VERSION = '0.1.0'
DESCRIPTION = "Optimization with hyperactive for jesse"

REQUIRED_PACKAGES = [
    'jesse',
    'pyyaml',
    'hyperactive',
    'psutil'
]

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='jesse-bruteforce',
    version=VERSION,
    author="TheTiEr",
    packages=find_packages(),
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cryptocoinserver/jesse-optuna",
    install_requires=REQUIRED_PACKAGES,
    entry_points='''
        [console_scripts]
        jesse-bruteforce=jesse_bruteforce.__init__:cli
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    include_package_data=True,
)
