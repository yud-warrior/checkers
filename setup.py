from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='english_checkers',
      version='0.1',
      description='The English chekers game simulation package',
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='chekers draughts boardgame',
      url='http://github.com/yud-warrior/checkers',
      author='Rodion Iudenko',
      author_email='rodionyudenko@gmail.com',
      license='MIT',
      packages=['chekers'],
      install_requires=[
          'markdown',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['funniest-joke=funniest.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)