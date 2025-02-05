from setuptools import setup, find_packages

setup(
    name='DeepDrishti',
    version='0.0.3',
    author="Atanu Debnath",
    author_email="playatanu@gmail.com",
    description="A set of python modules for Computer Vision",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/playatanu/DeepDrishti",
    project_urls={
        "Documentation": "https://playatanu.github.io/DeepDrishti",
        "Source": "https://github.com/playatanu/DeepDrishti",
        "Tracker": "https://github.com/playatanu/DeepDrishti/issues",
    },
    packages=find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        "pillow>=11.1.0",
        "numpy>=2.2.1",
        "torch>=2.6.0",
        "torchvision>=0.21.0",
        "tqdm>=4.67.1", 
    ],
    python_requires='>=3.10',
    
)