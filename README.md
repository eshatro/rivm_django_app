# graphql-api

[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)


# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Build system files
Docker, docker-compose.yml and Makefile

# Local Development

For local development build and start the dev server:
```bash
make app-init
```

The above command will pull the pre build image from public docker registry 
and start a django container based on that. 
Alternatively for a local build refer to the Makefile command
```bash
make local-build
```

The rest of the Makefile commands are the same.

Application code: rivm/rivm/*

To check out the auto generated docs visit:
http://localhost:8001/

Application local endpoints: 
1. http://localhost:8000/graphql
2. http://localhost:8000/

Optionally after testing locally tear down the application containers and images by
```bash
make tear-down
```

Run commands inside the docker container:

```bash
make shell
```

To run tests
```bash
make run-tests
```
