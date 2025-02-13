from setuptools import setup, find_packages

setup(
    name="mahdi-detect",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'ultralytics',
        'opencv-python',
        'numpy',
        'torch',  # اگر نیاز به PyTorch دارید
    ],
    include_package_data=True,  # این گزینه به شما کمک می‌کند که مدل‌ها و فایل‌های اضافی را نیز شامل کنید
    package_data={
        'mahdi_detect': ['license_plate_detector.pt', 'yolov8n.pt'],
    },
    author="Mahdi",
    author_email="mahdihuseine001@gmail.com",
    description="A library for vehicle and license plate detection.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://pypi.org/project/mahdi-detect/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
