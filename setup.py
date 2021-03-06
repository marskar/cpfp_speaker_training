import setuptools

with open("README.rst", "r") as f:
    long_desc = f.read()

setuptools.setup(
    name='cpfp_speaker_training',
    version='0.0.1',
    description='Training for the CPFP Fellows Research Meeting',
    long_description=long_desc,
    long_description_content_type="text/x-rst",
    author='Martin Skarzynski',
    url='https://www.github.com/marskar/cpfp_speaker_training/',
    license='MIT',
    packages=setuptools.find_packages(where='src'),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
