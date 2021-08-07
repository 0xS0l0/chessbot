#!/usr/bin/env python3

import pyautogui as pygui
from stockfish import Stockfish
import requests as rs

def moves(key):

    pygui.press(key)

    return

stockfish = Stockfish(" complete path of your stockfish file ", parameters={"Threads": 2, "Skill Level": 20})

print(stockfish.get_parameters())

headers = {'Authorization': 'Bearer " your api key without double quotes "'} 

while True:
    
    response = rs.get("https://lichess.org/api/account/playing", headers=headers)

    print(stockfish.get_board_visual())

    jsonD = response.json()

    stockfish.set_fen_position(jsonD["nowPlaying"][0]["fen"]+" "+jsonD["nowPlaying"][0]["color"][0])

    if(jsonD["nowPlaying"][0]["isMyTurn"]):
        pygui.keyDown('enter')

        move = stockfish.get_best_move_time(5000)
        moves(move[0])
        moves(move[1])
        moves(move[2])
        moves(move[3])
