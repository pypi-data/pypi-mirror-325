from setuptools import setup, find_packages

setup(
    name='Gdiist-BPU-Toolkit',
    version='0.2',
    license='MIT',
    author="GDIIST",
    author_email='739503445@qq.com',
    packages = find_packages(exclude=['lib*', 'HardwareConfig']),
    install_requires=['brainpy>=2.4.2'],
)
