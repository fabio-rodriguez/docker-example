# How create Docker container and output files created to local storage

The fist step is create the Dockerfile

Build Container: 

>> docker build -t <CONTAINER-NAME>:v1 .

Execute Container:  docker run -it --gpus all -e NVIDIA_DRIVER_CAPABILITIES=all --privileged <CONTAINER-NAME>:v1

Get Container Id: 

>> docker container ls -a 


Copy Files to Local Storage: 

>> docker cp <CONTAINER-ID>:PATH-TO-FILE-IN-CONTAINER PATH-TO-LOCAL-FOLDER

Example:

docker cp <CONTAINER-ID>:/app/docker_test.txt PATH-TO-LOCAL-FOLDER
