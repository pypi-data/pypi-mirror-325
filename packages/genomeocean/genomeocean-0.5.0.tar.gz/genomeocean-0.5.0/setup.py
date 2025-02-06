import setuptools

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name='genomeocean',
    version='0.5.0',
    author='Zhong Wang',
    author_email='zhongwang@lbl.gov',
    description='A Python library for GenomeOcean inference and fine-tuning.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jgi-genomeocean/genomeocean",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy==1.26.4",
        "torch==2.4.0",
        "biopython==1.83",
        "einops==0.7.0",
        "transformers==4.44.2",
        "vllm==0.6.1.post2",
        "flash-attn==2.6.3",
        "triton==3.0.0",
        "tqdm==4.66.4",
        "scikit-learn==1.5.0",
        "pyrodigal==3.6.3",
        "peft==0.14.0",
        "wandb==0.19.4",
        ],
    classifiers=[
        'Programming Language :: Python :: 3.8', 
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10', 
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
