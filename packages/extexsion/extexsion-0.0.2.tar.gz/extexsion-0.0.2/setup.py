from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='extexsion',
    version='0.0.2',
    description='extexsion',
    long_description=long_description,
    author='huang yi yi',
    author_email='363766687@qq.com',
    packages=find_packages(),
    package_data={
        'extexsion': ['*.pyi'],
    },
    python_requires='>=3.6',
    install_requires=[
        "requests>=2.32.2.post1",
    ],
)