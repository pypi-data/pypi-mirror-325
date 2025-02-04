from setuptools import setup, find_packages

setup(
    name="hari_rr",
    version="0.1.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="A collection of ML algorithms including Decision Trees, SVM, XGBoost, etc.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/hari_rr",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        'matplotlib'
       
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
