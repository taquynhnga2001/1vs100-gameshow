import wx
import requests
import math
import random
import plotly.graph_objects as go
url_data = "https://sheetdb.io/api/v1/xr0f4qkl7w06c"
url_ans = "https://sheetdb.io/api/v1/ofsmne5uzeyh7"


class Player:
    def __init__(self, name, sbd, status):
        self.name = name
        self.sbd = sbd
        self.out = status                       # True or False
        self.box = wx.BoxSizer(wx.VERTICAL)
        self.text_name = wx.StaticText()
        self.text_sbd = wx.StaticText()


# ------------ SURVEY OTHERS FRAME & PANEL -----------------------------------------
class SurveyOthersFrame(wx.Frame):
    def __init__(self, parent, title):
        super(SurveyOthersFrame, self).__init__(parent, title=title, size=(700, 500))
        self.SetIcon(wx.Icon("images/logo.jpg", wx.BITMAP_TYPE_ANY))

        self.panel = SurveyOthersPanel(self)


class SurveyOthersPanel(wx.Panel):
    def __init__(self, parent):
        super(SurveyOthersPanel, self).__init__(parent)
        self.SetBackgroundColour('GOLDENROD')

        self.programpanel = wx.BoxSizer(wx.VERTICAL)
        self.mainpanel = wx.BoxSizer(wx.VERTICAL)
        ans_txt = wx.StaticText(self, label="Đáp án muốn khảo sát:")
        ans_txt.SetFont(wx.Font(30, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        self.player_ans = wx.TextCtrl(self, size=(70, 50), style=wx.TE_CENTRE)
        self.player_ans.SetFont(wx.Font(30, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        survey_button = wx.Button(self, label="Khảo sát", size=(250, 50))
        survey_button.SetBackgroundColour("blue violet")
        survey_button.SetForegroundColour("black")
        survey_button.SetFont(wx.Font(27, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        survey_button.Bind(wx.EVT_BUTTON, self.survey)
        self.survey_txt = wx.StaticText(self, label="Có bao nhiêu người chơi ra\nđáp án giống bạn?", style=wx.ALIGN_CENTRE)
        self.survey_txt.SetFont(wx.Font(30, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        self.survey_txt.SetForegroundColour("Red")
        self.mainpanel.Add(ans_txt, 0, wx.TOP | wx.CENTER, 40)
        self.mainpanel.Add(self.player_ans, 0, wx.TOP | wx.CENTER, 0)
        self.mainpanel.Add(survey_button, 0, wx.TOP | wx.CENTER, 10)
        self.mainpanel.Add(self.survey_txt, 0, wx.TOP, 50)
        self.programpanel.Add(self.mainpanel, 0, wx.CENTER, 0)
        self.SetSizer(self.programpanel)

    def survey(self, event):
        his_ans = self.player_ans.GetValue()
        dict_players = app.frame.panel.dict_survey_players
        no_of_ans = 0
        for player in dict_players.keys():
            if dict_players[player][1] == his_ans:
                no_of_ans += 1
        self.survey_txt.SetLabel("   Có "+str(no_of_ans)+" người chơi khác ra\nđáp án "+his_ans)
        self.SetSizer(self.programpanel)


# ------------ ASK OTHERS FRAME & PANEL -----------------------------------------
class AskOthersFrame(wx.Frame):
    def __init__(self, parent, title):
        super(AskOthersFrame, self).__init__(parent, title=title, size=(700, 500))
        self.SetIcon(wx.Icon("images/logo.jpg", wx.BITMAP_TYPE_ANY))

        self.panel = AskOthersPanel(self)


class AskOthersPanel(wx.Panel):
    def __init__(self, parent):
        super(AskOthersPanel, self).__init__(parent)
        self.SetBackgroundColour('GOLDENROD')

        self.programpanel = wx.BoxSizer(wx.VERTICAL)
        self.mainpanel = wx.BoxSizer(wx.VERTICAL)
        twoplayers = wx.BoxSizer(wx.HORIZONTAL)
        choose_button = wx.Button(self, label="Chọn 1 người đúng và 1 người sai", size=(650, 70))
        choose_button.SetBackgroundColour("blue violet")
        choose_button.SetForegroundColour("black")
        choose_button.SetFont(wx.Font(27, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        choose_button.Bind(wx.EVT_BUTTON, self.choose)
        self.num1 = wx.TextCtrl(self, size=(150, 100), style=wx.TE_CENTRE)
        self.num1.SetFont(wx.Font(65, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        self.num2 = wx.TextCtrl(self, size=(150, 100), style=wx.TE_CENTRE)
        self.num2.SetFont(wx.Font(65, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        twoplayers.Add(self.num1, 0, wx.CENTER, 0)
        twoplayers.Add(self.num2, 0, wx.LEFT, 20)
        self.mainpanel.Add(choose_button, 0, wx.TOP | wx.CENTER, 80)
        self.mainpanel.Add(twoplayers, 0, wx.TOP | wx.CENTER, 50)
        self.programpanel.Add(self.mainpanel, 0, wx.CENTER, 0)
        self.SetSizer(self.programpanel)

    def choose(self, event):
        true_player = random.choice(list(app.frame.panel.dict_ask_true.values()))
        false_player = random.choice(list(app.frame.panel.dict_ask_false.values()))
        if random.choice([True, False]):
            self.num1.SetLabel(true_player.sbd)
            self.num2.SetLabel(false_player.sbd)
        else:
            self.num2.SetLabel(true_player.sbd)
            self.num1.SetLabel(false_player.sbd)
        self.SetSizer(self.programpanel)


# ------------ BELIEVE OTHERS FRAME & PANEL -----------------------------------------
class BelieveOthersFrame(wx.Frame):
    def __init__(self, parent, title):
        super(BelieveOthersFrame, self).__init__(parent, title=title, size=(740, 560))
        self.SetIcon(wx.Icon("images/logo.jpg", wx.BITMAP_TYPE_ANY))

        self.panel = BelieveOthersPanel(self)


class BelieveOthersPanel(wx.Panel):
    def __init__(self, parent):
        super(BelieveOthersPanel, self).__init__(parent)
        self.SetBackgroundColour('GOLDENROD')

        a = len(app.frame.panel.dict_A)
        b = len(app.frame.panel.dict_B)
        c = len(app.frame.panel.dict_C)
        d = len(app.frame.panel.dict_D)
        print(a, b, c, d, "ahihi")

        x = ["A", "B", "C", "D"]
        y = [a, b, c, d]

        fig = go.Figure(data=[go.Bar(x=x, y=y, text=y, textposition='outside', marker_color='coral')])
        fig.write_image("believechart.png")
        chart = wx.StaticBitmap(self, pos=(10, 10))
        chart.SetBitmap(wx.Bitmap('believechart.png'))


# ------------- MAIN FRAME & PANEL -------------------------------------------------
class Frame(wx.Frame):
    def __init__(self, parent, title):
        super(Frame, self).__init__(parent, title=title, size=(1300, 800))
        self.SetIcon(wx.Icon("images/logo.jpg", wx.BITMAP_TYPE_ANY))

        self.panel = Panel(self)


class Panel(wx.Panel):
    def __init__(self, parent):
        super(Panel, self).__init__(parent)
        self.SetBackgroundColour('MEDIUM GOLDENROD')

        programpanel = wx.BoxSizer(wx.VERTICAL)
        self.homepanel = wx.BoxSizer(wx.HORIZONTAL)
        self.leftpanel = wx.BoxSizer(wx.VERTICAL)
        self.mainpanel = wx.BoxSizer(wx.VERTICAL)
        self.rightpanel = wx.BoxSizer(wx.VERTICAL)

        # HEADING SHOWS REMAINING PLAYERS
        self.remain_players = 100
        self.heading_txt = wx.StaticText(self, label="1 vs. " + str(self.remain_players))
        self.heading_txt.SetFont(wx.Font(30, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        self.mainpanel.Add(self.heading_txt, 0, wx.TOP | wx.CENTER, 10)

        # TABLE OF PLAYERS
        self.table = wx.BoxSizer(wx.VERTICAL)
        self.row = wx.BoxSizer(wx.HORIZONTAL)
        self.dict_players = {}
        self.dict_remain_players = {}
        self.dict_survey_players = {}
        self.dict_ask_true = {}
        self.dict_ask_false = {}
        self.dict_A = {}
        self.dict_B = {}
        self.dict_C = {}
        self.dict_D = {}
        self.no_of_ques = 0
        self.bound = 0
        # create players in table
        with open("participants.csv", "r") as player_file:
            players = player_file.readlines()
            total = len(players)-1
            self.remain_players = total
            self.heading_txt.SetLabel("1 vs. "+str(self.remain_players))
            numRow = math.ceil(math.sqrt(total))
            for index, player in enumerate(players[1:]):
                player = player.strip().split(",")
                sbd, name = player[0], player[1]
                player = self.create_player(name, sbd)
                self.dict_players["player_"+str(index+1)] = player
                if index % numRow == 0:
                    self.row = wx.BoxSizer(wx.HORIZONTAL)
                    self.row.Add(player.box, 0, wx.BOTTOM, wx.CENTER)
                else:
                    self.row.Add(player.box)
                if index % numRow == numRow-1 or index == total-1:
                    self.table.Add(self.row)

        # BUTTON CHANGES COLOR OF PLAYERS - right panel
        resultButton = wx.Button(self, label="Show result", size=(300, 50))
        resultButton.SetBackgroundColour('sea green')
        resultButton.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        resultButton.Bind(wx.EVT_BUTTON, self.show_result)
        # SURVEY OTHER PLAYERS BUTTON
        surveyButton = wx.Button(self, label="Khảo sát người chơi", size=(300, 50))
        surveyButton.SetBackgroundColour("navy")
        surveyButton.SetForegroundColour('white')
        surveyButton.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        surveyButton.Bind(wx.EVT_BUTTON, self.survey_others)
        # ASK OTHER PLAYERS BUTTON
        askButton = wx.Button(self, label="Hỏi người chơi", size=(300, 50))
        askButton.SetBackgroundColour("navy")
        askButton.SetForegroundColour('white')
        askButton.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        askButton.Bind(wx.EVT_BUTTON, self.ask_others)
        # BELIEVE OTHER PLAYERS BUTTON
        believeButton = wx.Button(self, label="Tin người chơi", size=(300, 50))
        believeButton.SetBackgroundColour("navy")
        believeButton.SetForegroundColour('white')
        believeButton.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        believeButton.Bind(wx.EVT_BUTTON, self.believe_others)

        # DISPLAY MAIN PLAYER'S MONEY
        self.money = 0
        self.money_text = wx.StaticText(self, label="S$"+str(self.money)+" ", size=(300, 150), style=wx.ALIGN_RIGHT)
        self.money_text.SetFont(wx.Font(100, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        self.money_text.SetForegroundColour('yellow')
        self.money_text.SetBackgroundColour('black')

        # ADD SIZERs
        # main panel
        self.mainpanel.Add(self.table, 0, wx.TOP | wx.CENTER, 10)
        self.mainpanel.Add(resultButton, 0, wx.TOP | wx.CENTER, 20)
        self.mainpanel.Add(surveyButton, 0, wx.TOP | wx.TOP, 0)
        # right panel
        self.rightpanel.Add(surveyButton, 0, wx.CENTER, 0)
        self.rightpanel.Add(askButton, 0, wx.CENTER, 0)
        self.rightpanel.Add(believeButton, 0, wx.CENTER, 0)
        # left panel
        self.leftpanel.Add(self.money_text, 0, wx.CENTER, 0)
        # home panel
        self.homepanel.Add(self.leftpanel, 50, wx.ALL | wx.CENTER, 50)
        self.homepanel.Add(self.mainpanel, 0, wx.ALL | wx.CENTER, 20)
        self.homepanel.Add(self.rightpanel, 50, wx.ALL | wx.CENTER, 50)
        programpanel.Add(self.homepanel, 0, wx.CENTER, 0)

        self.SetSizer(programpanel)

    def create_player(self, name, sbd):
        player = Player(name=name, sbd=sbd, status=False)
        player.box = wx.BoxSizer(wx.VERTICAL)
        font20 = wx.Font(45, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        font10 = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        sbd_bgcolor = "CORAL"
        sbd_txtcolor = "black"
        name_bgcolor = "tan"

        player.text_sbd = wx.StaticText(self, label=sbd, size=(100, 80),
                                 style=wx.ALIGN_CENTRE_VERTICAL | wx.ALIGN_CENTRE_HORIZONTAL)
        player.text_sbd.SetBackgroundColour(sbd_bgcolor)
        player.text_sbd.SetFont(font20)
        player.text_sbd.SetForegroundColour(sbd_txtcolor)

        player.text_name = wx.StaticText(self, label=name, size=(100, 20),
                                  style=wx.ALIGN_CENTRE_HORIZONTAL | wx.ST_ELLIPSIZE_END)
        player.text_name.SetBackgroundColour(name_bgcolor)
        player.text_name.SetFont(font10)
        player.box.Add(player.text_sbd, 0, wx.ALL, wx.CENTER)
        player.box.Add(player.text_name, 0, wx.ALL, wx.CENTER)
        return player

    def change_color(self, player, sbd_color, name_color):
        player.text_sbd.SetBackgroundColour(sbd_color)
        player.text_name.SetBackgroundColour(name_color)

    def show_result(self, event):
        self.dict_remain_players = {}
        data = requests.get(url=url_data).json()
        correct_answer = requests.get(url=url_ans).json()[self.no_of_ques]["answer"]
        print(self.no_of_ques+1, " - CORRECT ANSWER: ", correct_answer)
        for answer in data[self.bound:]:
            player = self.dict_players["player_" + answer['SBD']]
            his_ans = answer["Answer"]
            if not player.out and his_ans == correct_answer:
                self.dict_remain_players["player_" + answer['SBD']] = [player, his_ans]
                print("player_" + answer['SBD'], his_ans, True)
            else:
                print("player_" + answer['SBD'], his_ans, False)
                player.out = True
                try:
                    self.dict_remain_players.pop("player_" + answer['SBD'])
                except:
                    pass
                self.change_color(player, sbd_color="dim grey", name_color="dim grey")
        self.bound = len(data)
        self.no_of_ques += 1
        print("bound: ", self.bound)
        self.remain_players = len(self.dict_remain_players.keys())
        self.heading_txt.SetLabel("1 vs. " + str(self.remain_players))
        self.Refresh()

    def survey_others(self, event):
        self.dict_survey_players = {}
        data = requests.get(url=url_data).json()
        for answer in data[self.bound:]:
            player = self.dict_players["player_" + answer['SBD']]
            his_ans = answer["Answer"]
            self.dict_survey_players["player_" + answer['SBD']] = [player, his_ans]
        survey_frame = SurveyOthersFrame(parent=None, title="Khảo sát người chơi")
        survey_frame.Show()

    def ask_others(self, event):
        self.dict_ask_true = {}
        self.dict_ask_false = {}
        data = requests.get(url=url_data).json()
        correct_answer = requests.get(url=url_ans).json()[self.no_of_ques]["answer"]
        print(self.no_of_ques + 1, " - CORRECT ANSWER: ", correct_answer)
        for answer in data[self.bound:]:
            player = self.dict_players["player_" + answer['SBD']]
            his_ans = answer["Answer"]
            if not player.out and his_ans == correct_answer:
                self.dict_ask_true["player_" + answer['SBD']] = player
                print("player_" + answer['SBD'], his_ans, True)
            else:
                self.dict_ask_false["player_" + answer['SBD']] = player
                print("player_" + answer['SBD'], his_ans, False)
        print(len(self.dict_ask_true), True , len(self.dict_ask_false), False)
        ask_frame = AskOthersFrame(parent=None, title="Hỏi người chơi")
        ask_frame.Show()

    def believe_others(self, event):
        self.dict_A = {}
        self.dict_B = {}
        self.dict_C = {}
        self.dict_D = {}
        data = requests.get(url=url_data).json()
        correct_answer = requests.get(url=url_ans).json()[self.no_of_ques]["answer"]
        print(self.no_of_ques + 1, " - CORRECT ANSWER: ", correct_answer)
        for answer in data[self.bound:]:
            player = self.dict_players["player_" + answer['SBD']]
            his_ans = answer["Answer"]
            if not player.out:
                if his_ans == "A":
                    self.dict_A["player_" + answer['SBD']] = player
                    print("player_" + answer['SBD'], his_ans)
                elif his_ans == "B":
                    self.dict_B["player_" + answer['SBD']] = player
                    print("player_" + answer['SBD'], his_ans)
                elif his_ans == "C":
                    self.dict_C["player_" + answer['SBD']] = player
                    print("player_" + answer['SBD'], his_ans)
                elif his_ans == "D":
                    self.dict_D["player_" + answer['SBD']] = player
                    print("player_" + answer['SBD'], his_ans)
        print(len(self.dict_A), "A\t", len(self.dict_B), "B\t", len(self.dict_C), "C\t", len(self.dict_D), "D\t")

        believe_frame = BelieveOthersFrame(parent=None, title="Tin người chơi")
        believe_frame.Show()


class App(wx.App):
    def OnInit(self):
        self.frame = Frame(parent=None, title="Đấu trường 100")
        self.frame.Show()
        return True


app = App()
app.MainLoop()