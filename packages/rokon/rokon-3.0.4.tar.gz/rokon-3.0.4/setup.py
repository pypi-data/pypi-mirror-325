
# # Version 1.0
# # from setuptools import setup, find_packages 
# # setup(
# # name="rokon", 
# # version="1.0", 
# # packages=find_packages(), 
# # install_requires=[ 
# # 'tensorflow', 
# # ], 
# # description="A lightweight CNN model repository", 
# # author="rokayon", 
# # author_email="rokayon.cse@gmail.com", 
# # ) 

# # Version 2.0
# from setuptools import setup, find_packages
# setup(
#     name="rokon",  # Package name (this will be used in pip install)
#     version="2.0.1",  # Update version as needed
#     author="Rokonozzaman Ayon",
#     author_email="rokayon.cse@gmail.com",
#     description="A collection of  RNet (lightweight CNN) models",
#     long_description=open("README.md").read(),
#     long_description_content_type="text/markdown",
#     url="https://github.com/rokayon/rokon",  # Your GitHub repo
#     packages=find_packages(),
#     install_requires=[
#         "tensorflow",  # Add required dependencies
#         "numpy",
#         "matplotlib",
#     ],
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     python_requires=">=3.6",
# )

# Version 3.0
from setuptools import setup, find_packages

setup(
    name="rokon",  # Package name (this will be used in pip install)
    version="3.0.4",  # Update version as needed
    author="Rokonozzaman Ayon",
    author_email="rokayon.cse@gmail.com",
    description="A collection of RNet (lightweight CNN) models",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rokayon/rokon",  # Your GitHub repo
    packages=find_packages(),
    install_requires=[
        "tensorflow>=2.18.0",  # Ensure compatibility with newer TensorFlow versions
        "numpy>=1.21.0",  # Ensure compatibility with Numpy
        "matplotlib>=3.3.0",  # Ensure compatibility with Matplotlib
        # "visualkeras>=0.0.2",  # Ensure compatibility with Visualkeras
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
