#! /bin/bash

set -e
set -x

docker_tag=$(date '+%d%m%Y%H%M%S')

# Deploy image to lambda
cd infra
docker_tag=${docker_tag} make apply
