from setuptools import setup, find_packages

setup(
    name="od-detect",  # نام پکیج برای نصب با pip
    version="0.1",
    packages=find_packages(),  # جستجوی خودکار ماژول‌ها
    install_requires=[
        'opencv-python',
        'ultralytics',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'od-detect=pd_detector.detect:main',  # اجرای CLI با این نام
        ],
    },
    include_package_data=True,
    description="A library for car and license plate detection",
    long_description="This library provides car and license plate detection using YOLO.",
    long_description_content_type='text/markdown',
    author="mahdi",
    author_email="mahdihuseine@gmail.com",
    license="MIT",
)
