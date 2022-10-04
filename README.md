# Gamer Verse - API

## Table of Contents
- [Introduction](#introduction)
- [User Stories](#user-stories)
- [Database Schema](#database-schema)
- [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Automated Testing](#automated-testing)
- [Solved Bugs](#solved-bugs)
- [Known Bugs](#known-bugs)
- [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries and Programs](#frameworks-libraries-and-programs)
    - [Databases](#databases)
- [Deployment](#deployment)
    - [Deploying to Heroku](#deploying-to-heroku)
    - [Forking Repository](#forking-repository)
    - [Cloning Repository](#cloning-repository)
- [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
    - [Media](#media)
    - [Resources](#resources)
    - [Acknowledgements](#acknowledgements)

## Introduction
Gamer Verse is a content sharing platform to share reviews, posts and have social interactions with likeminded individuals about games. Users will be able to find posts and reviews relating to the gaming space, along with community events in local cities. This is the backend API database section of the project built to support the ReactJS frontend, and is powered by the Django Rest Framework. 

DEPLOYED API (HEROKU) - [CLICK HERE](https://gamer-verse-drf-api.herokuapp.com/)

DEPLOYED FRONTEND (HEROKU) - CLICK HERE

DEPLOYED FRONTEND REPOSITORY - [CLICK HERE](https://github.com/Jbachtiger/ci-pp5-gamer-verse-drf-api#user-stories)

## User Stories

## Database Schema
DrawSQL was used to create a database schema to visualise the types of custom models this project might require. This schema was used as a guide to what needed to be added to each model.

![Database Schema](docs/database_schema/database_schema_gamer_verse.png)

## Testing

### Manual Testing

### Validator Testing

## Solved Bugs

- Bug 1: 'collections.OrderedDict' object has no attribute 'size'
This error occured when trying to implement validation for image size. The issue was a spelling mistake in the function call. def validate was originally called instead of def validate_image.

- Bug 2: UNIQUE constraint failed: posts_post.owner_id
This error happened as the posts model was set as owner = models.OneToOneField(User, on_delete=models.CASCADE) where as it needed to be owner = models.ForeignKey(User, on_delete=models.CASCADE).

- Bug 3: 'super' object has no attribute 'CREATE'
This error was due to a spelling issue with create being in all capitals and need to be lowercase.

## Known Bugs
None known

## Technologies Used

### Languages Used
- [Python](https://www.python.org/) 

### Frameworks, Libraries and Programs Used
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django Rest Auth](https://django-rest-auth.readthedocs.io/en/latest/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Cors Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- [Heroku](https://dashboard.heroku.com/apps)
- [GitHub](https://github.com/)
- [Git](https://git-scm.com/)
- [GitPod](https://gitpod.io/projects)
- [Cloudinary](https://cloudinary.com/)
- [DrawSQL](https://drawsql.app/diagrams)
- [Raw Pixel](https://www.rawpixel.com/)

### Databases 
- SQLite: local database used to test during development
- PostgreSQL: database used in Heroku to store data on deployment

## Deployment

### Set up JSON Web Tokens


### Deploying to Heroku

### Forking Repository
You can fork the GitHub repository to make a copy of the original to view and change without affecting the original. This can be done by:

1. Log into GitHub or create an account
2. Locate the repository at https://github.com/Jbachtiger/ci-pp5-gamer-verse-drf-api
3. At the top of the repository, on the right-hand side of the page you will see an option to select "Fork" from the available buttons
4. Click the fork button and a copy of the repository will have been created

### Cloning Repository

## Credits 

### Media
- [RawPixel](https://www.rawpixel.com/) was used to source the default profile and post images 

### Resources
- The Code Institute DRF-API walkthrough was used as a guide on how to build a DRF-API 
- Slack Community

### Acknowledgements
- My partner for her patience and continuing support




