from setuptools import setup, find_packages

setup(
    name='card_read_lib', 
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        '<cv2>',
        '<easyocr>'
    ],
    author='Lucas',  
    author_email='*****',
    description='Returns card name of magic, pokemon and magic cards',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',

)
