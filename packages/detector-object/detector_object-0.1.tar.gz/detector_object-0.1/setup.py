from setuptools import setup, find_packages

setup(
    name="detector-object",  # نام پروژه در PyPI
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'ultralytics',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'detector-object=detector_object.detect:main',  # تابع اصلی
        ],
    },
    include_package_data=True,
    description="A library for car and license plate detection",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="mahdi",
    author_email="mahdihuseine@gmail.com",
    license="MIT",
)
