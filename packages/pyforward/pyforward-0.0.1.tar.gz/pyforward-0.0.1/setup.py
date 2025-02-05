from setuptools import setup

setup(name='pyforward',
      version='0.0.1',
      description='port forwarding by https://github.com/imranmaj/pyforward?tab=readme-ov-file',
      packages=[
            'pyforward',
            'pyforward/models',
            'pyforward/network'
      ],
      author_email='dev.nevermore696@gmail.com',
      zip_safe=False)