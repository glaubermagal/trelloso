# coding: utf-8

import os
import requests
from flask import Flask, render_template, redirect

app = Flask(__name__)
TRELLO_API_KEY = os.environ.get("TRELLO_API_KEY")


@app.route('/authorize')
def authorize():
    trello_auth_url = "https://trello.com/1/authorize?expiration=30days&name=D3Studio&scope=read&response_type=token&key=%s" % TRELLO_API_KEY
    return redirect(trello_auth_url, code=302)


@app.route('/<list_type>/<board_id>/<token>')
def get_cards(list_type, board_id, token):
    trello_cards_url = "https://api.trello.com/1/boards/%s/cards/" % (board_id)

    request_cards = requests.get(url=trello_cards_url, params={
        'key': TRELLO_API_KEY,
        'token': token,
        'fields': 'name',
        'members': 'true',
        'member_fields': 'fullName',
        'checklists': 'all',
        'actions': 'all',
    })

    cards = request_cards.json()
    for index, card in enumerate(cards):
        active_members = []
        for action in card['actions']:
            if 'memberCreator' in action and action['memberCreator'] not in active_members:
                active_members.append(action['memberCreator'])
            if 'member' in action and action['member'] not in active_members:
                active_members.append(action['member'])

        active_members_sorted = sorted(active_members, key=lambda k: k['fullName'])
        cards[index]['active_members'] = active_members_sorted

        try:
            cards[index]['list_name'] = card['actions'][0]['data']['list']['name']
        except KeyError:
            try:
                cards[index]['list_name'] = card['actions'][1]['data']['listAfter']['name']
            except KeyError:
                try:
                    cards[index]['list_name'] = card['actions'][1]['data']['list']['name']
                except KeyError:
                    pass


    return render_template('cards.html', cards=cards, list_type=list_type)