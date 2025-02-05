from setuptools import setup, find_packages

setup(
    name='t5omass', 
    version='1.3',
    packages=find_packages(),
    install_requires=[
        'requests',
        'uuid',
        'user_agent'
        
    ],
    author='t5omas',
    author_email='t5omas@mail.com',
    description='This is a library to check email (Hotmail, Gmail) if is availabe, get instagram information by usernam, get reset of user instagram, check if email registered in instagram, And many more features that may be added soon.',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',
    url='https://t.me/t5omas',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)