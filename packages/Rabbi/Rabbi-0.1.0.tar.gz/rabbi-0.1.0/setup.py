from setuptools import setup, find_packages

setup(
    name="Rabbi",
    version="0.1.0",
    packages=find_packages(),  
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "seaborn",
        "xgboost",
        "optuna",
    ],
    author="Sarthak Mohapatra",
    description="A machine learning package for preprocessing and model training.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sarthakm402/Automated_ML",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
