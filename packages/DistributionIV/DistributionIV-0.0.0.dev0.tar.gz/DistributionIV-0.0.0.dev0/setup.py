from setuptools import setup, find_packages


with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    install_requires = [l.strip() for l in f]
    

setup(
    name='DistributionIV',
    version='0.0.0.dev0',
    description='Distributional Instrumental Variable Method',
    author='Xinwei Shen',
    author_email='xinwei.shen@stat.math.ethz.ch',
    install_requires=install_requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    license="BSD 3-Clause License",
)