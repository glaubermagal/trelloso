### Setting up and running

- Create a virtual environment
- Install all packages using `pip install -r requirements.txt`
- `export TRELLO_API_KEY=...` You can generate your API_KEY [here](https://trello.com/app-key)
- `export FLASK_APP=app.py` To set up the start up script
- `flask run`

### Routes
- Authentication on Trello: ``http://localhost:5000/authorize``.
You will be redirected to an authorization page. To receive an `auth_token`, grant access to the application.

- Cards and Members: ``http://localhost:5000/card_members/<board_id>/<auth_token>``
- Cards and Checklists: ``http://localhost:5000/card_checklists/<board_id>/<auth_token>``


![Screenshot](https://raw.githubusercontent.com/glaubermagal/trelloso/master/screenshot.png)