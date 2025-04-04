# Packager

A command-line tool for managing Singularity images and creating executable bundles.

## Installation

```bash
pip install .
```

## Configuration

The configuration file is stored at `~/.config/packager.ini`:

```ini
[packager]
singularity_path = /path/to/images
bin_path = /path/to/bin
packages_path = /path/to/packages

[images]
# This section is automatically populated by the tool
```

## Usage

### Add a set of singularity images
```bash
# From singularity_path
packager scanpackages
# From custom path
packager scanpackages --dir /qib/platforms/Informatics/transfer/outgoing/singularity/core
```

### Add single singularity image as package
```bash
bashpackager addpackage --image /path/to/image.simg --name mypackage --version 1.0.0
```


### Create a "HPC package" (bundle)
```bash
# Make an empty bundle
packager makebundle --name mybundle

# Make a bundle with one or more packages
packager makebundle --name denovo megahit=1.2.9 fastp=1.20.0
```

### Add package to bundle
```bash
# By default each package is exposed as a binary called package. You can add "aliases" i.e. each binary to expose
packager addtobundle --name mybundle --package blast --version 1.0 blastn makeblastdb blastp
```