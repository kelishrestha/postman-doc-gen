from setuptools import setup, find_packages

setup(name='postman_doc_gen',

      version='1.1.3',

      url='https://github.com/kelishrestha/postman-doc-gen.git',

      license='MIT',

      author='Kelina Shrestha',

      author_email='kylesth@gmail.com',

      description='Converts a postman collection into an HTML documentation',

      packages=find_packages(exclude=['tests']),

      long_description=open('README.md').read(),

      zip_safe=False,

      setup_requires=['fastjsonschema>=2.14', 'Jinja2>=2.11', 'MarkupSafe>=1.1'],
      python_requires='>=3.0')
