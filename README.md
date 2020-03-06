# trvmp-api

[![Actions Status](https://github.com/mymindwentblvnk/trvmp-api/workflows/Tests/badge.svg?branch=develop)](https://github.com/mymindwentblvnk/trvmp-api/actions)
[![Actions Status](https://github.com/mymindwentblvnk/trvmp-api/workflows/PEP%208/badge.svg?branch=develop)](https://github.com/mymindwentblvnk/trvmp-api/actions)

FIFA Dashboard based on FastAPI.



## Docker

### Build
`docker build -t trvmp .`

### Run
`docker run --name trvmp -p 80:80 trvmp`

## Local

### Run
`uvicorn app.main:app --reload`

### PEP 8
`flake8`

### Tests
`sh run-local-tests.sh`
