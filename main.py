import os


# docker build -t tw-sentiment-demo:v1 .
# docker run -it --gpus all -e NVIDIA_DRIVER_CAPABILITIES=all --privileged tw-sentiment-demo:v1
# docker container ls -a 
# docker cp d4e515d020e0:/images/ETH_output_chart.html "C:/Users/fabio/OneDrive/Escritorio/example Docker/"

if __name__ == "__main__":

    fn = "docker_test.txt"
    path2file = f"{os.curdir}/{fn}"
    
    print(f"*** Creating {path2file}")
    with open(path2file, "w") as f:
        f.write("Docker Test")


