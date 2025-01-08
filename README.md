# postman-doc-gen

Generate HTML API documentation from a postman collection. You can use this tool to auto-generate the documentation with postman environment variables.

## How to use

1. Download the latest release of the executable from <a href="https://github.com/kelishrestha/postman-doc-gen/releases"> here</a>.
2. Open a new terminal and call the executable using the following command

  ```
  ./postman_doc_gen [path_to_collection] -o [path_to_output_folder]
  ```

  To apply environment values to the examples, use the following command -

  ```
  ./postman_doc_gen [path_to_collection] -o [path_to_output_folder] -e [path_to_environment_json_file]
  ```

  To enable download links to collection, use the following command

  ```
  ./postman_doc_gen [path_to_collection] -o [path_to_output_folder] -e [path_to_environment_json_file] -d true
  ```

The output folder should now show the following:

1. index.html - this is the html documentation generated from the collection
2. css - this is the css folder consisting of the necessary css files
3. js - this is the javascript folder consisting of the required js files


## Development Guidelines

Pre-requisites:
* Python v3.9

### Steps for development
1. Create a virtual env (recommended but optional)
  ```
  python -m venv venv
  source ./venv/bin/activate
  ```
2. Install dependencies from the requirements file
  ```
  pip install -r requirements.txt
  ```
3. Create the documentation
  ```
  python postman_doc_gen.py [path/to/collection] -o [path/to/output/folder]
  ```
4. Create new executable using following command
  ```
  pyinstaller postman_doc_gen.spec postman_doc_gen.py
  ```

Note: If you get the following error when running the pyinstaller command
  ```
  OSError: Python library not found: libpython3.7.dylib, .Python, libpython3.7m.dylib, Python, Python3
  ```

then you need to re-install python on your machine with enable-shard & recreate the virtual environment
  ```
  env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.7.14
  ```

## Dependencies


The following tools/repos have been instrumental in building this tool

- <a href="https://palletsprojects.com/p/jinja/">Jinja</a>
- <a href="https://github.com/pyinstaller">PyInstaller</a>
- <a href="https://giphy.com/apps/giphycapture">Giphy Capture</a>
- <a href="https://pypi.org/project/bleach/">Bleach</a>
