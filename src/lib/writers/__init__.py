from src.lib.writers.file import FileWriter
from src.lib.writers.remotes.s3 import S3RemoteWriter
from src.lib.writers.remotes.s3_presigned_url import S3PresignedUrlRemoteWriter
from src.lib.writers.remotes.gcs import GCSRemoteWriter
from src.lib.writers.\
    remotes.gcs_presigned_url import GCSPresignedUrlRemoteWriter
from src.lib.writers.databases.mysql import (MysqlClientDatabaseWriter,
                                             MysqlDirectDatabaseWriter)
from src.lib.writers.\
    databases.postgresql import (PostgresClientDatabaseWriter,
                                 PostgresDirectDatabaseWriter)

writers = {
    's3-url': S3PresignedUrlRemoteWriter,
    's3': S3RemoteWriter,
    'gcs': GCSRemoteWriter
}

uri_writers = {
    'file': FileWriter,
    'gcs-url': GCSPresignedUrlRemoteWriter
}

database_writers = {
    'mysql-cli': MysqlClientDatabaseWriter,
    'mysql-direct': MysqlDirectDatabaseWriter,
    'postgres-cli': PostgresClientDatabaseWriter,
    'postgres-direct': PostgresDirectDatabaseWriter
}

writers.update(uri_writers)
writers.update(database_writers)
