from setuptools import setup, find_packages


def read_requirements():
    """Read the requirements.txt file and return a list of dependencies."""
    with open("requirements.txt", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


setup(
    name='CYB600-Lab1-Huff4a',  # Make sure this matches your PyPI name
    version='0.5',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    long_description=open('README.md').read(),  # Read the description from README
    long_description_content_type='text/markdown',
    entry_points={
        "console_scripts": [
            "cyb600-lab1=csc_cyb600_huff4.main:main",  # Adjust based on your package
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)


