# CS Python File Wrapper

## Quick Start
### Install

#### Pip
```
pip install 
```

To resolve packages using pip, add the following to `~/.pip/pip.conf`:
```python
[global]
index-url = https://<USERNAME>:<PASSWORD>@bergsalex.jfrog.io/artifactory/api/pypi/bergsalex-pypi/simple
```
If credentials are required they should be embedded in the URL. To resolve packages using pip, run:
```
pip install "jax-cs-storage"
```

#### Poetry
In your project's `pyproject.toml` file, add:
```
[[tool.poetry.source]]
name = "jfrogbergsalex"
url = "https://bergsalex.jfrog.io/artifactory/api/pypi/bergsalex-pypi/simple"
```

If the repository is password protected, add:
```
poetry config http-basic.jfrogbergsalex <YOUR-EMAIL>
```
You will be prompted for your password:
```
Password: 
```

Then you can run:
```
poetry add jax-cs-storage
```

#### Docker
##### Pip
Add the following to the top of your `requirements.txt` file:
```
--extra-index-url "https://bergsalex.jfrog.io/artifactory/api/pypi/bergsalex-pypi/simple"
```

##### Poetry
The `[[tool.poetry.source]]` configuration above should handle resolving to the right repository.

##### Access restricted repositories
TBD

### Setup
The file wrapper uses pydantic to get configuration from a .env file by default. The steps to 
customize this behavior are discussed in more detail in later sections.

For now, you'll need to at least have the following in you `.env`
```dotenv
JAX_CS_STORAGE_GCS_BUCKET = 'YOUR_BUCKET_NAME'
```
### Usage

#### Create a file from in memory content

```python
from jax.cs.storage import StorageObjectIngest

# You could also configure the package with `jax.cs.storage.init` in a namespace of you choice
# from .files import StorageObject, StorageObjectIngest

content = 'This is some in memory content'
filename = 'SomeGeneratedName.txt'
wrapped = StorageObjectIngest(content, from_memory=True).ingest(filename=filename)
```

#### Allow a user to create a file in Google Cloud Storage
Google cloud storage allows you to generate a signed url to allow user uploads to a specific 
location in object storage, without providing the user with explicit credentials to write to
that object storage bucket.

```python
from jax.cs.storage import StorageObject, ObjectSvcGCS

desired_gs_url = 'gs://some_gs_url'
wrapped = StorageObject(desired_gs_url, file_svc=ObjectSvcGCS)
user_upload_url = wrapped.user_upload_url(content_type='image/png')
```

#### Look up a file by name

```python
# `ObjectSvcGCS` is where `jax.cs.storage stores files in the default configuration,
# you should use whichever service you use with you StorageObjectIngest
from jax.cs.storage.object.services.gcs import ObjectSvcGCS

filename = 'SomeGeneratedName.txt'
all_files = ObjectSvcGCS.all()
found = filename in all_files
```

#### Cache by unique file name

```python
from jax.cs.storage import StorageObject, StorageObjectIngest
# `ObjectSvcGCS` is where `jax.cs.storage stores files in the default configuration,
# you should use whichever service you use with you StorageObjectIngest
from jax.cs.storage.object.services.gcs import ObjectSvcGCS


def check_if_exists():
    filename = 'SomeGeneratedName.txt'
    all_files = ObjectSvcGCS.all()
    found = filename in all_files

    if found:
        wrapped = StorageObject(filename)
    else:
        content = 'some_generated_content'
        wrapped = StorageObjectIngest(content, from_memory=True).ingest(filename=filename)

    return wrapped.user_url
```

#### Get a wrapped version of an existing file

```python
from jax.cs.storage import StorageObject


def get_file_for_user(known_file_location: str):
    # Get the wrapped file
    wrapped = StorageObject(known_file_location)
    # Return information about the file to a user
    return {'name': wrapped.user_name, 'location': wrapped.user_url}
```


## Configuration

### Settings
The following pydantic Settings class is used to configure the library. By 
default, these values will be populated automatically from a `.env` config file. 
The `.env` can have both your application configuration as well as the library 
configuration side by side:
```dotenv
LOG_LEVEL = 'DEBUG'
JAX_CS_STORAGE_GCS_BUCKET = 'fake-bucket'
JAX_CS_STORAGE_GCS_PREFIX_DIR = None
JAX_CS_STORAGE_GCS_CHECK_BLOB_EXISTS = True
JAX_CS_STORAGE_R2_BASE_URL 'https://r2.jax.org
# You should comingle application and library config variables
APPLICATION_SPECIFIC_CONFIG = 'something'
APPLICATION_SPECIFIC_CONFIG_2 = 'something_else'
JAX_CS_STORAGE_IO_FILE_ROOT = '/path/to/local/storage/root'
```

If you need to manually set the configuration of the library, you can do so with
the special `init` entrypoint method.

```python
from jax.cs.storage import init
from jax.cs.storage.config import StorageConfig

