from setuptools import setup

setup(
    name='corrscope',
    version='0',
    packages=['corrscope'],
    url='https://github.com/nyanpasu64/corrscope',
    license='BSD-2-Clause',
    author='nyanpasu64',
    author_email='',
    description='',
    # https://docs.pytest.org/en/latest/goodpractices.html
    setup_requires=["pytest-runner"],
    tests_require=['pytest>=3.2.0', 'pytest-pycharm', 'hypothesis', 'delayed-assert'],
    install_requires=[
        'ruamel.yaml>=0.15.70',  # See test_config.py to pick a suitable minimum version
        'numpy', 'scipy', 'click', 'more_itertools',
        'matplotlib',
        'attrs>=18.2.0',
        'PyQt5',
    ]
)
