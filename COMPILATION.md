# Compilation details

## Compiling the Anaconda package on Windows

Install Microsoft Visual Studio Community Edition and modify the version
numbers and directory paths as provided in `setup.py`.

Start the compilation with
```
conda build .
```

## Compilation for Linux/Anaconda on Windows using Docker

For the Windows terminal, I use Git Bash as readily available in
Git for Windows. Furthermore, make sure that Docker is installed.
Construct the build environment by building the Docker image
```
docker build . -t pylebedev-anaconda -f Dockerfile-linux-anaconda
```

Modify the `build_docker_linux_anaconda.sh` file and set the `ROOT` variable to the root
folder of this repository. Next, run the `docker_setup.sh` script

```
./build_docker_linux_anaconda.sh
```

After compilation, you will automatically be prompted whether to upload
the freshly generated packages.

## Compiling for Linux/PyPi on Windows using Docker

For the Windows terminal, I use Git Bash as readily available in
Git for Windows. Furthermore, make sure that Docker is installed.
Construct the build environment by building the Docker image
```
docker build . -t pylebedev-pypi -f Dockerfile-linux-pypi
```

Modify the `build_docker_linux_pypi.sh` file and set the `ROOT` variable to the root
folder of this repository. Next, run the `docker_setup.sh` script

```
./build_docker_linux_pypi.sh
```

### Uploading to PyPi

This will place wheels in the `dist` folder. To upload these wheels
to PyPi, make sure you have `twine` installed using

```
pip install twine
```

To upload, run

```
python -m twine upload dist/*
```
