# FullThrottle Backend Developer

- Run the command `docker-compose build`
- Now run the command `docker-compose up`
- open [phpMyAdmin](http://localhost:8070) or by copy-paste-hit on browser http://localhost:8070
- Username: platform_admin  
Password: pb_dev_env
- Import **platform_activity.sql** and dump it on platform_activity database.
- Get Postman collection of all the APIs are here: [Link](https://www.getpostman.com/collections/75a724de4b2c8a80eacd)
- ApiDocs are available here: [Link](https://documenter.getpostman.com/view/7692209/T1LQhSAU)
- For direct result run `curl --location --request GET 'http://localhost:8000/get/user/' \
--header 'Cookie: csrftoken=eXu1dC6NTX0K5N4CRr5skKHf7N3NmbVktT7cDWKeStiFMFUTZs4dUQVSGilJuODf'`

### Support:
- If there is anything which bother you in this project feel free to contact me.

### Thoughts:
- Tried to follow the coding best practices like AES-256 encryption of personal information like realname etc.
- Applied Request Validator. Thanks to Voluptuous a JavaScript joi like library to provide request validation.
- Custom logging is implemented in django project setting.
- Nginx is already configured so you don't have tp worry about that.
- Minimum size based external docker-images are used.

### Future Prospects
  - sessionId based session may be implemented that's why didn't handle authorization.
