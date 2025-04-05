from setuptools import setup, find_packages

setup(
    name="stalowa_bukmacherska",  # Replace with your project name
    version="0.3.0",
    author="BARTOSZ RADOMSKI",  # Replace with your name
    author_email="your_email@example.com",  # Replace with your email
    description="A description of your project",  # Add a short description of your project
    long_description=open('README.md').read(),  # Read the content from README file
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/your_project_name",  # Replace with the URL of your project
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy>=1.20.0",  # Example dependencies
        "matplotlib>=3.4.0",
        "scipy>=1.6.0",
        "scikit-learn>=0.24.0",
    ],
    python_requires='>=3.6',  # Python version requirement
)
