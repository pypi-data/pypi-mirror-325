import setuptools

# Reads the content of your README.md into a variable to be used in the setup below.
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    # Package Information:
    name='r4ven_utils',
    packages=['r4ven_utils'], # Should match the package folder.
    version='0.1.1',
    license='GPLv3',

    # Description Information:
    description='The companion that holds your grab-bag of utility functions and objects',
    long_description=long_description,
    long_description_content_type="text/markdown",

    # Author Information:
    author='Victor Vinci Fantucci',
    author_email='victor.v.fantucci@gmail.com',
    url='https://github.com/VictorFantucci/r4ven_utils_dev',

    # Project URLs:
    project_urls =
    {
        "Bug Tracker": "https://github.com/VictorFantucci/r4ven_utils_dev/issues",
        "Download": "https://github.com/VictorFantucci/r4ven_utils/releases/tag/alpha"
    },

    # Project Requirements:
    install_requires=[],

    # Project Descriptive meta-data:
    keywords=['r4ven_utils', 'utils', 'logs'],

    # Project Classifiers:
    classifiers=
    [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ]
)
