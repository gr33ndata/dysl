from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='dysl',
      version='0.1',
      description='Do you speak London?',
      long_description=readme(),
      url='https://github.com/gr33ndata/dysl',
      author='Tarek Amr',
      license='MIT',
      packages=['dysl', 'dysl.dyslib', 'dysl.corpora.corpuslib'],
      zip_safe=False)