from setuptools import setup, find_packages
exec(open('kdpy_imagen/version.py').read())

setup(
  name = 'kdpy-imagen',
  packages = find_packages(exclude=[]),
  include_package_data = True,
  entry_points={
    'console_scripts': [
      'kdpy_imagen = kdpy_imagen.cli:main',
      'imagen = kdpy_imagen.cli:imagen'
    ],
  },
  version = __version__,
  license='MIT',
  description = 'Imagen - unprecedented photorealism × deep level of language understanding',
  author = 'NKDuy',
  author_email = 'kn145660@gmail.com',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/khanhduy1407/kdpy-imagen',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'transformers',
    'text-to-image',
    'denoising-diffusion'
  ],
  install_requires=[
    'accelerate',
    'click',
    'einops>=0.4',
    'einops-exts',
    'ema-pytorch>=0.0.3',
    'fsspec',
    'kornia',
    'numpy',
    'packaging',
    'pillow',
    'pydantic',
    'pytorch-lightning',
    'pytorch-warmup',
    'sentencepiece',
    'torch>=1.6',
    'torchvision',
    'transformers',
    'tqdm'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
