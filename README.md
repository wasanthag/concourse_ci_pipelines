# concourse_ci_pipelines
various CICD pipelines based on concourse CI

- create and upload base image
  This pipeline builds a docker image based on a Dockerfile inside a github repo and uploads the built image to a docker  repository such as docker hub or any docker repo in the format containers.xyz.com/container. Dockerfile used copies pip requirements file on to the container and runs pip install. Other python packgae installers can be used as well, ex. easy_install

- run unit tests
  This pipeline pulls docker image from a docker image repository and runs unit test cases against code stored in a github repo
  
- deploy to kuberenetes cluster
  This pipeline pulls a docker image ,runs unit tests , package the code and docker image and uploads to a docker image repository if the unit tests pass. Then that docker image (including unit tests passed code) is deployed to a Kubernetes cluster based on a spec file. This use a fork from concourse CI community resources  jcderr/concourse-kubernetes-resource 

Crdentials such as github and docker hub login can be added in to a crdentials.yml file and use with concourse fly cli option -l crdentials.yml. These crdentials files should be added in to .gitignore to prevent them from being exposed to public.
