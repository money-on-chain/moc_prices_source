from setuptools        import setup, find_packages
from moc_prices_source import __version__ as version

with open("README.md", "r") as file_:
    long_description = file_.read()

with open("requirements.txt", "r") as file_:
    requirements = file_.read().split()

setup(
    name='moc_prices_source',
    version=version,
    packages=find_packages(),
    author='Juan S. Bokser',
    author_email='juan.bokser@moneyonchain.com',
    description='Prices source for MoC projects',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
    package_data={
        "moc_prices_source": ["data/*.json"]
    },
    python_requires='>=3.6',
    install_requires=requirements,
    scripts=['moc_prices_source_check']
)
