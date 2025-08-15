About the project:

- the project was created to host reviews of sports competitions;
- the django framework was used for development;
- the bootstrap CSS framework was used for visual design;
- the video (link) and other information about the competition is posted through the administrative panel;
- the Docker containerization technology was used as the project execution environment.

Project launch:

- before local launch of the application, you should switch the SECURE_SSL_REDIRECT setting from
default=True to default=False in the app/django_project/settings.py file;
- for security reasons, the docker-compose.prod.yml file is missing in the project root

Link to the working project:

- https://football-hockey.site/
