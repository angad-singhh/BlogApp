# REST full API for Blog APP
This project allows you to perform CRUD operation on Blog, add comment to a blog, like and dislike the blog with User registration. The API made using Python-FastAPI, MongoDB as database.

## High level ER Diagram
<img width="700" alt="Screenshot 2024-09-16 213953" src="https://github.com/user-attachments/assets/91665d7a-00d0-4996-951a-06dea3588245">


## Setting up locally
Clone this repository locally by using the below link:
```
https://github.com/angad-singhh/BlogApp.git
```


Create a virtual environment and Install the required dependencies :-

```
pip install -r requirements.txt
```


Run the application server on port 8000:

```
fastapi dev main.py 
```

## Data Models


#### Blog Model
```
class Blog(BaseModel):
    title: str
    authorID: str
    content: str
    tags: list[str]
    curr_date: str
    blog_id: 
```
#### Comment and Like Model
```
class Comments(BaseModel):
    content: str
    user_id: str
    comment_id: str
    blog_id: str


class Likes(BaseModel):
    user_id: list[str] = []
    blog_id: str
```
#### User Model
```
class User(BaseModel):
    name: str
    email: EmailStr
    user_id: str

```

## API Endpoints
Documentation for API endpoints and schemas can be accessed on: 
``` 
http://localhost:8000/docs

```
#### Blog Endpoints
<img width="876" alt="Screenshot 2024-09-16 203803" src="https://github.com/user-attachments/assets/9b2ca002-8a68-4423-843e-ddf934b35fcf">

#### Comment Endpoints
<img width="876" alt="Screenshot 2024-09-16 203815" src="https://github.com/user-attachments/assets/eab100fe-a52c-42e1-8a91-f21ad4a6da6a">

#### Like Endpoints
<img width="872" alt="Screenshot 2024-09-16 203826" src="https://github.com/user-attachments/assets/c11e2a86-d839-4130-9e25-23253e109b8a">

#### User Endpoints
<img width="869" alt="Screenshot 2024-09-16 203842" src="https://github.com/user-attachments/assets/240c04ed-504e-4c59-a573-7349ce99dddd">


## Connect with ME:

<a href="https://linkedin.com/in/angad-singhh" target="blank"><img align="center" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="angad-singhh" /></a>

<a href="mailto:angad.singh2605@gmail.com" target="blank"><img align="center" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="angad.singh2605@gmail.com" /></a>

