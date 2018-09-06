### Setting up and running

- Run `docker-compose up`
- Access to authenticate on Trello: ``http://localhost:5000/authorize``.
You will be redirected to an authorization page. To receive the `auth_token`, grant access to the application.

- To see cards and its members: ``http://localhost:5000/card_members/<board_id>/<auth_token>``
- To see cards and its checklists: ``http://localhost:5000/card_checklists/<board_id>/<auth_token>``


![Screenshot](https://raw.githubusercontent.com/glaubermagal/trelloso/master/screenshot.png)