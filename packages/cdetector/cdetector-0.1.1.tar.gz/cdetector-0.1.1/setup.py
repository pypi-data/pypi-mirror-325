from setuptools import setup, find_packages

setup(
    name='cdetector',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={'cdetector': ['../models/*.pt']},
    install_requires=[
        'opencv-python',
        'numpy',
        'ultralytics',
        'easyocr'
    ],
    description='A license plate and vehicle detector using YOLO and EasyOCR.',
    author='Your Name',
    author_email='Mahdihuseine001@gmail.com',
    url='https://pypi.org/project/cdetector/',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
