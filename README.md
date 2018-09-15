### Setting up and running

- Copy `.env.sample` into `.env` and set up your `TRELLO_API_KEY`. You can generate it [here](https://trello.com/app-key)
- Run `docker-compose up`
- Access to authenticate on Trello: ``http://localhost:5000/authorize``.
You will be redirected to an authorization page. To receive the `auth_token`, grant access to the application.

- To see cards all visible cards, visit: ``http://localhost:5000/<board_id>/<auth_token>?display=members,names,photos,checklists,labels``
- Feel free to change the URL param ``display`` to hide some elements.


![Screenshot](https://raw.githubusercontent.com/glaubermagal/trelloso/master/screenshot.png)


### Demo

[Authorize](https://trelloso.herokuapp.com/authorize) this demo and use the generated `auth_token` here: ``https://trelloso.herokuapp.com/zU1bVDqo/<auth_token>?display=members,names,photos,checklists,labels``
