from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sms4jawaly-sms',
    version='1.0.0',
    description='Python SDK for 4jawaly SMS Gateway',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='4jawaly',
    author_email='support@4jawaly.com',
    url='https://github.com/4jawaly/sms-gateway-python',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'requests>=2.25.0',
        'pydantic>=1.8.0'
    ],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Telephony'
    ],
    keywords='sms, messaging, 4jawaly, gateway',
    project_urls={
        'Bug Reports': 'https://github.com/4jawaly/sms-gateway-python/issues',
        'Source': 'https://github.com/4jawaly/sms-gateway-python'
    }
)
