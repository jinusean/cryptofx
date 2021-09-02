from setuptools import setup, find_packages
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(name='cryptofx',
      version='0.1.0',
      author='jinusean',
      pymodules=['cryptofx'],
      packages=find_packages(),
      install_requires = [requirements],
      entry_points='''
          [console_scripts]
          cfx=cryptofx.main:main
      '''
)
