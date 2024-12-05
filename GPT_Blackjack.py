from openai import OpenAI



class GPT:
    #Please enter a ChatGPT key here
    client = OpenAI(
    api_key='ENTER API KEY HERE'
    )
    prompt_history = [{"role": "system", "content": "Your are an intelligent assistant"}]
    #Hold values of drawn cards for blackjack
    user_cards = []
    dealer_cards = []
    drawn_cards = []
    
    #Draw new cards - exclude suits as it may tell you the suit instead of value (suit is not needed for blackjack)
    def draw_card(self):
        self.prompt_history.append({"role": "user", "content": "Draw a random card for blackjack and tell me what it is in one word but do not tell me its suit"})
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages= self.prompt_history
        )
        return completion.choices[0].message.content

    #Tell the sum of the users list of cards
    def user_card_sum(self):
        self.prompt_history.append({"role": "user", "content": f"in blackjack what is the sum value of the following cards {self.user_cards}. Please tell me the result in one word as a number"})
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages= self.prompt_history
        )
        return completion.choices[0].message.content
    
    #Tell the sum of the dealers list of cards
    def dealer_card_sum(self):
        self.prompt_history.append({"role": "user", "content": f"in blackjack what is the sum value of the following cards {self.dealer_cards}. Please tell me the result in one word as a number"})
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages= self.prompt_history
        )
        return completion.choices[0].message.content
    
    #Use GPT to recommend the user a move
    def recommended_move(self):
        self.prompt_history.append({"role": "user", "content": f"in blackjack tell me what is the best possible move when i have {self.user_card_sum()}. Please tell me in one word"})
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages= self.prompt_history
        )
        return completion.choices[0].message.content
    
    #Use GPT to recommend the dealer a move (used for automation)
    def dealer_recommendation(self):
        self.prompt_history.append({"role": "user", "content": f"in blackjack tell me what is the best possible move when i have {self.dealer_card_sum()}. Please tell me in one word"})
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages= self.prompt_history
        )
        return completion.choices[0].message.content
    
    #Use GPT to calculate the Users chance of winning
    def chance_to_win(self):
        self.prompt_history.append({"role": "user", "content": f"in blackjack what is my percentage chance of winning if i have {self.user_cards} and the dealer has a {self.dealer_cards} showing. Please tell me as a percentage in one word"})
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages= self.prompt_history
        )
        return completion.choices[0].message.content
    
    #Use GPT to predict the value of the next card
    def predicted_card_value(self):
        self.prompt_history.append({"role": "user", "content": f"in blackjack the following cards have been drawn {self.drawn_cards}. Please tell me the predicted value of the next card in one word as a number"})
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages= self.prompt_history
        )
        return completion.choices[0].message.content
    
    #Draw cards for the user
    def user_draw(self):
        card = self.draw_card()
        self.user_cards.append(card)
        self.drawn_cards.append(card)
    
    #Draw cards for the dealer
    def dealer_draw(self):
        card = GPT().draw_card()
        GPT().dealer_cards.append(card)
        GPT().drawn_cards.append(card)
        
    #Start the game - 2 user cards, 1 dealer card
    def initialise_game(self):
        print("Welcome to Blackjack\n")
        self.user_draw()
        self.user_draw()
        self.dealer_draw()
        print(f"Your Cards are: \n{self.user_cards}\n")
        print(f"The Dealers Shown Card is: \n{self.dealer_cards}\n")
    
    #Use GPT to determine the winner
    def game_outcome(self):
        self.prompt_history.append({"role": "user", "content": f"in blackjack which would win {self.user_card_sum()} or {self.dealer_card_sum()}. If the first number would win please reply 'You Win!'. if the second would win reply 'You Lose!'. Otherwise reply 'TIE!'"})
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages= self.prompt_history
        )
        return completion.choices[0].message.content
 
    #GPT Automates the end of the game once the user stands
    def finalise_game(self):
        while True:
            self.dealer_draw()
            print(f"The Dealers Cards are: \n{GPT().dealer_cards}\n")
            dealer_action = self.dealer_recommendation()
            print(f"The dealer chooses to: {dealer_action}\n")
            if dealer_action.lower() =='stand':
                break
            
        print(f"Your total is: {self.user_card_sum()}")
        print(f"The Dealers total is: {self.dealer_card_sum()}")
        print(self.game_outcome())
    
    #Allow the user to interact with GPT to play blackjack
    def play_game(self):
        self.initialise_game()
        while True:
            user_input = input("What would you like to do? \n'A' - Hit\n'B' - Stand\n'C' - Get a recommended move\n'D' - Know what your chance to win is\n'E' - Know what the predicted value of the next card is\n")
            if user_input.lower()=='a':
                GPT().user_draw()
                print(f"Your Cards are: \n{GPT().user_cards}\n")
            elif user_input.lower() =='b':
                GPT().finalise_game()
                break
            elif user_input.lower() =='c':
                print(f"Your recommended move is to: {GPT().recommended_move()}\n")
            elif user_input.lower()=='d':
                print(f"Your chance of winning is: {GPT().chance_to_win()}\n")
            elif user_input.lower()=='e':
                print(f"The predicted value of the next card is: {GPT().predicted_card_value()}\n")
            else:
                print("Please enter a valid value")
        
#Run Blackjack
GPT().play_game()

