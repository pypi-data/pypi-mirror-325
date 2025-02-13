from setuptools import setup, find_packages

def load_requirements(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()
    
#print(load_requirements("requirements.txt"))

setup(
    name='Ornator',
    version='0.0.1',
    description='A Python library for simplifying HTTP integrations with REST APIs, featuring decorators for authentication handling and request management.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Conectar Wali SAS',
    author_email='dev@conectarwalisas.com.co',
    url='https://github.com/ConectarWali/Ornator',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
    ],
    license_files=['LICENSE'],
    python_requires='>=3.9',
)
