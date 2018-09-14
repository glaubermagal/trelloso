### Setting up and running

- Copy `.env.sample` into `.env` and set up your `TRELLO_API_KEY`. You can generate it [here](https://trello.com/app-key)
- Run `docker-compose up`
- Access to authenticate on Trello: ``http://localhost:5000/authorize``.
You will be redirected to an authorization page. To receive the `auth_token`, grant access to the application.

- To see cards and its members with photo and name: ``http://localhost:5000/members/<board_id>/<auth_token>``
- To see cards and its members with photo and without name: ``http://localhost:5000/members_no_name/<board_id>/<auth_token>``
- To see cards and its checklists: ``http://localhost:5000/checklists/<board_id>/<auth_token>``


![Screenshot](https://raw.githubusercontent.com/glaubermagal/trelloso/master/screenshot.png)


### Demos

[Authorize](https://trelloso.herokuapp.com/authorize) this demo and use the generated `auth_token` down here:

- Cards and its members with photo and name: ``https://trelloso.herokuapp.com/members/zU1bVDqo/<auth_token>``
- Cards and its members with photo and without name: ``https://trelloso.herokuapp.com/members_no_name/zU1bVDqo/<auth_token>``
- Cards and its checklists: ``https://trelloso.herokuapp.com/checklists/zU1bVDqo/<auth_token>``
