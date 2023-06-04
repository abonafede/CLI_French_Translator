from setuptools import setup, find_packages

# Get the requirements from the requirements.txt file
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="En_to_Fr",
    description="English to French Command Line Translator",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': ['En_to_Fr=translator:main']},
    version="0.0.1",
    author="Andrew Bonafede",
    url="https://github.com/abonafede/CLI_French_Translator",
)