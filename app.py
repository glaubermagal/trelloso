# coding: utf-8

import os
from flask import Flask, render_template, redirect, request
import requests

app = Flask(__name__)
TRELLO_API_KEY = os.environ.get("TRELLO_API_KEY")


@app.route('/authorize')
def authorize():
    trello_auth_url = "https://trello.com/1/authorize?expiration=30days&name=Trelloso" \
                      "&scope=read&response_type=token&key=%s" % TRELLO_API_KEY
    return redirect(trello_auth_url, code=302)


@app.route('/<board_id>/<token>')
def get_board_data(board_id, token):
    order_by = request.args.get('order_by', default='', type=str)
    display = request.args.get('display', default='members,names,photos,checklists,labels', type=str)
    trello_cards_url = "https://api.trello.com/1/boards/%s/cards/open" % board_id
    trello_lists_url = "https://trello.com/1/boards/%s/lists" % board_id

    request_cards = requests.get(url=trello_cards_url, params={
        'key': TRELLO_API_KEY,
        'token': token,
        'fields': 'all',
        'members': 'true',
        'member_fields': 'fullName',
        'checklists': 'all',
        'actions': 'all',
    })

    request_lists = requests.get(url=trello_lists_url, params={
        'key': TRELLO_API_KEY,
        'token': token,
    })

    cards = request_cards.json()
    lists = request_lists.json()

    list_dict = {}
    for lst in lists:
        list_dict[lst['id']] = lst['name']

    for index, card in enumerate(cards):
        active_members = []
        labels = []
        for label in card['labels']:
            labels.append(label['name'])

        for action in card['actions']:
            if 'memberCreator' in action and action['memberCreator'] not in active_members:
                active_members.append(action['memberCreator'])
            if 'member' in action and action['member'] not in active_members:
                active_members.append(action['member'])

        active_members_sorted = sorted(active_members, key=lambda k: k['fullName'])
        cards[index]['active_members'] = active_members_sorted
        cards[index]['list_name'] = list_dict[card['idList']]
        cards[index]['labels_joined'] = ' / '.join(labels)

    if order_by == 'labels':
        cards = sorted(cards, key=lambda k: k['labels_joined'])

    return render_template(
        "cards.html",
        cards=cards,
        display=display
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')