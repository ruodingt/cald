from os import path

import setuptools

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'INSTRUCTIONS/README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='auto_template',
    version='0.1',
    description='A general utility package for BizAI.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ruodingt/cald',
    author='Rod (Ruoding) Tian',
    author_email='t.ruoding@gmail.com',
    license="N/A",
    include_package_data=True,
    package_data={
    },
    packages=setuptools.find_packages(),
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'click==8.0.0'
    ],
    python_requires='>=3.6',
    keywords=[
        'calendar'
    ],
    entry_points='''
        [console_scripts]
        cald=caldiff.cli:cald
    ''',
)
