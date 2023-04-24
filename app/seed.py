import os
from random import choice, randint
from faker import Faker
from __init__ import app
from models import db, User, Images, ImageWords, GuessedImages, InProgressImages, GameRecord, GeneratedMemes, Leaderboard

fake = Faker()

# Clear existing data and create tables
db.drop_all()
db.create_all()

# Generate fake data
NUM_USERS = 10
NUM_GUESSED_IMAGES = 100
NUM_IMAGES = 100
NUM_IN_PROGRESS_IMAGES = 50
NUM_GAME_RECORDS = 100
NUM_GENERATED_MEMES = 100

# Generate users
for _ in range(NUM_USERS):
    username = fake.user_name()
    email = fake.email()
    password = fake.password()
    phone_number = fake.phone_number()
    tagline = fake.sentence()
    bio = fake.sentence()
    user = User.signup(username=username, email=email, password=password, phone_number=phone_number, tagline=tagline, bio=bio)
    leaderboard = Leaderboard(user_id=user.id, total_score=randint(0, 100), games_played=randint(0, 50))
    db.session.add(leaderboard)
    
db.session.commit()

meme_templates = [
    {
        "id": 181913649,
        "name": "Drake Hotline Bling",
        "hint": "drakeposting, drakepost, drake hotline approves, drake no yes, drake like dislike, drake faces",
        "image_data": "https://imgflip.com/s/meme/Drake-Hotline-Bling.jpg"
    },
    {
        "id": 112126428,
        "name": "Distracted Boyfriend",
        "hint": "distracted bf, guy checking out another girl, man looking at other woman, jealous girlfriend, guy looking back, cheater temptation, wandering eyes, disloyal boyfriend",
        "image_data": "https://imgflip.com/s/meme/Distracted-Boyfriend.jpg"
    },
    {
        "id": 87743020,
        "name": "Two Buttons",
        "hint": "2 red buttons, choice button, which button, daily struggle, hard choice to make",
        "image_data": "https://imgflip.com/s/meme/Two-Buttons.jpg"
    },
    {
        "id": 129242436,
        "name": "Change My Mind",
        "hint": "Steven Crowder's sign, prove me wrong",
        "image_data": "https://imgflip.com/s/meme/Change-My-Mind.jpg"
    },
    {
        "id": 438680,
        "name": "Batman Slapping Robin",
        "hint": "cartoon comic DC character attacks sidekick",
        "image_data": "https://imgflip.com/s/meme/Batman-Slapping-Robing.jpg"
    },
    {
        "id": 124822590,
        "name": "Left Exit 12 Off Ramp",
        "hint": "car drifts off highway, sharp turn on road",
        "image_data": "https://imgflip.com/s/meme/Left-Exit-12-Off-Ramp.jpg"
    },
    {
        "id": 217743513,
        "name": "UNO Draw 25 Cards",
        "hint": "do something you don’t like or draw 25 cards, uno dilemma, uno or draw 25, draw 25",
        "image_data": "https://imgflip.com/s/meme/UNO-Draw-25-Cards.jpg"
    },
    {
        "id": 131087935,
        "name": "Running Away Balloon",
        "hint": "big yellow ball and pink guy, me vs my hopes and dreams",
        "image_data": "https://imgflip.com/s/meme/Running-Away-Balloon.jpg"
    },
    {
        "id": 61579,
        "name": "One Does Not Simply",
        "hint": "one does not simply walk into morder, lord of the rings boromir",
        "image_data": "https://imgflip.com/s/meme/One-Does-Not-Simply.jpg"
    },
    {
        "id": 93895088,
        "name": "Expanding Brain",
        "hint": "big, exploding cranium",
        "image_data": "https://imgflip.com/s/meme/Expanding-Brain.jpg"
    },
    {
        "id": 102156234,
        "name": "Mocking Spongebob",
        "hint": "spongebob mock, spongebob chicken, retarded spongebob, sarcastic spongebob, spongebob stupid, spongebob derp, spongebob bird, spongebob mocking face",
        "image_data": "https://imgflip.com/s/meme/Mocking-Spongebob.jpg"
    },
    {
        "id": 4087833,
        "name": "Waiting Skeleton",
        "hint": "skeleton waiting on bench in the park",
        "image_data": "https://imgflip.com/s/meme/Waiting-Skeleton.jpg"
    },
        {
        "id": 1035805,
        "name": "Boardroom Meeting Suggestion",
        "hint": "throw a guy out the boardroom window",
        "image_data": "https://imgflip.com/s/meme/Boardroom-Meeting-Suggestion.jpg"
    },
        {
        "id": 101470,
        "name": "Ancient Aliens",
        "hint": "Giorgio Tsoukalos, History Channel Guy",
        "image_data": "https://imgflip.com/s/meme/Ancient-Aliens.jpg"
    },
    {
        "id": 188390779,
        "name": "Woman Yelling At Cat",
        "hint": "Women yelling, confused cat, girl screaming at cat, angry woman yelling at cat at dinner table, lady screams at cat, woman pointing at cat, smudge the cat",
        "image_data": "https://imgflip.com/s/meme/Woman-Yelling-At-Cat.jpg"
    },
    {
        "id": 91538330,
        "name": "X X Everywhere	",
        "hint": "woody and buzz lightyear pointing, toy story, dicks everywhere, toystory everywhere",
        "image_data": "https://imgflip.com/s/meme/X-X-Everywhere.jpg"
    },
    {
        "id": 247375501,
        "name": "Buff Doge vs. Cheems",
        "hint": "swole doge vs cheems, strong doge weak doge, big doge small doge, then vs. now, buff doge vs. crying cheems",
        "image_data": "https://imgflip.com/s/meme/Buff-Doge-vs-Cheems.png"
    },
    {
        "id": 97984,
        "name": "Disaster Girl",
        "hint": "fire in background, pleased child",
        "image_data": "https://imgflip.com/s/meme/Disaster-Girl.jpg"
    },
    {
        "id": 89370399,
        "name": "Roll Safe Think About It",
        "hint": "thinking black guy, black guy pointing at his head, can't blank if you don't blank, smart black dude, guy tapping head",
        "image_data": "https://imgflip.com/s/meme/Roll-Safe-Think-About-It.jpg"
    },
    {
        "id": 61520,
        "name": "Futurama Fry",
        "hint": "Not sure if X or Y, Skeptical Fry",
        "image_data": "https://imgflip.com/s/meme/Futura-Fry.jpg"
    },
    {
        "id": 119139145,
        "name": "Blank Nut Button",
        "hint": "blank blue button, smash button, press button, button slam",
        "image_data": "https://imgflip.com/s/meme/Blank-Nut-Button.jpg"
    },
    {
        "id": 131940431,
        "name": "Gru's Plan",
        "hint": "Grus evil plan, Despicable Me diabolical plan, Gru's diabolical plan, gru 4 panel",
        "image_data": "https://imgflip.com/s/meme/Grus-Plan.jpg"
    },
    {
        "id": 222403160,
        "name": "Bernie I Am Once Again Asking For Your Support",
        "hint": "bernie sanders commercial, bernie sanders 2020 campaign, asking for your financial support, once again bernie",
        "image_data": "https://imgflip.com/s/meme/Bernie-I-Am-Once-Again-Asking-For-Your-Support.jpg"
    },
    {
        "id": 114585149,
        "name": "Inhaling Seagull",
        "hint": "inhaling bird",
        "image_data": "https://imgflip.com/s/meme/Inhaling-Seagull.jpg"
    },
    {
        "id": 155067746,
        "name": "Surprised Pikachu",
        "hint": "shocked pikachu",
        "image_data": "https://imgflip.com/s/meme/Surprised-Pikachu.jpg"
    },
    {
        "id": 178591752,
        "name": "Tuxedo Winnie The Pooh",
        "hint": "winnie the poo, winnie the pooh drake style, classy pooh bear, tuxedo pooh, winnie the pooh elegant, winnie pooh, winnie the pooh tux, fancy pooh",
        "image_data": "https://imgflip.com/s/meme/Tuxedo-Winnie-The-Pooh.png"
    },
    {
        "id": 5496396,
        "name": "Leonardo Dicaprio Cheers",
        "hint": "The Great Gatsby party with Jay Gatsby, gatsby toast",
        "image_data": "https://imgflip.com/s/meme/Leonardo-Dicaprio-Cheers.jpg"
    },
    {
        "id": 123999232,
        "name": "The Scroll Of Truth",
        "hint": "I’ve finally found it... after 15 years, nyehhh",
        "image_data": "https://imgflip.com/s/meme/The-Scroll-Of-Truth.jpg"
    },
    {
        "id": 61532,
        "name": "The Most Interesting Man In The World",
        "hint": "I dont always... but when I do, Dos Equis Man, I don't always",
        "image_data": "https://imgflip.com/s/meme/The-Most-Interesting-Man-In-The-World.jpg"
    },
    {
        "id": 100777631,
        "name": "Is This A Pigeon",
        "hint": "is this a pidgeon, anime butterfly guy, oblivious butterfly man anime, is this a bird, is this butterfly",
        "image_data": "https://imgflip.com/s/meme/Is-This-A-Pigeon.jpg"
    },
    {
        "id": 21735,
        "name": "The Rock Driving",
        "hint": "Race to Witch Mountain",
        "image_data": "https://imgflip.com/s/meme/The-Rock-Driving.jpg"
    },
    {
        "id": 27813981,
        "name": "Hide the Pain Harold",
        "hint": "sad life harold, maurice",
        "image_data": "https://imgflip.com/s/meme/Hide-the-Pain-Harold.jpg"
    },
    {
        "id": 8072285,
        "name": "Doge",
        "hint": "Shiba Inu",
        "image_data": "https://imgflip.com/s/meme/Doge.jpg"
    },
    {
        "id": 226297822,
        "name": "Panik Kalm Panik",
        "hint": "panic calm panic, meme man wurds",
        "image_data": "https://imgflip.com/s/meme/Panik-Kalm-Panik.jpg"
    },
    {
        "id": 61585,
        "name": "Bad Luck Brian",
        "hint": "high school photo, redhead, braces, polo",
        "image_data": "https://imgflip.com/s/meme/Bad-Luck-Brian.jpg"
    },
    {
        "id": 124055727,
        "name": "Y’all Got Any More Of That",
        "hint": "Tyrone Biggums, Dave Chappelle, Chappelles Show, yall got any more of that stuff, powder lips neck scratch",
        "image_data": "https://imgflip.com/s/meme/Yall-Got-Any-More-Of-That.jpg"
    },
    {
        "id": 135256802,
        "name": "Epic Handshake",
        "hint": "arm wrestling, holding hands, grasping hands, epic hand shake, black white arms agreement",
        "image_data": "https://imgflip.com/s/meme/Epic-Handshake.jpg"
    },
    {
        "id": 148909805,
        "name": "Monkey Puppet",
        "hint": "monkey looking away, monkey puppet avoids eye contact, hiding in plain sight, awkward look monkey",
        "image_data": "https://imgflip.com/s/meme/Monkey-Puppet.jpg"
    },
    {
        "id": 28251713,
        "name": "Oprah You Get A",
        "hint": "oprah giveway, oprah winfrey, oprah you get a car, everyone gets a car, you get an oprah, oprah excited",
        "image_data": "https://imgflip.com/s/meme/Oprah-You-Get-A.jpg"
    },
    {
        "id": 61539,
        "name": "First World Problems",
        "hint": "fwp, woman crying",
        "image_data": "https://imgflip.com/s/meme/First-World-Problems.jpg"
    },
    {
        "id": 80707627,
        "name": "Sad Pablo Escobar",
        "hint": "pablo escobar waiting, man waiting, waiting man, lonely man, narcos waiting, narcos bored, narcos alone",
        "image_data": "https://imgflip.com/s/meme/Sad-Pablo-Escobar.jpg"
    },
    {
        "id": 134797956,
        "name": "American Chopper Argument",
        "hint": "orange county choppers fight, american chopper hot take",
        "image_data": "https://imgflip.com/s/meme/American-Chopper-Argument.jpg"
    },
    {
        "id": 101288,
        "name": "Third World Skeptical Kid",
        "hint": "African skeptical child",
        "image_data": "https://imgflip.com/s/meme/Third-World-Skeptical-Kid.jpg"
    },
    {
        "id": 252600902,
        "name": "Always Has Been",
        "hint": "wait it's all just ohio, two astronauts betrayal, astronaut gun, astronaut lie, astronaut discovers conspiracy theory, always have been, it always was",
        "image_data": "https://imgflip.com/s/meme/Always-Has-Been.jpg"
    },
    {
        "id": 6235864,
        "name": "Finding Neverland",
        "hint": "Johnny Depp And Little Kid Crying",
        "image_data": "https://imgflip.com/s/meme/Finding-Neverland.jpg"
    },
    {
        "id": 61527,
        "name": "Y U No",
        "hint": "how did you not get it, frustrated, angry, cartoon",
        "image_data": "https://imgflip.com/s/meme/Y-U-No.jpg"
    },
    {
        "id": 61556,
        "name": "Grandma Finds The Internet",
        "hint": "geriatric goes online, older generation figures out technology",
        "image_data": "https://imgflip.com/s/meme/Grandma-Finds-The-Internet.jpg"
    },
    {
        "id": 175540452,
        "name": "Unsettled Tom",
        "hint": "tom face, concerned tom, tom and jerry, disgusted tom, surprised tom, tom staring down",
        "image_data": "https://imgflip.com/s/meme/Unsettled-Tom.jpg"
    },
    {
        "id": 91545132,
        "name": "Trump Bill Signing",
        "hint": "executive order trump",
        "image_data": "https://imgflip.com/s/meme/Trump-Bill-Signing.jpg"
    },
    {
        "id": 180190441,
        "name": "They're The Same Picture",
        "hint": "it's the same picture, corporate needs you to find the differences between this picture and this picture, pam from the office, office same picture, spot the difference",
        "image_data": "https://imgflip.com/s/meme/Theyre-The-Same-Picture.jpg"
    },
    {
        "id": 161865971,
        "name": "Marked Safe From",
        "hint": "facebook marked safe, marked safe flag, marked safe today, facebook safe from",
        "image_data": "https://imgflip.com/s/meme/Marked-Safe-From.jpg"
    },
    {
        "id": 563423,
        "name": "That Would Be Great",
        "hint": "Bill Lumbergh, office space, yea that'd be great",
        "image_data": "https://imgflip.com/s/meme/That-Would-Be-Great.jpg"
    },
    {
        "id": 61546,
        "name": "Brace Yourselves X is Coming",
        "hint": "imminent ned from game of thrones, brace yourselves winter is coming, brace yourself",
        "image_data": "https://imgflip.com/s/meme/Brace-Yourselves-X-is-Coming.jpg"
    },
    {
        "id": 84341851,
        "name": "Evil Kermit",
        "hint": "kermit me to me, kermit inner me, sith kermit, kermit dark side",
        "image_data": "https://imgflip.com/s/meme/Evil-Kermit.jpg"
    },
    {
        "id": 61582,
        "name": "Creepy Condescending Wonka",
        "hint": "willy wonka stare, sarcastic wonka, tell me more about X, tell me again, gene wilder",
        "image_data": "https://imgflip.com/s/meme/Creepy-Condescending-Wonka.jpg"
    },
    {
        "id": 405658,
        "name": "Grumpy Cat",
        "hint": "disgruntled kitty",
        "image_data": "https://imgflip.com/s/meme/Grumpy-Cat.jpg"
    },
    {
        "id": 61533,
        "name": "X All The Y",
        "hint": "all the things",
        "image_data": "https://imgflip.com/s/meme/X-All-The-Y.jpg"
    },
    {
        "id": 14371066,
        "name": "Star Wars Yoda",
        "hint": "master yoda",
        "image_data": "https://imgflip.com/s/meme/Star-Wars-Yoda.jpg"
    },  
    {
        "id": 61544,
        "name": "Success Kid",
        "hint": "Motivation Baby, Motivation Kid, Success Baby",
        "image_data": "https://imgflip.com/s/meme/Success-Kid.jpg"
    },
    {
        "id": 135678846,
        "name": "Who Killed Hannibal",
        "hint": "Eric Andre shooting Hannibal Buress, why would they do this",
        "image_data": "https://imgflip.com/s/meme/Who-Killed-Hannibal.jpg"
    },
    {
        "id": 16464531,
        "name": "But That's None Of My Business",
        "hint": "Kermit the frog, kermit drinking lipton iced tea",
        "image_data": "https://imgflip.com/s/meme/But-Thats-None-Of-My-Business.jpg"
    },
    {
        "id": 101511,
        "name": "Don't You Squidward",
        "hint": "spongebob grinning, spongebob smirk face, smug spongebob",
        "image_data": "https://imgflip.com/s/meme/Dont-You-Squidward.jpg"
    },
    {
        "id": 110163934,
        "name": "I Bet He's Thinking About Other Women",
        "hint": "i bet he's thinking of other woman, i bet he's thinking about other girls, couple in bed, i wonder what he's thinking, guy thinking in bed",
        "image_data": "https://imgflip.com/s/meme/I-Bet-Hes-Thinking-About-Other-Women.jpg"
    },
    {
        "id": 3218037,
        "name": "This Is Where I'd Put My Trophy If I Had One",
        "hint": "empty podium man distraught over no wins",
        "image_data": "https://imgflip.com/s/meme/This-Is-Where-Id-Put-My-Trophy-If-I-Had-One.jpg"
    },
    {
        "id": 196652226,
        "name": "Spongebob Ight Imma Head Out",
        "hint": "Ight Imma Head Out, aight imma head out, spongebob aight, alright I'm out, spongebob getting out of chair",
        "image_data": "https://imgflip.com/s/meme/Spongebob-Ight-Imma-Head-Out.jpg"
    },
    {
        "id": 1509839,
        "name": "Captain Picard Facepalm",
        "hint": "star trek face palm",
        "image_data": "https://imgflip.com/s/meme/Captain-Picard-Facepalm.jpg"
    },
    {
        "id": 55311130,
        "name": "This Is Fine",
        "hint": "this is fine dog, dog house fire, dog in burning house, house on fire",
        "image_data": "https://imgflip.com/s/meme/This-Is-Fine.jpg"
    },
    {
        "id": 101287,
        "name": "Third World Success Kid",
        "hint": "happy african child, african kids dancing",
        "image_data": "https://imgflip.com/s/meme/Third-World-Success-Kid.jpg"
    },
    {
        "id": 235589,
        "name": "Evil Toddler",
        "hint": "evil baby",
        "image_data": "https://imgflip.com/s/meme/Evil-Toddler.jpg"
    },
    {
        "id": 100947,
        "name": "Matrix Morpheus",
        "hint": "what if I told you",
        "image_data": "https://imgflip.com/s/meme/Matrix-Morpheus.jpg"
    },
    {
        "id": 79132341,
        "name": "Bike Fall",
        "hint": "falling off bike, baton roue, stick in bike wheel, bike stick, bicycle stick, bike blame, falling bike",
        "image_data": "https://imgflip.com/s/meme/Bike-Fall.jpg"
    },
    {
        "id": 61516,
        "name": "Philosoraptor",
        "hint": "green dinosaur, dinosaur wondering",
        "image_data": "https://imgflip.com/s/meme/Philosoraptor.jpg"
    },
    {
        "id": 195515965,
        "name": "Clown Applying Makeup",
        "hint": "putting on clown makeup, clown face, clown paint, becoming a clown",
        "image_data": "https://imgflip.com/s/meme/Clown-Applying-Makeup.jpg"
    },
    {
        "id": 132769734,
        "name": "Hard To Swallow Pills",
        "hint": "hard pills to swallow",
        "image_data": "https://imgflip.com/s/meme/Hard-To-Swallow-Pills.jpg"
    },
    {
        "id": 14230520,
        "name": "Black Girl Wat",
        "hint": "confused black girl, black girl with hand out, seriously black girl",
        "image_data": "https://imgflip.com/s/meme/Black-Girl-Wat.jpg"
    },
    {
        "id": 245898,
        "name": "Picard Wtf",
        "hint": "captain jean-luc picard star trek, annoyed picard, why the fuck would you",
        "image_data": "https://imgflip.com/s/meme/Picard-Wtf.jpg"
    },
    {
        "id": 99683372,
        "name": "Sleeping Shaq",
        "hint": "i sleep, real shit",
        "image_data": "https://imgflip.com/s/meme/Sleeping-Shaq.jpg"
    },
    {
        "id": 101440,
        "name": "10 Guy",
        "hint": "Really High Guy, Stoner Stanley, Brainwashed Bob, stoned guy, ten guy",
        "image_data": "https://imgflip.com/s/meme/10-Guy.jpg"
    },
    {
        "id": 922147,
        "name": "Laughing Men In Suits",
        "hint": "Men laughing, And then I said, And then I told them, rich men laughing",
        "image_data": "https://imgflip.com/s/meme/Laughing-Men-In-Suits.jpg"
    },
    {
        "id": 61580,
        "name": "Too Damn High",
        "hint": "The rent is too damn high",
        "image_data": "https://imgflip.com/s/meme/Too-Damn-High.jpg"
    },
    {
        "id": 259237855,
        "name": "Laughing Leo",
        "hint": "Leonardo DiCaprio laughing, Django Laughing Leo, Django Unchained laugh, laughing while holding a drink, Calvin Candie laugh",
        "image_data": "https://imgflip.com/s/meme/Laughing-Leo.jpg"
    },
    {
        "id": 101716,
        "name": "Yo Dawg Heard You Xzibit",
        "hint": "Yo dawg we heard you like Y so we put some X in your X so you can Y while you Y",
        "image_data": "https://imgflip.com/s/meme/Yo-Dawg-Heard-You-Xzibit.jpg"
    },
    {
        "id": 40945639,
        "name": "Dr Evil Laser",
        "hint": "Dr. Evil quotation marks, Dr Evil Air Quotes",
        "image_data": "https://imgflip.com/s/meme/Dr-Evil-Laser.jpg"
   },
    {
        "id": 259680,
        "name": "Am I The Only One Around Here",
        "hint": "Angry Walter from The Big Lebowski",
        "image_data": "https://imgflip.com/s/meme/Am-I-The-Only-One-Around-Here.jpg"
    },
    {
        "id": 109765,
        "name": "I’ll Just Wait Here",
        "hint": "waiting skeleton",
        "image_data": "https://imgflip.com/s/meme/Ill-Just-Wait-Here.jpg"
    },
    {
        "id": 9440985,
        "name": "Face You Make Robert Downey Jr",
        "hint": "Robert Downey Jr",
        "image_data": "https://imgflip.com/s/meme/Face-You-Make-Robert-Downey-Jr.jpg"
    },
    {
        "id": 61581,
        "name": "Put It Somewhere Else Patrick",
        "hint": "patrick from spongebob",
        "image_data": "https://imgflip.com/s/meme/Put-It-Somewhere-Else-Patrick.jpg"
    },
    {
        "id": 56225174,
        "name": "Be Like Bill",
        "hint": "bill the stick figure with a hat",
        "image_data": "https://imgflip.com/s/meme/Be-Like-Bill.jpg"
    },
    {
        "id": 12403754,
        "name": "Bad Pun Dog",
        "hint": "joke dog, whisper joke dog, happy husky, joke telling husky, pun husky",
        "image_data": "https://imgflip.com/s/meme/Bad-Pun-Dog.jpg"
    },
    {
        "id": 163573,
        "name": "Imagination Spongebob",
        "hint": "spongebob rainbow, nobody cares",
        "image_data": "https://imgflip.com/s/meme/Imagination-Spongebob.jpg"
    },
    {
        "id": 460541,
        "name": "Jack Sparrow Being Chased",
        "hint": "pirates of the caribbean",
        "image_data": "https://imgflip.com/s/meme/Jack-Sparrow-Being-Chased.jpg"
    },
    {
        "id": 21604248,
        "name": "Mugatu So Hot Right Now",
        "hint": "Mugatu from Zoolander, Will Farrell",
        "image_data": "https://imgflip.com/s/meme/Mugatu-So-Hot-Right-Now.jpg"
    },
    {
        "id": 29617627,
        "name": "Look At Me",
        "hint": "I’m the captain now, captain phillips",
        "image_data": "https://imgflip.com/s/meme/Look-At-Me.jpg"
    },
    {
        "id": 195389,
        "name": "Sparta Leonidas",
        "hint": "Leonidas from the movie 300",
        "image_data": "https://imgflip.com/s/meme/Sparta-Leonidas.jpg"
    },
    {
        "id": 444501,
        "name": "Maury Lie Detector",
        "hint": "The lie detector determined that was a lie. The fact that you X determined that was a lie. Maury Povich.",
        "image_data": "https://imgflip.com/s/meme/Maury-Lie-Detector.jpg"
    },
    {
        "id": 100955,
        "name": "Confession Bear",
        "hint": "sad mammal, admitting fault",
        "image_data": "https://imgflip.com/s/meme/Confession-Bear.jpg"
    },
    {
        "id": 766986,
        "name": "Aaaaand Its Gone",
        "hint": "and it's gone, south park banker guy",
        "image_data": "https://imgflip.com/s/meme/Aaaaand-Its-Gone.jpg"
    },
    {
        "id": 6531067,
        "name": "See Nobody Cares",
        "hint": "Jurassic Park Dennis",
        "image_data": "https://imgflip.com/s/meme/See-Nobody-Cares.jpg"
    },
    {
        "id": 1367068,
        "name": "I Should Buy A Boat Cat",
        "hint": "sophisticated cat, fancy cat, newspaper cat",
        "image_data": "https://imgflip.com/s/meme/I-Should-Buy-A-Boat-Cat.jpg"
    },
    {
        "id": 260755514,
        "name": "Wake Up Babe",
        "hint": "sleeping couple, man above woman",
        "image_data": "https://i.imgflip.com/4b8w8q.jpg"
    },
    {
        "id": 4173692,
        "name": "Scared Cat",
        "hint": "fearful feline",
        "image_data": "https://imgflip.com/s/meme/Scared-Cat.jpg"
    }
]

