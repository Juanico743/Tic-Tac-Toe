import tkinter as tk
from tkinter import messagebox


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.start_restart_next = None
        self.tempTextHolder = None
        self.movingPlayer = None
        self.scoreBoard = None
        self.nextMove = None
        self.myColor = None
        self.buttons = None
        self.button = None
        self.status = None
        self.color = None
        self.move = None
        self.draw = False
        self.win = False
        self.player1_Score = 0
        self.player2_Score = 0
        self.maxMove = 9
        self.round = 1
        self.game = 1
        self.player1_color = "#6E66fA"
        self.player2_color = "#FA6678"
        self.draw_color = "#7D7D7D"
        self.win_color = "#52FA87"
        self.player1 = "X"
        self.player2 = "O"
        self.occupied = []
        self.buttons = []
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.resizable(False, False)
        self.master.geometry("550x360")  # automatic size
        self.pack(fill="both", expand=True)
        self.window()

    def window(self):

        self.top_panel()
        self.tic_tac_toe_board()
        self.side_bar()

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def top_panel(self):
        tittle = tk.Frame(self, bg="#000000")
        tittle.grid(row=0, column=0, columnspan=2, sticky="nsew")

        label = tk.Label(tittle, text="TIC TAC TOE", bg="#000000", height=1, font=("Berlin Sans FB Demi", 30),
                         fg="#03DAC6")
        label.grid(row=0, column=0, rowspan=3, sticky="nsew")

        name = tk.Label(tittle, text="HALOW ™️", bg="#000000", height=1, font=("Berlin Sans FB Demi", 15),
                        fg="#FFFFFF")
        name.grid(row=1, column=1, sticky="nsew")

        tittle.grid_rowconfigure(0, weight=1)
        tittle.grid_columnconfigure(0, weight=1)
        tittle.grid_columnconfigure(1, weight=1)

    def tic_tac_toe_board(self):
        outer_board = tk.Frame(self, bg="#FFFFFF", padx=10, pady=10)
        outer_board.grid(row=1, column=0)

        board = tk.Frame(outer_board, bg="black", padx=10, pady=10)
        board.grid(row=0, column=0)
        outer_board.grid_columnconfigure(0, weight=1)

        for i in range(1, 10):
            button = tk.Button(board, bg="#FFFFFF", text=str(i), fg="#FFFFFF", font=("Berlin Sans FB Demi", 30),
                               disabledforeground="#FFFFFF", width=3, height=0, relief="flat", state="disabled",
                               command=lambda button_id=i: self.change_check(button_id))

            button.grid(row=(i - 1) // 3, column=(i - 1) % 3, padx=5, pady=5)
            self.buttons.append(button)

            button.bind("<Leave>", self.on_leave)
            button.bind("<Enter>", self.on_enter)

    def on_enter(self, event):
        if not self.win or not self.draw:
            button = event.widget
            if button["text"] not in ["X", "O"]:
                self.tempTextHolder = button["text"]
                if self.movingPlayer != self.player1:
                    button.config(bg="#9a94ff", text="x", fg=self.player1_color)
                elif self.movingPlayer != self.player2:
                    button.config(bg="#fa8c99", text="o", fg=self.player2_color)

    def on_leave(self, event):
        button = event.widget
        if not self.win or not self.draw:
            if button["text"] == "X":
                if button["background"] not in [self.win_color, self.draw_color]:
                    button.config(bg=self.player1_color, fg="#000000")
            elif button["text"] == "O":
                if button["background"] not in [self.win_color, self.draw_color]:
                    button.config(bg=self.player2_color, fg="#000000")
            else:
                button.config(bg="#FFFFFF", fg="#FFFFFF", text=self.tempTextHolder)

    def side_bar(self):
        sidebar = tk.Frame(self, bg="#FFFFFF", )
        sidebar.grid(row=1, column=1, sticky="nsew")

        self.move = tk.Label(sidebar, text="🪐", bg="#FFFFFF", height=1, font=("Berlin Sans FB Demi", 70), fg="#000000")
        self.move.grid(row=1, column=0, columnspan=3, sticky="ew")

        self.scoreBoard = tk.Label(sidebar, text=f"{self.player1_Score:^3} - {self.player2_Score:^3}", bg="#FFFFFF",
                                   height=1, font=("impact", 50), fg="#000000")
        self.scoreBoard.grid(row=2, column=0, columnspan=3, sticky="ew")

        playersScore = tk.Label(sidebar, text=f"{'PLAYER 1':^23}{'PLAYER 2':^23}", bg="#FFFFFF", height=1,
                                font=("Berlin Sans FB Demi", 10), fg="#000000")
        playersScore.grid(row=3, column=0, columnspan=3, sticky="ew")

        self.start_restart_next = tk.Button(sidebar, bg="#FFFFFF", text="START", fg="#000000", width=3, height=0,
                                            relief="flat", font=("Berlin Sans FB Demi", 15), padx=20,
                                            command=self.begin)
        self.start_restart_next.grid(row=5, column=0, sticky="ew")

        quit_exit = tk.Button(sidebar, bg="#FFFFFF", text="QUIT", fg="#000000", font=("Berlin Sans FB Demi", 15),
                              width=3, height=0, relief="flat", padx=20, command=self.quit)
        quit_exit.grid(row=5, column=2, sticky="ew")

        sidebar.grid_columnconfigure(0, weight=3)
        sidebar.grid_columnconfigure(1, weight=0)
        sidebar.grid_columnconfigure(2, weight=3)
        sidebar.grid_rowconfigure(1, weight=2)
        sidebar.grid_rowconfigure(4, weight=2)
        sidebar.grid_rowconfigure(5, weight=1)

    def begin(self):
        if self.start_restart_next["text"] == "START":
            for i in range(9):
                self.buttons[i].config(state="normal")
            self.start_restart_next.config(text="RESTART")
            self.move.config(text="X", fg=self.player1_color)
        elif self.start_restart_next["text"] == "RESTART":
            restartResult = messagebox.askyesno("Restart", "Note: When Restart, the Score will be lost.",
                                                icon="question", default='yes')
            if restartResult:
                self.round = 1
                self.game = 1
                self.occupied = []
                self.player1_Score = 0
                self.player2_Score = 0
                self.scoreBoard.config(text="0  -  0")
                for i in range(9):
                    self.buttons[i].config(bg="#FFFFFF", text=str(i), fg="#FFFFFF", disabledforeground="#FFFFFF")
        elif self.start_restart_next["text"] == "NEXT":
            self.win = False
            self.draw = False
            self.game += 1
            self.occupied = []
            self.start_restart_next.config(text="RESTART")
            for i in range(9):
                self.buttons[i].config(bg="#FFFFFF", text=str(i), fg="#FFFFFF", state="normal",
                                       disabledforeground="#FFFFFF")

        if self.game % 2 == 1:
            self.movingPlayer = self.player2
            self.maxMove = 9
            self.round = 1
            self.move.config(text=self.player1, fg=self.player1_color)
        elif self.game % 2 == 0:
            self.movingPlayer = self.player1
            self.maxMove = 10
            self.round = 2
            self.move.config(text=self.player2, fg=self.player2_color)

    def moving(self):
        if self.round % 2 == 0:
            self.movingPlayer = self.player2
            self.nextMove = self.player1
            self.myColor = self.player1_color
            self.color = self.player2_color
        elif self.round % 2 == 1:
            self.movingPlayer = self.player1
            self.nextMove = self.player2
            self.myColor = self.player2_color
            self.color = self.player1_color

    def change_check(self, button_id):
        self.moving()
        if button_id not in self.occupied:
            button = self.buttons[button_id - 1]
            button.config(text=self.movingPlayer, background=self.color, fg="#000000")
            self.occupied.append(button_id)
            self.round += 1

            self.move.config(text=self.nextMove, fg=self.myColor)

        self.check_winner()

    def check_winner(self):
        for i in range(0, 7, 3):
            if self.buttons[i].cget("text") == self.buttons[i + 1].cget("text") == self.buttons[i + 2].cget("text"):
                self.buttons[i].config(background=self.win_color, disabledforeground="#000000")
                self.buttons[i + 1].config(background=self.win_color, disabledforeground="#000000")
                self.buttons[i + 2].config(background=self.win_color, disabledforeground="#000000")
                self.winner()

        for i in range(3):
            if self.buttons[i].cget("text") == self.buttons[i + 3].cget("text") == self.buttons[i + 6].cget("text"):
                self.buttons[i].config(background=self.win_color, disabledforeground="#000000")
                self.buttons[i + 3].config(background=self.win_color, disabledforeground="#000000")
                self.buttons[i + 6].config(background=self.win_color, disabledforeground="#000000")
                self.winner()

        if self.buttons[0].cget("text") == self.buttons[4].cget("text") == self.buttons[8].cget("text"):
            self.buttons[0].config(background=self.win_color, disabledforeground="#000000")
            self.buttons[4].config(background=self.win_color, disabledforeground="#000000")
            self.buttons[8].config(background=self.win_color, disabledforeground="#000000")
            self.winner()

        if self.buttons[2].cget("text") == self.buttons[4].cget("text") == self.buttons[6].cget("text"):
            self.buttons[2].config(background=self.win_color, disabledforeground="#000000")
            self.buttons[4].config(background=self.win_color, disabledforeground="#000000")
            self.buttons[6].config(background=self.win_color, disabledforeground="#000000")
            self.winner()
        else:
            self.check_draw()

    def check_draw(self):
        if not self.win:
            if self.round == (self.maxMove + 1):
                for i in range(9):
                    self.buttons[i].config(background=self.draw_color)
                self.draw_()

    def winner(self):
        self.win = True
        for i in range(9):
            self.buttons[i].config(state="disabled")
        self.start_restart_next.config(text="NEXT")
        if self.movingPlayer == self.player1:
            self.player1_Score += 1
            self.move.config(text=f"x👑x", fg=self.player1_color)
        elif self.movingPlayer == self.player2:
            self.player2_Score += 1
            self.move.config(text=f"o👑o", fg=self.player2_color)
        self.scoreBoard.config(text=f"{self.player1_Score:^3} - {self.player2_Score:^3}")

    def draw_(self):
        self.draw = True
        for i in range(9):
            self.buttons[i].config(state="disabled")
        self.start_restart_next.config(text="NEXT")
        self.move.config(text="🗿🗿", fg=self.draw_color)

    def quit(self):
        quitResult = messagebox.askyesno("Quit", "Do you want Leave?", icon="question", default='yes')
        if quitResult:
            self.master.quit()
        # self.master.destroy()


root = tk.Tk()

app = Application(master=root)

app.mainloop()