StorageObject, StorageObjectIngest = init(
    StorageConfig.parse_obj({
        'GCS_BUCKET': '1',
        'R2_BASE_URL': 'https://r2.jax.org/test',
        'GCS_PREFIX_DIR': '3',
        'GCS_CHECK_BLOB_EXISTS': False,
        'IO_FILE_ROOT': '/path/to/local/storage/root'
    })
)
```

You can use standard Pydantic methods to create the settings instance. 
E.g. from a dictionary:

```python
from jax.cs.storage import init
from jax.cs.storage.config import StorageConfig

my_dict_config = {
    'GCS_BUCKET': '1',
    'R2_BASE_URL': 'https://r2.jax.org/test',
    'GCS_PREFIX_DIR': '3',
    'GCS_CHECK_BLOB_EXISTS': False}
StorageObject, StorageObjectIngest = init(StorageConfig.parse_obj(my_dict_config))
```

The underlying settings class looks like:
```python
from typing import Optional
from pydantic import AnyHttpUrl, BaseSettings

class StorageConfig(BaseSettings):
    """The pydantic configuration class definition for the jax.cs.storage package."""

    LOG_LEVEL: str = 'DEBUG'

    GCS_BUCKET: Optional[str] = None
    GCS_PREFIX_DIR: Optional[str] = None
    GCS_URL_EXPIRE_HOURS: int = 24
    GCS_CHECK_BLOB_EXISTS: bool = True
    R2_BASE_URL: AnyHttpUrl = 'https://r2.jax.org'
    IO_FILE_ROOT: Optional[str] = '/'

    class Config:
        """The config class for pydantic object.

        Used here to configure the default means of determining settings for the package.
        """

        env_prefix = 'JAX_CS_STORAGE_'
        case_sensitive = True
        env_file = ".env"
```

### Wrapper Config
#### Default Service
The default service is the concrete ObjectSvc implementation that the StorageObject will fall back to if
no other service can validate the file. To set the default wrapper service set the `default_svc` 
argument on the `init` call:

```python
from jax.cs.storage import init, ObjectSvcGCS

StorageObject, StorageObjectIngest = init(default_svc=ObjectSvcGCS)
```

#### Available Services
The available services are an ordered list of concrete ObjectSvc implementations in which the order of
the list is the order of precedence of the services. To set the list of available services, use the 
`services` argument on the `init` call:

```python
from jax.cs.storage import init, ObjectSvcGCS, ObjectSvcR2, ObjectSvcIO

StorageObject, StorageObjectIngest = init(
    services=[ObjectSvcGCS, ObjectSvcIO, ObjectSvcR2])
```

#### Ingestion Service
To set how files are ingested using the StorageObjectIngest, pass an alternate concrete implementation
of the ObjectIngestSvc abstract class as the `ingestion_svc` argument on the `init` call:

```python
from jax.cs.storage import init, ObjectIngestSvcGCS

StorageObject, StorageObjectIngest = init(ingestion_svc=ObjectIngestSvcGCS)
```

#### Configure app instance to use a specific Ingestion service
This example shows how you could dynamically configure the library to use different file ingestion
services in different scenarios.

```python
from jax.cs.storage import init
from jax.cs.storage.object.services.io import ObjectIngestSvcIO
from jax.cs.storage.object.services.gcs import ObjectIngestSvcGCS

# This could be a boolean value taken from your app config
use_gcs = False
ingestion_svc = ObjectIngestSvcGCS if use_gcs else ObjectIngestSvcIO
StorageObject, StorageObjectIngest = init(
    ingestion_svc=ingestion_svc
)
```

## Contributing

### Static Checkers

#### Python syntax and style: `flake8`
Flake8 is pre-configured with the .flake8 file from this repository. Just run the following.
```bash
python -m flake8 src/jax
```

#### Docstring existence and format: `pydocstyle`
Service implementations inherit their docstrings from their abstract class, we ignore D102 for the
service.py files.

Pydocstyle is configured in the `pyproject.toml` file at the root of this repository.

##### Check non-service files
````bash
pydocstyle src/jax/cs/storage/ 
````

##### Check services
```bash
pydocstyle src/jax/cs/storage/object/services --match='service.py' --add-ignore=D102
```

#### Known security vulnerabilities: `bandit`
```bash
bandit -r src/jax/cs/storage
 ```

e.g.
```
$ bandit -r src/jax/cs/storage
[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.7.12
Run started:2022-01-21 14:02:01.153764

Test results:
        No issues identified.

Code scanned:
        Total lines of code: 1143
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0.0
                Low: 0.0
                Medium: 0.0
                High: 0.0
        Total issues (by confidence):
                Undefined: 0.0
                Low: 0.0
                Medium: 0.0
                High: 0.0
Files skipped (0):
```

#### Dependency license analysis: `liccheck`
Liccheck is configured in the `[tools.liccheck]` section of the `pyproject.toml` file.

```
liccheck
```

e.g.
```bash
$ liccheck
gathering licenses...
8 packages and dependencies.
check authorized packages...
8 packages.
```