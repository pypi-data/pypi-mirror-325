from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'Gap client package'
LONG_DESCRIPTION = 'Gap client package for connecting apis through functions'

# Setting up
setup(
       # the name must match the folder name 'gapSolutions_client'
        name="gapSolutions_client", 
        version=VERSION,
        author="Samer Hisham",
        author_email="samerrhisham@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'

        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
