-------------------------------- NexusHub EX --------------------------------
Create Python Web Application Using Flask/Fast API
see main.py

Add Health-Check Route To Your Application (Return 200, "ok")
see in main.py

Build Your Image Using Tag python_health_check:v0.1
use the Dockerfile attached

Test Locally The Application (Using Port 5000)
docker build -t python_health_check:v0.1 -f Dockerfile . --> create the image from Dockerfile and requirments.txt
docker volume create nexus-data --> prepare volum to the container
docker run -d --name nexus3 -p 8081:8081 -p 8082:8082 -v nexus-data:/nexus-data sonatype/nexus3 --> create container from the image with volume and prepare expose port also to internal repository 8081 nexus 8082 new repo
run on bow 
Create Private Registry Nexus3 Using Docker Image
Add Mount Binding / Volume For Persistent Data
Login The Admin Panel VIA Port 8081
Create New Repository With Name My-Private-Hub Using Port 8082
Tag Existing Image For New Repository
Push The Docker Artifact To NexusHub
Delete The Image Locally And Pull Again From NexusHub Registry
