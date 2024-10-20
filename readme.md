# Commands for project set up

1. Locate the .env_template file.

2. Create a .env file in your project root by copying the template:
    > cp .env-template .env

3. Fill in the required values in your .env file. Ensure each variable in the .env-template file is defined with the correct values.

4. Install docker by following below linK : 
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04

5. Install docker compose by following below link : 
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-22-04

6. Build and Run the Containers
    > sudo docker compose up

7. Run makemigration and migrate command
    > sudo docker exec -it mycurrency_app sh  
    > python3 manage.py makemigrations   
    > python3 manage.py migrate

7. To stop the containers:
    > sudo docker compose down

