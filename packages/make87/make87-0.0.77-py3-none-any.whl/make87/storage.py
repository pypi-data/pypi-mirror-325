import os
from pathlib import Path


def get_system_storage_path() -> Path:
    """Returns the path to the system storage directory."""
    path = Path("/tmp/make87")
    if "MAKE87_STORAGE_PATH" in os.environ:
        storage_url = os.environ["MAKE87_STORAGE_PATH"]
        endpoint_url = os.environ["MAKE87_STORAGE_ENDPOINT_URL"]
        access_key = os.environ.get("MAKE87_STORAGE_ACCESS_KEY")
        secret_key = os.environ.get("MAKE87_STORAGE_SECRET_KEY")

        try:
            from s3path import S3Path
            from s3path.old_versions import _S3Accessor

            S3Path._accessor = _S3Accessor(
                endpoint_url=endpoint_url,
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key
            )

            path = S3Path(storage_url)

        except ImportError:
            raise ImportError(
                "Please install make87[storage] to use the cloud storage functionality."
            )

    path.mkdir(parents=True, exist_ok=True)
    return path
