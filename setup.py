#from distutils.core import setup
from setuptools import find_packages, setup

setup(
    name                = 'NeatSeq-Flow-tutorial',
    version             = '1.1.0',
    author              = 'Liron Levin and Menachem Sklarz',
    author_email        = 'levinl@post.bgu.ac.il',
    maintainer          = 'Menachem Sklarz',
    maintainer_email    = 'sklarz@bgu.ac.il',
    url                 = 'https://github.com/bioinfo-core-BGU/neatseq-flow-tutorial', # Change to readthe docs tutorial section
    description         = 'Files for the NeatSeq-Flow tutorial',
    license             = 'Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description    =  open('README').read(),
    download_url        = 'https://github.com/bioinfo-core-BGU/neatseq-flow-tutorial',
    platforms           = ["POSIX","Windows"],
    data_files          = [('TUTORIAL',['Example_WF_conda_env.yaml',
                                        'Example_WF.yaml',
                                        'Example_WF_from_ftp.yaml']),
                            ('TUTORIAL/Sample_sets',['Samples_from_FTP.nsfs',
                                                     'Samples.nsfs',
                                                     'Samples_conda.nsfs']),
                            ('TUTORIAL/Data',[  'Sample_sets/Sample1.F.fastq',
                                                'Sample_sets/Sample1.R.fastq',
                                                'Sample_sets/Sample1.fasta',
                                                'Sample_sets/Sample2.F.fastq',
                                                'Sample_sets/Sample2.R.fastq',
                                                'Sample_sets/Sample2.fasta',
                                                'Sample_sets/Sample3.F.fastq',
                                                'Sample_sets/Sample3.R.fastq',
                                                'Sample_sets/Sample3.fasta'])],
    # install_requires    = [],
    classifiers         = [
                          'Development Status :: 4 - Beta',
                          'Environment :: Console',
                          'Intended Audience :: End Users',
                          'Intended Audience :: Developers',
                          'License :: OSI Approved :: Python Software Foundation License',
                          'Operating System :: Microsoft :: Windows',
                          'Operating System :: POSIX',
                          'Programming Language :: Python',
                          ],
    )
    

    
