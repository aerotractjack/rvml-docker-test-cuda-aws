import rastervision
import torch
import boto3
import io
import time

now = str(int(time.monotonic()))

foo = f"{str(rastervision)}, {torch.cuda.is_available()}"
contents = io.BytesIO(bytes(foo, "utf-8"))
s3 = boto3.client('s3')
print(contents.read())
contents.seek(0)
s3.upload_fileobj(contents, "aerotrest", f"test-{now}.txt")
print("Donezo!")
