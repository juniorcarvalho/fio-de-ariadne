from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    location = "fio-de-ariadne"
    file_overwrite = False
