# Development Log for FableForge
*Date: December 19, 2023*

## Project Initiation and Planning
### Conceptualization and Scope Definition:
- Defined the concept of "FableForge" as an AI-driven storytelling and image creation application.
- Outlined the project's scope, including AI integration for story and image generation.

### Selection of Technology Stack:
- Chose Python with Django for the backend.
- Decided on React for the frontend development.
- Selected PostgreSQL for the database.
- Agreed on using AWS for cloud hosting.

### Project Proposal Documentation:
- Drafted a comprehensive project proposal, detailing objectives, background, scope, technology stack, and more.
- Created detailed appendices, including a technology stack overview (Appendix A), user flow diagrams (Appendix B), and a timeline with milestones (Appendix C).

### Development Strategy Planning:
- Developed a detailed timeline and milestone chart for the project, spanning 10 weeks with weekly milestones and daily tasks.
- Established a strategy for iterative development, testing, and deployment.

### Kanban Board Setup for Week 1:
- Initiated a Kanban board for the first week of development, categorizing tasks into "To Do," "In Progress," and "Done."


### Virtual Environment Setup
- Created conda environment FableForge python=3.11

### Django Setup
- Installed latest Django (5.0)
- Created Django project: fableforge_django
- Created app: fableforge
- Did first migration: python manage.py migrate
- Created superuser: neo 


### Ensured gitignore
- Verified that gitignore file was properly configured for Django
    - db.sqlite3
    - __pycache__