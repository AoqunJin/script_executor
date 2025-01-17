from setuptools import setup, find_packages

setup(
    name='script_executor',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'script-executor=script_executor.cli:main'
        ],
    },
    author='Ao-Qun',
    description='A script execution manager supporting various command executions.',
    url='',
)