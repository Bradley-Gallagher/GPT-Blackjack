# GPT-Blackjack
To start playing simply run the code each time you want to play a round of blackjack - however you will first need to enter an API key to use ChatGPT.

The game works by asking ChatGPT to draw cards at random for the user and the dealer. The user may ask ChatGPT for advice (through limited options) or to make a move (hit or stand).
Once the user has finished, ChatGPT will play for the dealer by calculating recommended moves and following those recommendations until it stands.

In this game, ChatGPT is used to facilitate playing a simple card game. Although this could be done almost entirely without any code by using the ChatGPT website, once an API is used this becomes complicated. The API version was less cooperative in playing card games and would refuse to start the game. 
Additionally, it would not remember who had which cards which meant that it could not serve as a foundation to host the game.
As a result, GPT was used to facilitate the basic funcitonality of the game (drawing cards at random), making predictions (chances of winning, or best moves), and determining winners.
This functionality could be expanded to learning algorithms such as detecing card counting - e.g., what is the predicted value of the next card and how would someone react to that - if someone follows the patterns outlined by GPT to a high degree, they may be cheating.
Other functionality could also be included for playing other games too.

When interacting with GPT, a long response may be given which would needed to be reduced and parsed to find the item of interest (e.g., a cards value), therefore it was consistently instructed to respond in one word outputs where possible so that the output would be consistent and easily dealt with by a seperate system.
If this was not the case, the system running the game would frequently produce errors.
