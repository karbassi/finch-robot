from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='finch-robot',
      version='0.1',
      description='Finch robot USB connection',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='finch robot',
      url='http://github.com/karbassi/finch-robot',
      author='Ali Karbassi',
      author_email='ali@karbassi.com',
      license='MIT',
      packages=['finch-robot'],
      include_package_data=True,
      zip_safe=False)
