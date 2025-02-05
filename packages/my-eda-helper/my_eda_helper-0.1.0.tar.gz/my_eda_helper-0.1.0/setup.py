from setuptools import setup, find_packages

setup(
    name="my_eda_helper",  # Package name
    version="0.1.0",    # Initial version
    author="Bidut Sharkar Shemanto",
    author_email="shemantosharkarofficial@gmail.com",
    description="A helper package for Exploratory Data Analysis (EDA)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shemanto27/eda-helper-py",  
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "seaborn",
        "matplotlib",
        "scipy",
        "statsmodels",
        "scikit-learn",
        "wordcloud",
        "IPython"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
