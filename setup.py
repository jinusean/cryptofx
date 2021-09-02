from setuptools import setup, find_packages
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(name='crypto-fx',
      version='0.1.0',
      author='jinusean',
      pymodules=['crypto-fx'],
      packages=find_packages(),
      install_requires = [requirements],
      entry_points='''
          [console_scripts]
          crypto-fx=crypto-fx.main:main
      '''
)
