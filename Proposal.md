### Proposal for Software Engineering project

# Doggag
---

## Enginheroes
Gan Xiao Nan  
Luís Ferreira

---

[Project overview]  
The project consists of an web app to see, vote and comment on dog pictures. It will be developed mainly using python (django) with a user authentication system for uploading images, voting and commenting.
It will be separated in a couple views: "index" view where the posts are listed and ordered by upvotes; a "detail" view where we can see the picture and comment; and user related views where we can log in, edit profile and upload posts.

---

[System architecture]  
It's a simple web app with a database and an image storage.

![architecture failed to load](./imgs_proposal/Architecture.PNG)


---

[Domain model]  
![Domain model diagram failed to load](./imgs_proposal/domain.png)  
Class diagrams are written on [classes](Class.md)

---

[ER diagram]  

![ER diagram failed to load](./imgs_proposal/ER_doggag.png)

---

[Database tables]  

We use a table of an already existing django class "User", from django.contrib.auth, that will help with authentication. The other tables are from original model classes. It is to note that comment table primary key is only complete with the post foreign key and the profile primary key is only complete with the user foreign key. Since the database is SQLite, date is stored as TEXT and for images only the path is stored as TEXT.  

![Database tables failed to load](./imgs_proposal/db.png)

---

[Hosting website]  

[http://doggag.pythonanywhere.com/](http://doggag.pythonanywhere.com/)

---

(Things to talk about)

- [x] Project title, team name & members on the front page
- [x] Overview of the project in around half a page
- [x] Proposed system architecture
- [x] Proposed domain model
- [x] Proposed entity-relationship diagram
- [x] Proposed database tables
- [x] Proposed user interface
- [ ] Website(s) where the main Django server is based.
