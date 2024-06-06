from setuptools import setup, find_packages

setup(
    name='html-table-to-json',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'beautifulsoup4'
    ],
    entry_points={
        'console_scripts': [
            'html-table-to-json=main:main',
        ],
    },
    author='Thiago Schumann',
    author_email='thiagoarturschumann@gmail.com',
    description='Effortlessly convert HTML tables to JSON with this Python-based tool.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ThiagoSchumann/html-table-to-json',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
