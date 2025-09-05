import random

emotion_data = {
    "admiration": {
        "quotes": [
            "Admiration is the highest form of flattery.",
            "To admire is to see the beauty of another's soul.",
            "Admiration is the gateway to inspiration.",
            "Great minds inspire admiration.",
            "Admire others and you elevate yourself.",
            "Admiration opens hearts and minds.",
            "True admiration is expressed through actions.",
            "Admiration is the spark of creativity.",
            "Admire what you love, and it will inspire you.",
            "Admiration strengthens the bonds of friendship."
        ],
        "activities": [
            "Write a thank-you note to someone you admire",
            "Take a walk and notice beauty around you",
            "Try a creative activity like painting",
            "Read a biography of someone inspiring",
            "Watch a documentary about innovators"
        ],
        "games": ["Uncharted 4", "Tales of Arise", "Ori and the Will of the Wisps"],
        "books": ["Steve Jobs by Walter Isaacson", "Long Walk to Freedom by Nelson Mandela", "Educated by Tara Westover"],
        "movies": ["Hidden Figures", "The Social Network", "The Imitation Game"]
    },
    "amusement": {
        "quotes": [
            "Laughter is the best medicine.",
            "Amusement is the spice of life.",
            "A day without laughter is a day wasted.",
            "Smile, it increases your face value.",
            "Amusement lightens the heart and soul.",
            "Happiness is homemade.",
            "Fun is the secret ingredient of life.",
            "A sense of humor is a sense of proportion.",
            "Amusement is contagious, spread it around.",
            "Laugh, and the world laughs with you."
        ],
        "activities": [
            "Watch a comedy show or movie",
            "Play a lighthearted or humorous game",
            "Call a friend and share jokes",
            "Try an improv or acting exercise",
            "Write funny short stories"
        ],
        "games": ["Untitled Goose Game", "Psychonauts 2", "Human: Fall Flat"],
        "books": ["Good Omens by Neil Gaiman & Terry Pratchett", "The Hitchhiker's Guide to the Galaxy by Douglas Adams", "Bossypants by Tina Fey"],
        "movies": ["The Grand Budapest Hotel", "Paddington 2", "The Mask"]
    },
    "anger": {
        "quotes": [
            "For every minute you remain angry, you give up sixty seconds of peace.",
            "Anger is an acid that can do more harm to the vessel in which it is stored than to anything on which it is poured.",
            "Speak when you are angry and you will make the best speech you will ever regret.",
            "The best fighter is never angry.",
            "Anger dwells only in the bosom of fools.",
            "Control your anger or it will control you.",
            "Anger is a wind which blows out the lamp of the mind.",
            "He who angers you conquers you.",
            "Holding on to anger is like grasping a hot coal with the intent of throwing it at someone else.",
            "To be angry is to revenge the faults of others on ourselves."
        ],
        "activities": [
            "Go for a run or workout",
            "Practice deep breathing or meditation",
            "Write down your feelings in a journal",
            "Listen to calming music",
            "Do a creative outlet like drawing or music"
        ],
        "games": ["The Witcher 3", "Red Dead Redemption 2", "Firewatch", "Life is Strange", "Cyberpunk 2077"],
        "books": ["Anger: Wisdom for Cooling the Flames by Thich Nhat Hanh", "The Dance of Anger by Harriet Lerner", "Emotional Intelligence by Daniel Goleman"],
        "movies": ["Inside Out", "Gran Torino", "The Pursuit of Happyness"]
    },
    "annoyance": {
        "quotes": [
            "Annoyance is the price of individuality.",
            "Patience is the key to overcoming annoyance.",
            "Annoyance is a reminder to breathe.",
            "Let go of small irritations.",
            "Annoyance fades faster than anger.",
            "Take a step back when annoyed.",
            "Annoyance is an opportunity to practice tolerance.",
            "Respond with calm, not irritation.",
            "Annoyance is temporary, wisdom is permanent.",
            "Laugh at minor annoyances."
        ],
        "activities": [
            "Listen to soothing music",
            "Play a story-driven game to distract yourself",
            "Take a short walk",
            "Try a mindfulness exercise",
            "Watch a lighthearted movie"
        ],
        "games": ["Firewatch", "Life is Strange", "Journey"],
        "books": ["The Art of Happiness by Dalai Lama", "The Book of Joy by Dalai Lama & Desmond Tutu", "Calm by Michael Acton Smith"],
        "movies": ["Inside Out", "Paddington 2", "Forrest Gump"]
    },
    "approval": {
        "quotes": [
            "Approval is sweet, but self-approval is sweeter.",
            "Respect and approval are earned through kindness.",
            "Seek approval from yourself, not others.",
            "Approval encourages growth and courage.",
            "Genuine approval uplifts the spirit.",
            "Approval is a sign of connection.",
            "Approval can inspire creativity.",
            "A kind word of approval brightens the day.",
            "Approval nurtures confidence.",
            "True approval comes from understanding."
        ],
        "activities": [
            "Compliment someone genuinely",
            "Write down achievements you're proud of",
            "Play a cooperative story-driven game",
            "Read inspiring books",
            "Watch motivational movies"
        ],
        "games": ["Uncharted 4", "Horizon Zero Dawn", "Firewatch"],
        "books": ["Daring Greatly by Brené Brown", "The Confidence Code by Katty Kay & Claire Shipman", "Big Magic by Elizabeth Gilbert"],
        "movies": ["The Pursuit of Happyness", "Hidden Figures", "Joy"]
    },
    "caring": {
        "quotes": [
            "To care for others is to care for yourself.",
            "Caring is love in action.",
            "A caring heart changes the world.",
            "Kindness begins with caring.",
            "Caring is the essence of humanity.",
            "Care deeply, act gently.",
            "Caring is contagious.",
            "To care is to be alive.",
            "Caring is a form of strength.",
            "Every act of caring is a step toward peace."
        ],
        "activities": [
            "Volunteer for a local cause",
            "Send a thoughtful message to a friend",
            "Play cooperative story games",
            "Read heartwarming books",
            "Watch feel-good movies"
        ],
        "games": ["Stardew Valley", "Spiritfarer", "Life is Strange"],
        "books": ["Wonder by R.J. Palacio", "The Giving Tree by Shel Silverstein", "To Kill a Mockingbird by Harper Lee"],
        "movies": ["The Pursuit of Happyness", "Coco", "Paddington 2"]
    },
    "confusion": {
        "quotes": [
            "Confusion is the beginning of clarity.",
            "In confusion lies opportunity.",
            "Embrace confusion, it teaches patience.",
            "Confusion is the spark of curiosity.",
            "Seek answers, not certainty.",
            "Confusion precedes understanding.",
            "Even chaos has its pattern.",
            "Confusion is a path to insight.",
            "Step back and breathe in confusion.",
            "Curiosity thrives in confusion."
        ],
        "activities": [
            "Meditate or do mindfulness exercises",
            "Play puzzle or story-driven games",
            "Read a thought-provoking book",
            "Take a walk to clear your mind",
            "Write down your thoughts to organize them"
        ],
        "games": ["The Witness", "Myst", "Return of the Obra Dinn"],
        "books": ["Thinking, Fast and Slow by Daniel Kahneman", "Sapiens by Yuval Noah Harari", "The Art of Thinking Clearly by Rolf Dobelli"],
        "movies": ["Inception", "Shutter Island", "Memento"]
    },
    "curiosity": {
        "quotes": [
            "Curiosity is the wick in the candle of learning.",
            "The important thing is not to stop questioning.",
            "Curiosity is the engine of achievement.",
            "Curiosity keeps the mind alive.",
            "Curiosity is the beginning of knowledge.",
            "Let your curiosity lead you.",
            "Curiosity creates opportunities.",
            "Curiosity is the gateway to discovery.",
            "Stay curious and explore.",
            "Curiosity is the spark of innovation."
        ],
        "activities": [
            "Explore a new topic online",
            "Play a mystery or story-driven game",
            "Visit a museum or art gallery",
            "Read an educational book",
            "Ask someone questions and learn"
        ],
        "games": ["Outer Wilds", "Myst", "The Witness", "Firewatch"],
        "books": ["Sapiens by Yuval Noah Harari", "Astrophysics for People in a Hurry by Neil deGrasse Tyson", "Cosmos by Carl Sagan"],
        "movies": ["Interstellar", "The Martian", "Arrival"]
    },
    "desire": {
        "quotes": [
            "Desire is the starting point of all achievement.",
            "Keep your desires pure and your efforts strong.",
            "Desire is the fuel of passion.",
            "The key to happiness is wanting what you have.",
            "Desire motivates action.",
            "Desire with purpose leads to fulfillment.",
            "Let desire guide, not blind.",
            "True desire is aligned with values.",
            "Desire can transform dreams into reality.",
            "Desire is the heartbeat of ambition."
        ],
        "activities": [
            "Set achievable goals",
            "Play a story-driven game to inspire",
            "Write down what you truly want",
            "Read motivational books",
            "Watch inspirational movies"
        ],
        "games": ["The Witcher 3", "Red Dead Redemption 2", "Life is Strange", "Uncharted 4"],
        "books": ["The Alchemist by Paulo Coelho", "Think and Grow Rich by Napoleon Hill", "Big Magic by Elizabeth Gilbert"],
        "movies": ["The Pursuit of Happyness", "Inception", "The Secret Life of Walter Mitty"]
    },
    "disappointment": {
        "quotes": [
            "Disappointment is a natural part of life.",
            "Every disappointment is a blessing in disguise.",
            "Disappointment teaches patience.",
            "Expect less, appreciate more.",
            "Disappointment is temporary; lessons are permanent.",
            "Turn disappointment into motivation.",
            "Disappointment is the tuition you pay for wisdom.",
            "Do not let disappointment define you.",
            "Face disappointment with resilience.",
            "Disappointment is a stepping stone to growth."
        ],
        "activities": [
            "Write about your feelings",
            "Play a story-driven game to escape and reflect",
            "Listen to calming music",
            "Take a walk or meditate",
            "Read inspiring books"
        ],
        "games": ["Firewatch", "Life is Strange", "What Remains of Edith Finch"],
        "books": ["The Art of Happiness by Dalai Lama", "Man's Search for Meaning by Viktor Frankl", "When Things Fall Apart by Pema Chödrön"],
        "movies": ["Inside Out", "Good Will Hunting", "The Pursuit of Happyness"]
    },
    "disapproval": {
        "quotes": [
            "Disapproval is often the mirror of our own doubts.",
            "Express opinions with respect.",
            "Disapproval should be constructive.",
            "Criticism is a tool for growth.",
            "Disapproval fades with understanding.",
            "Seek truth, not judgment.",
            "Disapproval can teach patience.",
            "Judge less, understand more.",
            "Disapproval can refine ideas.",
            "Disapproval should be a guide, not a weapon."
        ],
        "activities": [
            "Reflect on why you feel disapproval",
            "Play cooperative story-driven games",
            "Read books to broaden perspective",
            "Watch a thought-provoking movie",
            "Practice empathy exercises"
        ],
        "games": ["Uncharted 4", "Life is Strange", "Firewatch"],
        "books": ["The Art of Thinking Clearly by Rolf Dobelli", "How to Win Friends & Influence People by Dale Carnegie", "Emotional Intelligence by Daniel Goleman"],
        "movies": ["12 Angry Men", "The Social Network", "A Beautiful Mind"]
    },
    "disgust": {
        "quotes": [
            "Disgust protects the mind from harm.",
            "Disgust is often a guide to values.",
            "Learn to rise above disgust.",
            "Disgust fades with understanding.",
            "Control your reactions, not the world.",
            "Disgust can teach self-awareness.",
            "Disgust is natural, but not permanent.",
            "Transform disgust into curiosity.",
            "Disgust often hides fear or discomfort.",
            "Disgust is a signal, not a command."
        ],
        "activities": [
            "Take a walk to refresh your mind",
            "Play a calming story-driven game",
            "Read an inspiring book",
            "Listen to soothing music",
            "Do a relaxing hobby"
        ],
        "games": ["Firewatch", "Life is Strange", "Journey"],
        "books": ["Man's Search for Meaning by Viktor Frankl", "Emotional Intelligence by Daniel Goleman", "The Book of Joy by Dalai Lama & Desmond Tutu"],
        "movies": ["Inside Out", "Forrest Gump", "Paddington 2"]
    },
    "embarrassment": {
        "quotes": [
            "Embarrassment is temporary; learning is permanent.",
            "Everyone feels embarrassed sometimes.",
            "Embarrassment builds humility.",
            "Laugh at your mistakes.",
            "Embarrassment fades faster than you think.",
            "Face embarrassment with courage.",
            "Embarrassment is a stepping stone.",
            "Self-compassion conquers embarrassment.",
            "Embarrassment teaches resilience.",
            "Embarrassment is proof that you tried."
        ],
        "activities": [
            "Laugh it off and move on",
            "Play a lighthearted story-driven game",
            "Write about your experience",
            "Talk to a friend you trust",
            "Watch a funny movie"
        ],
        "games": ["Untitled Goose Game", "Psychonauts 2", "Firewatch"],
        "books": ["The Gifts of Imperfection by Brené Brown", "Daring Greatly by Brené Brown", "Bossypants by Tina Fey"],
        "movies": ["The Mask", "Mean Girls", "Paddington 2"]
    },
    "excitement": {
        "quotes": [
            "Excitement is energy in motion.",
            "Ride the wave of excitement.",
            "Excitement fuels creativity.",
            "Embrace the thrill of new experiences.",
            "Excitement is contagious, spread it.",
            "Stay curious and excited.",
            "Excitement makes life colorful.",
            "Harness excitement for growth.",
            "Excitement is passion expressed.",
            "Excitement opens new doors."
        ],
        "activities": [
            "Play an adventure or story-driven game",
            "Try a new hobby",
            "Go on a mini adventure",
            "Read an engaging book",
            "Watch an inspiring movie"
        ],
        "games": ["Uncharted 4", "The Witcher 3", "Life is Strange"],
        "books": ["Harry Potter series by J.K. Rowling", "Percy Jackson series by Rick Riordan", "The Hunger Games by Suzanne Collins"],
        "movies": ["Inception", "Guardians of the Galaxy", "Spider-Man: Into the Spider-Verse"]
    },
    "fear": {
        "quotes": [
            "Fear is only as deep as the mind allows.",
            "Face your fears and rise.",
            "Fear is a teacher, not a jailer.",
            "Courage is acting despite fear.",
            "Fear reveals what you value.",
            "Transform fear into curiosity.",
            "Fear is temporary; growth is permanent.",
            "Don't let fear dictate your life.",
            "Fear challenges us to be brave.",
            "Understanding fear dissolves it."
        ],
        "activities": [
            "Try controlled breathing or meditation",
            "Play immersive story-driven games",
            "Read empowering books",
            "Watch movies with positive messages",
            "Write about your fears"
        ],
        "games": ["Alan Wake", "Life is Strange", "Firewatch"],
        "books": ["Feel the Fear and Do It Anyway by Susan Jeffers", "The Gift of Fear by Gavin de Becker", "Daring Greatly by Brené Brown"],
        "movies": ["A Quiet Place", "Coraline", "The Secret Life of Walter Mitty"]
    },
    "gratitude": {
        "quotes": [
            "Gratitude turns what we have into enough.",
            "Gratitude is the fairest blossom which springs from the soul.",
            "Start each day with a grateful heart.",
            "Gratitude unlocks happiness.",
            "Gratitude is a magnet for miracles.",
            "Feeling grateful magnifies joy.",
            "Gratitude changes perspective.",
            "Gratitude is a daily practice.",
            "Express gratitude often.",
            "Gratitude enriches life."
        ],
        "activities": [
            "Write a gratitude journal",
            "Send a thank-you message",
            "Play cooperative story-driven games",
            "Read uplifting books",
            "Watch heartwarming movies"
        ],
        "games": ["Stardew Valley", "Spiritfarer", "Life is Strange"],
        "books": ["The Gratitude Diaries by Janice Kaplan", "Thanks! How Practicing Gratitude Can Make You Happier by Robert Emmons", "A Simple Act of Gratitude by John Kralik"],
        "movies": ["Coco", "The Pursuit of Happyness", "Paddington 2"]
    },
    "grief": {
        "quotes": [
            "Grief is the price we pay for love.",
            "Tears are the silent language of grief.",
            "Grief is a journey, not a destination.",
            "Allow yourself to feel grief fully.",
            "Grief transforms, it does not destroy.",
            "Healing comes in waves.",
            "Grief is proof of deep connection.",
            "Time softens the sharp edges of grief.",
            "Sharing grief eases the burden.",
            "Grief teaches us compassion."
        ],
        "activities": [
            "Write your feelings in a journal",
            "Play emotional story-driven games",
            "Read comforting books",
            "Watch tearjerker movies",
            "Take quiet walks to reflect"
        ],
        "games": ["What Remains of Edith Finch", "Life is Strange", "Firewatch"],
        "books": ["A Grief Observed by C.S. Lewis", "Option B by Sheryl Sandberg", "The Year of Magical Thinking by Joan Didion"],
        "movies": ["Manchester by the Sea", "Bridge to Terabithia", "Inside Out"]
    },
    "joy": {
        "quotes": [
            "Joy is not in things; it is in us.",
            "Find joy in the little things.",
            "Joy multiplies when shared.",
            "Joy is the simplest form of gratitude.",
            "Spread joy wherever you go.",
            "Joy is a light that shines within.",
            "Joy cannot be bought, only felt.",
            "True joy is found in moments.",
            "Joy is contagious, give it freely.",
            "Let joy be your compass."
        ],
        "activities": [
            "Dance or listen to upbeat music",
            "Play fun story-driven games",
            "Read uplifting books",
            "Spend time with friends",
            "Watch feel-good movies"
        ],
        "games": ["Stardew Valley", "Animal Crossing", "Life is Strange", "Unravel"],
        "books": ["The Book of Joy by Dalai Lama & Desmond Tutu", "Happier by Tal Ben-Shahar", "Big Magic by Elizabeth Gilbert"],
        "movies": ["Paddington 2", "Coco", "The Secret Life of Walter Mitty"]
    },
    "love": {
        "quotes": [
            "Love all, trust a few.",
            "Love is composed of a single soul inhabiting two bodies.",
            "Where there is love there is life.",
            "Love is the bridge between you and everything.",
            "The best thing to hold onto in life is each other.",
            "Love is the ultimate adventure.",
            "Love yourself first.",
            "Love is the greatest refreshment in life.",
            "True love stories never have endings.",
            "Love is a verb, act upon it daily."
        ],
        "activities": [
            "Write a love note",
            "Spend quality time with loved ones",
            "Play cooperative story-driven games",
            "Read romance novels",
            "Watch romantic movies"
        ],
        "games": ["Life is Strange", "Firewatch", "Stardew Valley", "Florence"],
        "books": ["Pride and Prejudice by Jane Austen", "The Fault in Our Stars by John Green", "Me Before You by Jojo Moyes"],
        "movies": ["The Notebook", "Coco", "La La Land"]
    },
    "nervousness": {
        "quotes": [
            "Nervousness is the excitement in disguise.",
            "Take a deep breath, you’ve got this.",
            "Nervous energy can be transformed into action.",
            "Nerves are a sign you care.",
            "Courage is not the absence of fear.",
            "Step forward despite nervousness.",
            "Focus on the process, not the outcome.",
            "Nervousness fades with preparation.",
            "Embrace nervousness, it means growth.",
            "Turn nerves into fuel."
        ],
        "activities": [
            "Practice deep breathing",
            "Play relaxing story-driven games",
            "Listen to calming music",
            "Write a plan to reduce uncertainty",
            "Read motivational books"
        ],
        "games": ["Firewatch", "Life is Strange", "Journey"],
        "books": ["Feel the Fear and Do It Anyway by Susan Jeffers", "The Confidence Code by Katty Kay & Claire Shipman", "Daring Greatly by Brené Brown"],
        "movies": ["Inside Out", "The Secret Life of Walter Mitty", "Coco"]
    },
    "optimism": {
        "quotes": [
            "Optimism is the faith that leads to achievement.",
            "Keep your face toward the sunshine.",
            "Optimism is a happiness magnet.",
            "Positive thinking brings positive results.",
            "Optimism fuels resilience.",
            "Optimism makes hard work enjoyable.",
            "Believe in better days.",
            "Optimism transforms challenges into opportunities.",
            "Optimism is contagious.",
            "A positive mind sees positive outcomes."
        ],
        "activities": [
            "Write down positive affirmations",
            "Play uplifting story-driven games",
            "Read inspiring books",
            "Spend time in nature",
            "Watch motivational movies"
        ],
        "games": ["Stardew Valley", "Life is Strange", "Unravel"],
        "books": ["The Power of Positive Thinking by Norman Vincent Peale", "The Happiness Advantage by Shawn Achor", "Big Magic by Elizabeth Gilbert"],
        "movies": ["The Pursuit of Happyness", "Coco", "Paddington 2"]
    },
    "pride": {
        "quotes": [
            "Pride is the fruit of achievement.",
            "Let your pride be in your work.",
            "Take pride in small victories.",
            "Pride motivates excellence.",
            "Healthy pride fuels confidence.",
            "Celebrate your accomplishments.",
            "Pride is the evidence of effort.",
            "True pride comes from humility.",
            "Pride strengthens character.",
            "Pride should inspire, not divide."
        ],
        "activities": [
            "Write down accomplishments",
            "Play a story-driven game and celebrate milestones",
            "Read biographies of achievers",
            "Share your achievements with friends",
            "Watch motivational movies"
        ],
        "games": ["Uncharted 4", "The Witcher 3", "Life is Strange"],
        "books": ["Daring Greatly by Brené Brown", "Mindset by Carol Dweck", "Grit by Angela Duckworth"],
        "movies": ["Hidden Figures", "The Pursuit of Happyness", "Rocky"]
    },
    "realization": {
        "quotes": [
            "Realization is the dawn of awareness.",
            "The first step to change is realization.",
            "Realization brings clarity.",
            "Every realization is a lesson.",
            "Awareness is the gateway to wisdom.",
            "Self-realization is life’s greatest gift.",
            "Realization is power in disguise.",
            "Understand to transform.",
            "Moments of realization shape destiny.",
            "Realization lights the path forward."
        ],
        "activities": [
            "Reflect through journaling",
            "Play thought-provoking story-driven games",
            "Read philosophical books",
            "Meditate to absorb insights",
            "Watch reflective movies"
        ],
        "games": ["Firewatch", "Life is Strange", "The Witness"],
        "books": ["Sapiens by Yuval Noah Harari", "The Art of Happiness by Dalai Lama", "Thinking, Fast and Slow by Daniel Kahneman"],
        "movies": ["Inception", "The Truman Show", "Memento"]
    },
    "relief": {
        "quotes": [
            "Relief is the reward of endurance.",
            "A sigh of relief is a song of victory.",
            "Relief follows perseverance.",
            "Let go and feel relief.",
            "Relief brings peace to the mind.",
            "Every struggle ends in relief.",
            "Relief is the calm after the storm.",
            "Relief is a gentle blessing.",
            "Savor moments of relief.",
            "Relief is gratitude in disguise."
        ],
        "activities": [
            "Take a deep breath and relax",
            "Play calming story-driven games",
            "Listen to soothing music",
            "Read a light-hearted book",
            "Watch feel-good movies"
        ],
        "games": ["Journey", "Stardew Valley", "Firewatch"],
        "books": ["The Book of Joy by Dalai Lama & Desmond Tutu", "Calm by Michael Acton Smith", "The Art of Happiness by Dalai Lama"],
        "movies": ["Paddington 2", "Coco", "The Secret Life of Walter Mitty"]
    },
    "remorse": {
        "quotes": [
            "Remorse is the path to redemption.",
            "Admit mistakes, learn, and move on.",
            "Remorse is the seed of growth.",
            "Forgive yourself and act better.",
            "Remorse teaches empathy.",
            "Acknowledge, reflect, and improve.",
            "Remorse is a teacher of conscience.",
            "Change starts with remorse.",
            "Regret is wasted energy, remorse is learning.",
            "Remorse is proof you care."
        ],
        "activities": [
            "Write an apology or self-reflection",
            "Play story-driven games to gain perspective",
            "Read self-help books",
            "Meditate on lessons learned",
            "Engage in constructive actions"
        ],
        "games": ["Life is Strange", "Firewatch", "What Remains of Edith Finch"],
        "books": ["The Road to Character by David Brooks", "The Gifts of Imperfection by Brené Brown", "Emotional Intelligence by Daniel Goleman"],
        "movies": ["Good Will Hunting", "Atonement", "The Pursuit of Happyness"]
    },
    "sadness": {
        "quotes": [
            "Tears are words the heart can't express.",
            "Sadness is part of the human journey.",
            "Feel sadness fully, then let it go.",
            "Sadness teaches empathy.",
            "Grieve, but do not linger.",
            "Sadness allows for growth.",
            "Even the darkest clouds have silver linings.",
            "Sadness is temporary; hope is eternal.",
            "Sadness is proof of love.",
            "Sadness opens the door to joy."
        ],
        "activities": [
            "Play emotional story-driven games",
            "Listen to comforting music",
            "Write in a journal",
            "Read uplifting books",
            "Watch tearjerker or inspiring movies"
        ],
        "games": ["What Remains of Edith Finch", "Life is Strange", "Firewatch"],
        "books": ["Man's Search for Meaning by Viktor Frankl", "The Art of Happiness by Dalai Lama", "Option B by Sheryl Sandberg"],
        "movies": ["Inside Out", "Bridge to Terabithia", "The Pursuit of Happyness"]
    },
    "surprise": {
        "quotes": [
            "Surprise is the spice of life.",
            "Expect the unexpected.",
            "Surprises keep life exciting.",
            "Embrace the unexpected with joy.",
            "Surprise opens new possibilities.",
            "Life is full of delightful surprises.",
            "Surprise ignites curiosity.",
            "Stay open to wonder.",
            "Surprise brings novelty and excitement.",
            "Surprise is a gift, cherish it."
        ],
        "activities": [
            "Try a new hobby or activity",
            "Play a mystery story-driven game",
            "Read an unexpected twist book",
            "Watch a surprise-filled movie",
            "Take a spontaneous adventure"
        ],
        "games": ["The Stanley Parable", "Outer Wilds", "Life is Strange"],
        "books": ["Gone Girl by Gillian Flynn", "The Girl on the Train by Paula Hawkins", "Big Little Lies by Liane Moriarty"],
        "movies": ["The Sixth Sense", "Knives Out", "Inception"]
    },
    "neutral": {
        "quotes": [
            "Neutrality allows clarity of thought.",
            "Stay balanced and observe.",
            "Neutrality fosters understanding.",
            "Calm minds see clearly.",
            "Neutrality is the path to wisdom.",
            "Balance is the key to peace.",
            "Neutrality opens the mind.",
            "Observe, then act.",
            "Equanimity is strength.",
            "Stay centered, stay wise."
        ],
        "activities": [
            "Do whatever you enjoy: relax, play games, watch movies, or read",
            "Take a walk or meditate",
            "Listen to your favorite music",
            "Try a hobby you love",
            "Explore a new skill"
        ],
        "games": ["Any story-driven game you enjoy"],
        "books": ["Any book you enjoy"],
        "movies": ["Any movie you enjoy"]
    }
}

def get_random_resource(emotion):
    """
    Returns a random quote, activity, game, book, and movie for a given emotion.
    """
    if emotion not in emotion_data:
        return {
            "quote": "Embrace your emotions.",
            "activity": "Do something you enjoy.",
            "game": None,
            "book": None,
            "movie": None
        }
    data = emotion_data[emotion]
    return {
        "quote": random.choice(data["quotes"]),
        "activity": random.choice(data["activities"]),
        "game": random.choice(data["games"]),
        "book": random.choice(data["books"]),
        "movie": random.choice(data["movies"])
    }