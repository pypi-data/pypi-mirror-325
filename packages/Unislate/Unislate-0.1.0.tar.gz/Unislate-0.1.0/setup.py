from setuptools import setup
import sys
import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

install_requires = []
if sys.platform == "win32":
    install_requires.append("windows-curses")

setup(
    name="Unislate",
    version="0.1.0",
    description="Минималистичный консольный редактор с подсветкой синтаксиса",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Qwez",
    url="https://github.com/qwez-source/unislate",    
    py_modules=["unislate"], 
    entry_points={
        "console_scripts": [
            "unislate = unislate:main", 
        ],
    },
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
