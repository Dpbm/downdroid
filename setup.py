from setuptools import setup, find_packages

setup(
    name='downdroid',
    description='A CLI tool to download android versions',
    author="Dpbm",
    url="https://github.com/Dpbm/downdroid",
    scripts=["bin/downdroid"],
    license="MIT",
    license_files="LICENSE*",
    keywords=[
        "android",
        "android-X86",
        "ISO",
        "systems",
        "linux",
        "virtualization",
        "CLI",
        "cli-tool"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    version='0.0.1',
    packages=find_packages(where=['downdroid', 'downdroid/utils']),
    install_requires=[
        'requests-html',
        'tqdm'
    ],
)
