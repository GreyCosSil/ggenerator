from src.lib.writers.file import FileWriter
from src.lib.writers.remotes.s3 import S3RemoteWriter
from src.lib.writers.remotes.s3_presigned_url import S3PresignedUrlRemoteWriter
from src.lib.writers.remotes.gcs import GCSRemoteWriter
from src.lib.writers.remotes.gcs_presigned_url import GCSPresignedUrlRemoteWriter

writers = {
    'file': FileWriter,
    's3': S3RemoteWriter,
    'gcs': GCSRemoteWriter
}

uri_writers = {
    's3-url': S3PresignedUrlRemoteWriter,
    'gcs-url': GCSPresignedUrlRemoteWriter
}

writers.update(uri_writers)
