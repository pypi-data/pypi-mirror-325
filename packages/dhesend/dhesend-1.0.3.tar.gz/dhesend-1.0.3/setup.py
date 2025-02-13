from setuptools import setup, find_packages

setup(
    name="dhesend",
    version="1.0.3",
    packages=find_packages(),
    install_requires=[
        "requests>=2.32.3"
    ],
    description="Dhesend Official Python SDK.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Dhesend",
    author_email="",
    url="https://github.com/dhesend/dhesend-python",
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)