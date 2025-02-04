from setuptools import setup, find_packages

setup(
    name='neuropacs',
    version='1.8.6',
    description='neuropacs Python API',
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Kerrick Cavanaugh',
    author_email='kerrick@neuropacs.com',
    url='https://github.com/neuropacs/neuropacs-py-sdk',
    packages=find_packages(),
    install_requires=[
        'cryptography>=41.0.1',
        'pycryptodome>=3.20.0',
        'requests>=2.31.0',
        'requests-toolbelt>=1.0.0',
        'dicomweb-client>=0.59.3',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Healthcare Industry',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)

# To update this package:
# 1. ENSURE ALL KEYS ARE REMOVED
# 2. Remove /build /dist /neuropacs.egg-info
    # rm -rf ./build ./dist ./neuropacs.egg-info
# 3. Update version in setup.py and __init__.py
# 4. Run: python setup.py sdist bdist_wheel
# 5. Run: twine upload dist/*
