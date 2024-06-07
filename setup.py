from setuptools import setup, find_packages

print(find_packages())

setup(
   name='spoorschavuiten',
   version='1.0',
   description='A useful module',
   author='Sverre',
   author_email='',
   packages=['spoorschavuiten'],  #same as name
   
   install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
)