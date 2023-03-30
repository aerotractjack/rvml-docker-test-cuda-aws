FROM raster-vision-pytorch:latest
WORKDIR /app
COPY test_cuda_aws.py ./
CMD [ "python3", "test_cuda_aws.py"]
