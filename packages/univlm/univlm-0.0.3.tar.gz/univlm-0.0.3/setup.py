from setuptools import setup, find_packages

setup(
    name='univlm',  # Name of your package
    version='0.0.1',  # Version of your package
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'huggingface_hub>=0.20.2',
        'transformers>=4.35.0',
        'diffusers>=0.24.0',
        'fuzzywuzzy>=0.18.0'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'your-package-install=src.post_install:run_script',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS POSIX :: Linux',
    ],
)
