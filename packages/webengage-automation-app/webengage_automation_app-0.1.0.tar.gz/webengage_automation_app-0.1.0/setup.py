from setuptools import setup, find_packages

setup(
    name="webengage-automation-app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "track=webengage_automation.logger:main",
        ],
    },
    author="Nipun Patel",
    author_email="nipunp27@gmail.com",
    description="Webengage internal tool to send the app logs to their API for testing the data with DataModel",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://www.webengage.com/",
    license="MIT",
    license_files=["LICEN[CS]E.*"], 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)
