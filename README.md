# Settlers of Catan: AI Simulator
To run: navigate to >ai-catan>code, then `python main.py` 
## I ) Program Description
This program explores several uses of AI for playing Settlers of Catan. Does initial settlement location really determine who will win in the end? How much is this a skill-based game, and how much can be attributed to randomness or pure luck? Let's find out.
By utilizing a trained multiple linear regression model to choose settlement locations, and a rule-based option selector for playing out the game, 3 computers can compete in a full match against eachother. 
  1. Run thousands of simulations quickly to collect training data for your own research (with output to outputdata.csv)
  2. Plug in personalized board coordinates to see which locations our computer(s) would find most optimal
  3. View a single match progression on a  visualized board position print-out to output.txt

## II ) Supported Game Mechanics
  1. Resource Collecting
  2. Building roads, settlements, and cities
  3. Trading in to the bank (only 4 for 1 trades) if it benefits the player
  4. Robber gets placed if 7 is rolled; players containing > 7 cards must discard half their deck

## III ) What isn't supported (yet)
  1. Trading with other players
  2. Ports
  3. Development cards
  4. Rewards for longest road / largest army

## IV) External Libraries and Resources Utilized
  1. Pandas
  2. Numpy
  3. Sklearn
  4. https://www.kaggle.com/lumins/settlers-of-catan-games - for initial training set. Subsequent training taken from our own simulations