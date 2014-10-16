from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='dysl',
      version='0.13',
      description='Do you speak London?',
      long_description=readme(),
      url='https://github.com/gr33ndata/dysl',
      author='Tarek Amr',
      license='MIT',
      packages=['dysl', 
                'dysl.dyslib', 
                'dysl.corpora', 
                'dysl.corpora.corpuslib'],
      include_package_data=True,
      zip_safe=False)
