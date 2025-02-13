from setuptools import setup

setup(
    name='bmobpy',
    version='1.10.1',
    packages=['bmobpy'],
    install_requires=[
        'websockets',
        'requests'
    ],
    author='www.bmobapp.com',
    author_email='admin@bmobapp.com',
    description='Bmob后端云的Python SDK',
    license='MIT',
    keywords='Bmob后端云 Python SDK',
    url='https://www.bmobapp.com'
)