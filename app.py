# coding: utf-8

import os
from flask import Flask, render_template, redirect
import requests

app = Flask(__name__)
TRELLO_API_KEY = os.environ.get("TRELLO_API_KEY")


@app.route('/authorize')
def authorize():
    trello_auth_url = "https://trello.com/1/authorize?expiration=30days&name=D3Studio&scope=read&response_type=token&key=%s" % TRELLO_API_KEY
    return redirect(trello_auth_url, code=302)


@app.route('/<list_type>/<board_id>/<token>')
def get_board_data(list_type, board_id, token):
    trello_cards_url = "https://api.trello.com/1/boards/%s/cards/all" % board_id
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
    for list in lists:
        list_dict[list['id']] = list['name']

    for index, card in enumerate(cards):
        active_members = []
        for action in card['actions']:
            if 'memberCreator' in action and action['memberCreator'] not in active_members:
                active_members.append(action['memberCreator'])
            if 'member' in action and action['member'] not in active_members:
                active_members.append(action['member'])

        active_members_sorted = sorted(active_members, key=lambda k: k['fullName'])
        cards[index]['active_members'] = active_members_sorted
        cards[index]['list_name'] = list_dict[card['idList']]

    if list_type == "card_members_no_name":
        return render_template('members_no_name.html', cards=cards, list_type=list_type)
    else:
        return render_template('cards.html', cards=cards, list_type=list_type)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')