from setuptools import setup, find_packages

setup(
    name="ansible_targetnode_setup",
    version="0.1",
    author="Mohammad Noorain",
    author_email="your-email@example.com",
    description="A Python package to automate Ansible TargetNode installation and configuration.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ansible_targetnode_setup = ansible_targetnode_setup.controller:setup_ansible",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    install_requires=[],  # Add dependencies if needed
)
