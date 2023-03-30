# Basic usage of deploying custom RasterVision apps on `docker`

### Setup steps:
1. clone the (`rastervision`)[https://github.com/azavea/raster-vision] repository
2. build the `raster-vision-pytorch:latest` image locally 
```
cd /path/to/rastervision/
chmod +x docker/build
docker/build
```

### Usage steps:
1. clone this repository
2. create and run a container based off the pre-built `raster-vision-pytorch` image
```python
cd /path/to/this/repository
chmod +x ./start.sh
./start.sh
```
