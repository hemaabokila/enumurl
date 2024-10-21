from setuptools import setup, find_packages

setup(
    name="url-enumeration",
    version="1.0.0",
    author="Ibrahem abo kila",
    author_email="ibrahemabokila@gmail.com",
    description="A simple URLE numeration tool.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hemaabokila/url-enumeration",
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'colorama',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'enumurl=url.main:main', 
        ],
    },
)

