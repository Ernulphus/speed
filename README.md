# Card Game "Speed"

Run with ``python3 main.py``.
The objective of the game is to play all your cards first, or play more cards than your opponent if it is impossible for either player to play all their cards.
Select a card in your hand with a, s, d, f, w, e, and r in that order (first four are left hand's home position, the last three are reaching up with the ring, middle, and index fingers.)
Play the selected card to the left pile with j or to the right pile with k - you can play a card on a pile if the top card of the pile has a rank that is one above or one below your card. 

You can draw a card from your deck (on the right) by hitting space. Maximum hand size is 7.
If neither player can play a card, the game will display "stuck" and you can hit semicolon (;) to clear the piles and place a new card from each deck onto its pile. If a deck is empty, both cards will come from a single deck as a catch-up mechanic.

Aces (A) wrap around and can be played on a K or a 2.
X represents 10 so that it can be a single character wide. J is jack, Q is queen, and K is king.

The game is currently only single player against the computer.

To do list:
- Title menu / ending menu
- Multiple difficulties (faster or slower AI, more sophisticated AI hand routing)
- Local multiplayer
- Online multiplayer