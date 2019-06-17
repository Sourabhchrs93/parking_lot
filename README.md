# Parking lot

### Quick Start

Initialize and activate a virtualenv:

```
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

Install the dependencies:

```
$ pip install -r requirements.txt
```

Execute the script:

```
$ bin/setup
$ bin/parking_lot {absolute filepath}
$ bin/run_functional_tests
```

key points:
```
- 'filepath' is optional if file path is NOT passed application 
    accepts command line input. 
- use 'exit' to terminate the application
```