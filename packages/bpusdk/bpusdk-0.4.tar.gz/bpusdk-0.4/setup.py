from setuptools import setup, find_packages

setup(
    name='bpusdk',
    version='0.4',
    license='MIT',
    author="GDIIST",
    author_email='739503445@qq.com',
    packages=find_packages('src','Tests','Models'),
    package_dir={'': 'src', '': 'Tests', '': 'Models'},
    install_requires=['brainpy>=2.4.2'],
)
