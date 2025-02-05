# Development

This project uses uv for dependency management and packaging/deployment to pypi.


### Update Packages

- check for updates on pypi.org and update the pyproject.toml file as needed


### Get A Development Instance

### Basic How To Develop

- activate virtualenv: `ve`
    - or you can source it: `source .venv/bin/activate`
- install dependencies: `uv sync`
- run app (if you run the app - e.g. `mailck --version` from the venv you will be using the dev instance vs the globally installed instance)


### Publish To PyPi

- build a release: `uv build`
- publish to pypi: `uv publish dist/ibuilder-3.10.1*`
    + __NOTE:__ this assumes you set the `UV_PUBLISH_TOKEN` environment variable (_.env-setup should do this for you_)