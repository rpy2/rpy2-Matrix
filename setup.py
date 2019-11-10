from disutils import setup

pack_version = __import__('rpy2_Matrix').__version__

if __name__ == '__main__':
    setup(
        name='rpy2_Matrix',
        version=pack_version,
        description='Mapping the R package Matrix',
        license='GPLv2+',
        requires=['rpy2'],
        package_dir='rpy2_Matrix',
        classifiers=['Programming Language :: Python',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.7',
                     'Programming Language :: Python :: 3.8',
                     ('License :: OSI Approved :: GNU General '
                      'Public License v2 or later (GPLv2+)'),
                     'Intended Audience :: Developers',
                     'Intended Audience :: Science/Research',
                     'Development Status :: 5 - Production/Stable']
    )
