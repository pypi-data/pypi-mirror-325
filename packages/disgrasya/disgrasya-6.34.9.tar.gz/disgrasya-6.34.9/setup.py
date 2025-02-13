from setuptools import setup, find_packages

setup(
    name='disgrasya',
    version='6.34.9',
    description='A utility for checking credit cards through multiple gateways using multi-threading and proxies.',
    author='Jaehwan0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'subprocess32;python_version<"3.2"'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'disgrasya=disgrasya.main:main',
        ],
    },
    package_data={
        'disgrasya': ['tmp/*.mjs'],
    },
)
