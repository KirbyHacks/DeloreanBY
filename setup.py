from setuptools import setup

setup(
    name='deloreanby',
    version='0.1.0',    
    description='A Python package that bypasses advertisements to streamline user experiences with content.',
    url='https://github.com/KirbyHacks/DeloreanBY',
    author='! rL⌀w',
    author_email='bytebvrd@gmail.com',
    license='MIT',
    packages=['deloreanby'],
    install_requires=['urllib3',
                      'aiohttp',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)