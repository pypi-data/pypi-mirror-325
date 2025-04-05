from setuptools import setup, find_packages

setup(
    name="coifstackcommons",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    license='MIT', 
    install_requires=[ "bcrypt" ],                      # Requirements for this packages 
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="coifstackcommons",
    author_email = 'urtatsberrocal@gmail.com', 
    download_url = 'https://github.com/Urtats-Code/coifstack-commons/archive/refs/tags/v_01.tar.gz', 
    keywords = ['utils', 'authentification', 'response', 'validation'], 
    url="https://github.com/Urtats-Code/coifstack-commons",
      classifiers=[
    'Development Status :: 3 - Alpha',      

    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',

     'License :: OSI Approved :: MIT License',

    'Programming Language :: Python :: 3',      
  ],

)   