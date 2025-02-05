from setuptools import setup, find_packages

setup(
    name="frappe-setup",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        'click',
        'docker',
        'docker-compose',
    ],
    entry_points={
        'console_scripts': [
            'frappe-setup=frappe_setup.cli:main',
        ],
    },
    package_data={
        'frappe_setup': ['docker_files/*', 'scripts/*'],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to automate Frappe Framework setup with Docker",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/frappe-setup",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
) 