import PySimpleGUI as sg


butt_size = (7, 3)
PL_1 = "X"
PL_2 = "O"

current_player = PL_1

player1_positions = []
player2_positions = []

n_places = 9

place1 = sg.Button("", key="-1-", size=butt_size)
place2 = sg.Button("", key="-2-", size=butt_size)
place3 = sg.Button("", key="-3-", size=butt_size)
place4 = sg.Button("", key="-4-", size=butt_size)
place5 = sg.Button("", key="-5-", size=butt_size)
place6 = sg.Button("", key="-6-", size=butt_size)
place7 = sg.Button("", key="-7-", size=butt_size)
place8 = sg.Button("", key="-8-", size=butt_size)
place9 = sg.Button("", key="-9-", size=butt_size)

layout = [[place1, place2, place3],
          [place4, place5, place6],
          [place7, place8, place9],
          [sg.Text("", key="winner")],
          [sg.Button("Salir", key="-salir-"), sg.Button("Reiniciar", key="-retry-")]]


def check_win_condition(current_player, player1_positions, player2_positions):
    winning_positions = [["-1-", "-2-", "-3-"], ["-1-", "-4-", "-7-"], ["-3-", "-6-", "-9-"], ["-4-", "-5-", "-6-"],
                         ["-7-", "-8-", "-9-"], ["-2-", "-5-", "-8-"], ["-1-", "-5-", "-9-"], ["-3-", "-5-", "-7-"]]
    winstate = False
    if current_player == "X":
        for position_element in winning_positions:
            wincheck = set(player1_positions).intersection(position_element)
            if len(wincheck) >= 3:
                winstate = True
                return winstate

    else:
        for position_element in winning_positions:
            wincheck = set(player2_positions).intersection(position_element)
            if len(wincheck) >= 3:
                winstate = True
                return winstate


def add_event_to_positions(event, player_positions):
    player_positions.append(event)
    return player_positions


def player_change(current_player,):
    if current_player == PL_1:
        current_player = PL_2
        return current_player
    else:
        current_player = PL_1
        return current_player


def main():
    winstate = False
    n_places = 9
    current_player = PL_1
    player1_positions = []
    player2_positions = []
    window = sg.Window("Tres en raya", layout)
    while True:
        event, value = window.read()
        print(event, value)
        reset_start_position = 1

        if event == sg.WINDOW_CLOSED or event == "-salir-":
            break

        if event == "-retry-":
            for i in range(n_places):
                window["-{}-".format(reset_start_position)].Update("")
                reset_start_position += 1
            window["winner"].Update("")
            winstate = False
            player1_positions.clear()
            player2_positions.clear()
            current_player = PL_1

        if window.Element(event).ButtonText == "" and not winstate:
            window.Element(event).Update(text=current_player)

            if current_player == PL_1:
                player1_positions = add_event_to_positions(event, player1_positions)
            else:
                player2_positions = add_event_to_positions(event, player2_positions)

            win = check_win_condition(current_player, player1_positions, player2_positions)

            if win and current_player == PL_1:
                print("P1 wins")
                window["winner"].Update("Jugador X gana")
                winstate = True
            elif win and current_player == PL_2:
                print("P2 wins")
                window["winner"].Update("Jugador O gana")
                winstate = True

            current_player = player_change(current_player)


if __name__ == "__main__":
    main()
