def game():
    print("===== Tic Tac Toe AI =====")
    print("You = X")
    print("Computer = O")

    while True:

        print_board()

        # Player Turn
        player_move()

        winner = check_winner(board)
        if winner:
            break

        # AI Turn
        computer_move()

        winner = check_winner(board)
        if winner:
            break

    print_board()

    if winner == "X":
        print("\n🎉 You Win!")
    elif winner == "O":
        print("\n🤖 AI Wins!")
    else:
        print("\n🤝 Match Draw!")


if __name__ == "__main__":
    game()