for meme_template in meme_templates:
    image = Images(
        phrase=meme_template["name"],
        hint=meme_template["hint"],
        image_data=meme_template["image_data"],
        template_id=meme_template["id"]
    )
    db.session.add(image)
    db.session.flush()

    # Generate image words
    words = meme_template["name"].split(" ")
    for word in words:
        image_word = ImageWords(word=word, image_id=image.id)
        db.session.add(image_word)

db.session.commit()

# Generate guessed images, in progress images, game records, and generated memes
for _ in range(NUM_GUESSED_IMAGES):
    guessed_image = GuessedImages(
        image_id=randint(1, NUM_IMAGES),
        user_id=randint(1, NUM_USERS),
        round=randint(1, 10),
        completed=choice([True, False])
    )
    db.session.add(guessed_image)

    if not guessed_image.completed:
        in_progress_image = InProgressImages(
            image_id=guessed_image.image_id,
            user_id=guessed_image.user_id,
            in_round=choice([True, False])
        )
        db.session.add(in_progress_image)

    game_record = GameRecord(
        user_id=guessed_image.user_id,
        guessed_image_id=guessed_image.id,
        round=randint(1, 10)
    )
    db.session.add(game_record)

    generated_meme = GeneratedMemes(
        image_id=guessed_image.image_id,
        user_id=guessed_image.user_id,
        is_favorite=choice([True, False])
    )
    db.session.add(generated_meme)

# Commit the changes
db.session.commit()
