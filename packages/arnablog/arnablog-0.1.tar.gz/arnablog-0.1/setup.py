from setuptools import setup, find_packages

setup(
    name="arnablog",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "arnablog=arnablog.add_to_changelog:main",
        ],
    },
    author="Your Name",
    description="A CLI tool to add entries to a changelog file",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
