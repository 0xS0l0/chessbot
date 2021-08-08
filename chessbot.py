#!/usr/bin/env python3

import pyautogui as gui
from stockfish import Stockfish
import requests as rq

def moves(key):

    gui.press(key)

    return

stockfish = Stockfish(" complete path of your stockfish file ", parameters={"Threads": 2, "Skill Level": 20})

print(stockfish.get_parameters())

headers = {'Authorization': 'Bearer " your api key without double quotes "'} 

while True:
    
    response = rq.get("https://lichess.org/api/account/playing", headers=headers)

    print(stockfish.get_board_visual())

    jsonD = response.json()

    stockfish.set_fen_position(jsonD["nowPlaying"][0]["fen"]+" "+jsonD["nowPlaying"][0]["color"][0])

    if(jsonD["nowPlaying"][0]["isMyTurn"]):
        gui.keyDown('enter')

        move = stockfish.get_best_move_time(5000)
        moves(move[0])
        moves(move[1])
        moves(move[2])
        moves(move[3])
