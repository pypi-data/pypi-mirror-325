from setuptools import setup, find_packages

setup(
    name='rokon',                          # The name of the package
    version='0.1.0',                       # Version of the package
    packages=find_packages(),              # Automatically find all the packages inside 'rokon' folder
    install_requires=[                     # External dependencies
        'tensorflow',                      # Include TensorFlow if necessary
        'numpy',                            # Include numpy if necessary
    ],
    # Other metadata
    author='Rokonozzaman Ayon',
    author_email='rokayon.cse@gmail.com',
    description='A package for RNet models and dynamic model loading',
    url='https://github.com/rokayon/rokon',  # Your GitHub URL (optional)
)
