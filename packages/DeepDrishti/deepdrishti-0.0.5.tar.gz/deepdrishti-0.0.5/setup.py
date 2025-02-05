from setuptools import setup, find_packages

setup(
    name='DeepDrishti',
    version='0.0.5',
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
        "pillow",
        "numpy",
        "torch",
        "torchvision",
        "tqdm", 
    ],
    python_requires='>=3.10',
    
)