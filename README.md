# Fynd Python Developer

## Improvising Scaling
  If application become very famous and started to receive ton of traffic. I will follow the following steps to scale this application:
   - Apply Load Balance for requests.
   - Dockerize your application for great scaling.
   - Apply Server-side caching for large data retrieval and whenever there is an update in DB update the server-side caching as well.
   - Apply Redis DB Caching for faster performance.

### Steps for running this application:
- Run the command `docker-compose up -d --build`
- open [phpMyAdmin](http://localhost:8070) or by copy-paste-hit on browser http://localhost:8070
- Username: platform_admin
  Password: dev_env
- Import **platform_imdb.sql** and dump it on platform_imdb database.
- Run localhost:8000 for view anonymously.
- Create User Profile & SuperUser Profile inside docker-container to check admin related features and user related features.
- During addition of movies either upload `imdb.json` file or something similar structured file.

### Support:
- If there is anything which bother you in this project feel free to contact me.

### Thoughts:
- Custom logging is implemented in django project setting.
- Nginx is already configured so you don't have tp worry about that.
- Minimum size based external docker-images are used.

### Future Prospects
 - sessionId based session may be implemented.