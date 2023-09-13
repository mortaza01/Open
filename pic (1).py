from setuptools import setup, find_packages
import os
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='shbomb',
    packages=find_packages(),
    include_package_data=True,
    version="1.0.1",
    description='Powerful Bangladeshi SMS Bombing Tools!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='CyberSH',
    author_email='freelike761@gmail.com',
    #install_requires=[],

  
    keywords=["cybershbd","cyber sh","shbomb","sms bomb","cyber sh bomber","shtasrif bomb","cybersh sms bomber","cybersh bombing"],
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
            'Environment :: Console',
    ],
    
    license='MIT',
    entry_points={
            'console_scripts': [
                'shbomb = shbomb.shbomb:shbomb',
            ],
    },
    python_requires='>=3.9.5'
)
