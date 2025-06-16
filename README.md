# Universal Auto
This repo is supposed to get statistics from Uber, Bolt, Uklon to calculate performance of car cross this aggregators for fleet owners and provide reports via telegram BOT for Drivers, Fleet Managers and Fleet Owners. 

# How to run a project on your local machine?
1. Install Docker https://docs.docker.com/engine/install/
2. Rename .env_example to .env
3. Rename docker-compose_example.yml to docker-compose.yml
4. create DB using credentials from .env file in your local Postgres instance or use pgAdmin to create DB
   - If you want to use pgAdmin, add pgAdmin into docker-compose run `docker-compose up --build pgadmin` and open http://localhost:5050/browser/
   - Create DB `universal_auto_dev` in pgAdmin or in your local Postgres instance using credentials from .env file
   - If you have error /data/db: permission denied failed to solve run: `sudo chmod -R 777 ./data/db`
5. Run `docker-compose up --build`
6. Run migrations by `docker exec -it universal_auto_web python3 manage.py migrate`
7. Run to create admin user `docker exec -it universal_auto_web python3 manage.py createsuperuser`
8. Open http://localhost/admin/ in browser and auth with user created at step 7
9. add Partner instance
   - Go to http://localhost/admin/app/partner/add/
   - Save the form
10. Run `docker exec -it universal_auto_web python3 manage.py runscript seed_db` to create test data

# How to start contribute?

1. Take an issue from the list  https://github.com/KurochkaR/universal_auto/issues and ask questions
2. Fork project and create a new branch from a master branch with the name in the format: issues-12-your_last_name
3. Ensure you run makemigrations by `docker exec -it universal_auto_web python3 manage.py makemigrations`
4. After work is finished and covered by tests create a Pull Request with good description what exactly you did and how and add KurochkaR as reviewer. 
5. After review fix found problems
6. Manual QA stage need to be done by other person to confirm solutions works as expected
7. We will deploy to staging server to confirm it works in pre-pod ENV
8. Merge into master and deploy to production instance. 
