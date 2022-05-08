from setuptools import setup

setup(
    name="ares",
    version="0.1.0",
    description="ARES Software package",
    url="",
    author="Henk van den Brink",
    author_email="",
    license="MIT",
    packages=["ares"],
    install_requires=[
        "paho-mqtt==1.5.1",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
    ],
)
