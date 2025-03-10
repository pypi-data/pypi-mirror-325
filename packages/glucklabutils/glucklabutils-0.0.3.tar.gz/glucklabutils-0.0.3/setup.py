from setuptools import setup, find_packages

VERSION = "0.0.3" 
DESCRIPTION = "GluckLab utils"
LONG_DESCRIPTION = "GluckLab useful tools"

# Setting up
setup(
        name="glucklabutils", 
        version=VERSION,
        author="Jose Mojica Perez",
        author_email="jlmojicaperez@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["pandas"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'

        keywords=["python"],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
