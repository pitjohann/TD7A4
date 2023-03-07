# TD7A4

## Description

Part 1: Without using docker-compose

Step 1:

Add to your application a feature, which reads a text file on your host and shows the content on a web page. Any changes in the content of this file should be shown by refreshing the web page. (by using a bind mount) 

The content of this file can for example explain the benefits of using docker volumes!

Step 2:

Make your database persistent. (by using Volume)

Explain how you can migrate it! How to share it with another instance of the same database engine.

Part 2: By using docker-compose 

Do both steps by using docker-compose and show your docker-compose.yaml and its changes!

### Part 1

#### Step 1

To do the application that reads a text file and shows the content on a web page we need a python code.
This code is in app.py which uses flask to create a web application instance. 
To build a container that uses this code we need to pull the python image.
For this we need a terminal where we'll write the commands.
Navigate to where your files are using ` cd <absolutePathToFiles>`.
Now we can execute the docker commands.
Here's the command to pull from the Registry the python image.

```docker pull python```

Next we need to write a Dockerfile that will build our container's image. 
The file for this is the file named Dockerfile.

On your terminal you can now build the image using the following command which will use our Dockerfile to create the image. 

``` docker build -t <your image's name> ```

Next we will create the container and start it in the same command. We will use a bind mount to be able to modify the content of `text.txt` and for that we will add on the command the -v part as described here : 

``` docker run -d -p 5000:5000 -v <absolutePathToYourTxtFile:/app/test.txt> <your image's name> ```

Now you just need to go on a webrowser and type `localhost:5000/text` to see your txt file.

#### Step 2
In this part we'll use Volumes to make the database persistent.
We first create a Volume with `docker volume create <VolumeName>`

Then we create a network so that the container you created before and the database container will be able to communicate.
`docker network create --driver bridge <networkName>`

Now we pull the database image from the registry, here Mongo `docker pull mongo`.

All that is left is to create and run the database container using Volumes on the network we created.
``` docker run -d -v <VolumeName:/data/db> --name <containerName> --network <networkName> mongo```

Make sure you stopped the container of Step 1 on Docker Desktop before doing the next step since we need to run the container on the same network as the dtb container.
Then type this command to run the container:
``` docker run -d -p 5000:5000 -v <absolutePathToYourTxtFile:/app/test.txt> --network <NetworkName> <your image's name>```

You can now test your dtb by doing the following commands : 
```
docker exec -it <image's name> mongosh

use test_database

db.test_collection.find()
```

### Part 2

For this part we just need the file docker-compose.yml and run the docker compose by doing this command in the terminal: 

`docker-compose up -d`

And we can check if that worked by doing the verification steps of part 1.
