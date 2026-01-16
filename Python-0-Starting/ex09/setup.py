from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='ft_package',
    version='0.0.1',
    author='eagle',
    author_email='eagle@42.fr',
    description='A sample test package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/eagle/ft_package',
    packages=find_packages(),
    python_requires='>=3.6',
    license='MIT',
)
