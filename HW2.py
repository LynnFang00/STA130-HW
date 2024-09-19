#!/usr/bin/env python
# coding: utf-8

# 1. Begin (or restart) part "3(a)" of the TUT Demo and interact with a ChatBot to make sure you understand how each part the Monte Hall problem code above works

# This Monty Hall simulation models a game where the player picks one of three doors, aiming to win a car. After the player's choice, the host reveals a goat behind one of the other doors, and the player always switches to the remaining door.
# 
# The code simulates this process 100,000 times and tracks how often the player wins by switching. It shows that switching results in a win about 2/3 of the time, matching the known probability for the Monty Hall problem.

# In[ ]:





# 2. Extend your ChatBot sessions to now address part "3(b)" of the TUT Demo and interact with your ChatBot to see if it can suggest a simpler, more streamlined way to code up this for loop simulation so the process is more clear and easier to understand; then, describe any preferences you have in terms of readibility or explainability between the original code and the code improvements suggested by the ChatBot

# In[ ]:


import numpy as np

# Set parameters
all_doors = (1, 2, 3)  # The three doors
reps = 100000  # Number of repetitions
wins = 0  # Counter for wins

for _ in range(reps):
    # Randomly choose a winning door and the player's initial choice
    winning_door = np.random.choice(all_doors)
    player_choice = np.random.choice(all_doors)
    
    # Monty reveals a door (not the player's choice and not the winning door)
    available_doors = [door for door in all_doors if door != player_choice and door != winning_door]
    monty_reveal = np.random.choice(available_doors)
    
    # Player switches to the remaining unopened door
    remaining_door = [door for door in all_doors if door != player_choice and door != monty_reveal][0]
    
    # Check if the switch results in a win
    if remaining_door == winning_door:
        wins += 1

# Calculate win probability
win_probability = wins / reps
print(win_probability)


# Key Improvements:
# Simplified Logic:
# 
# Instead of removing doors and re-adding them, we create a list of available doors after the player's choice and Monty’s reveal.
# Monty Reveals Automatically:
# 
# Monty always reveals a door that is neither the player’s choice nor the winning door, which avoids extra checks.
# Switching:
# 
# The player switches to the remaining door in one line, making the code more readable.
# Summary of Process:
# Randomly assign a winning door and the player’s initial choice.
# Monty reveals a goat door that’s neither the player’s choice nor the winning door.
# The player switches to the remaining unopened door.
# If the remaining door is the winning door, the player wins.
# Repeat this process 100,000 times and compute the win probability.
# This version is shorter, easier to follow, and gives you the same result as the original code.

# Preference: I think the improved version of the Monty Hall code is easier to follow because it simplifies the logic, reduces unnecessary steps like removing and re-adding doors, and avoids confusing elements like the try block. It keeps the process clear and straightforward, making it easier to understand and read.

# In[ ]:





# 3. Submit your preferred version of the Monty Hall problem that is verified to be running and working with a final printed output of the code; then, add code comments explaining the purpose of each line of the code

# In[ ]:


import numpy as np

# Step 1: Setup the simulation
all_door_options = (1, 2, 3)  # Tuple representing the 3 doors
my_door_choice = 1  # You always start by choosing door 1
i_won = 0  # Variable to count how many times you win by switching
reps = 100000  # Number of times to repeat the simulation

# Step 2: Run the simulation in a loop
for i in range(reps):
    secret_winning_door = np.random.choice(all_door_options)  # Randomly pick the winning door
    
    # Step 3: Host reveals a goat door
    # Filter out the door that you initially chose and the winning door
    remaining_doors = [door for door in all_door_options if door != my_door_choice and door != secret_winning_door]
    
    # The host randomly reveals one of the goat doors
    goat_door_reveal = np.random.choice(remaining_doors)
    
    # Step 4: Switch to the other remaining door
    new_choice = [door for door in all_door_options if door != my_door_choice and door != goat_door_reveal][0]
    
    # Step 5: Check if the new choice is the winning door
    if new_choice == secret_winning_door:
        i_won += 1  # Increment the win count if you picked the winning door after switching

# Step 6: Calculate and print the win ratio
win_ratio = i_won / reps
print(win_ratio)


# Summary: In the previous conversation, I shared a Monty Hall simulation code written by Prof. Schwartz, and ChatGPT helped me understand it step by step. The code simulates the Monty Hall problem using a "switch" strategy to calculate the probability of winning by switching doors.
# 
# It then provided a simplified version of the for loop, which streamlined the logic by using list comprehensions and removing unnecessary parts like the try-except block. It followed that with the full, revised version of the code and detailed explanations for each part of the program, covering the setup, host revealing a goat door, switching doors, and calculating the win ratio.
# link:https://chatgpt.com/share/66ebb3d1-204c-800d-af0a-fc15a1e19312

# In[ ]:





# 4. Watch the embedded video tutorial on Markov chains in the next Jupyter cell below to understand their application and relevance for ChatBots; then, after watching the video, start a new ChatBot session by prompting that you have code that creates a "Markovian ChatBot"; show it the first version of the "Markovian ChatBot code" below; and interact with the ChatBot session to make sure you understand how the original first version of the "Markovian ChatBot code" works

# In[1]:


# Markov Chains and Text Generation
from IPython.display import YouTubeVideo
YouTubeVideo('56mGTszb_iM', width = 550)


# Summary: I shared a piece of code that implements part of a Markov chain for a chatbot.
# ChatGPT explained the code, detailing how it tracks word frequencies and the transitions between words to predict the next word in a sequence. The code builds a statistical model by storing word usage (word_used) and the words that follow each word (next_word).
# I then asked about the underlying logic, and it explained that the code models word sequences by tracking how frequently one word follows another. This allows the chatbot to predict or generate the next word based on past word transitions.
# link: https://chatgpt.com/share/66ebb487-dab0-800d-b8e4-ad84f408d212

# In[ ]:





# 5. Recreate (or resume) the previous ChatBot session from question "4" above, and now prompt the ChatBot session that you have a couple extensions of the code to show it, and then show it each of the extentions of the "Markovian ChatBot code" below in turn
# 
# 5.1. Without just supplying your ChatBot session with the answers, see if the ChatBot can figure out what the extensions in the code do; namely, making character specific Markov chains, and using bigrams (rather than just the previous word alone) dependency... prompt your ChatBot session with some hints if it's not seeming to "get it"
# 

# 5.2. Interact with your ChatBot session to have it explain details of the code wherever you need help understanding what the code is doing and how it works
# 
# 
# 5.3. Start yet another new ChatBot session and first show the ChatBot the original "Markovian ChatBot code" below, and then tell ChatBot that you have an extension but this time just directly provide it the more complicated final extension without ever providing the intermediate extension code to the ChatBot session and see if it's still able to understand everything extension does; namely, making character specific Markov chains, and using bigrams (rather than just the previous word alone) dependency... prompt the ChatBot with some hints if it's not seeming to understand what you're getting at...

# Summary: Explanation of Code:
# 
# The original code builds a word-based Markov Chain that tracks word frequencies and how often a word follows another word.
# The extension creates a more advanced model by tracking bigrams (pairs of consecutive words) and the words that follow those bigrams.
# Logic of Code:
# 
# The logic is order-based, focusing on the sequence of words (or word pairs) and not on individual characters.
# Character-Specific Markov Chains:
# 
# The code is not making character-specific Markov chains. It is modeling word sequences (bigrams) rather than sequences of individual characters.
# In conclusion, the code is building a word-based Markov Chain model, with no focus on individual characters or character sequences.
# 
# link: https://chatgpt.com/share/66ebb148-c8cc-800d-9dc4-c585e28053bd

# In[ ]:





# 6. Report on your experience interacting with ChatBots to understand the Monte Hall problem and "Markovian ChatBot" code
# 6.1 Discuss how quickly the ChatBot was able to be helpful for each of the above questions, and if so, how?
# 
# 
# 6.2 Discuss whether or not interacting with ChatBot to try to figure things out was frustrating or unhelpful, and if so, how?
# 
# 
# 6.3 Based on your experiences to date (e.g., including using ChatBots to troubleshoot coding errors in the previous homework), provide an overall assessment evaluating the usefulness of ChatBots as tools to help you understand code

# 6.1 It is very helpful using ChatGpt to make me understand the Monte Hall problem and "Markovian ChatBot" code I learnt that it is an extension of a Markovian chatbot that models conversational patterns based on characters in a dataset (avatar). The dataset has a column character, and the goal is to build two nested dictionaries, word_used2C and next_word2C, which track word sequences spoken by specific characters, potentially for generating predictive text based on their past word usage. It can give me instant reply with respect to the specific questions I ask.

# 6.2  Interacting with Chatgpt is really pleasing ad helpful, for it give me a full picture and summary of the new thing I'm learning and can always gives me solutions to the questions I ask. It can be modified by personal choices in terms of the level of understanding that benefits everyone.

# 6.3 ChatBots are helpful for quickly troubleshooting code errors and explaining concepts. They offer useful guidance on syntax and provide code suggestions, making them great for fixing simple issues or clarifying things on the go. However, they can miss the mark with more complex problems and lack the personalized feedback that a human tutor provides. While they're convenient, it's important not to rely too much on them—they're best used as a support tool alongside other learning methods.

# In[ ]:





# 7. Reflect on your experience interacting with ChatBot and describe how your perception of AI-driven assistance tools in the context of learning coding, statistics, and data science has been evolving (or not) since joining the course

# Since joining the course, my perception of AI-driven tools like ChatBots has evolved. Initially, I saw them as simple assistants for quick fixes and explanations, but I’ve come to appreciate their broader utility in learning coding, statistics, and data science. They help break down complex topics, offer personalized guidance, and make learning more accessible outside traditional classroom settings. While they’re not perfect and can miss nuances in difficult problems, they’ve proven valuable for immediate support and reinforcing concepts. Over time, I’ve realized how useful they are for boosting productivity and deepening understanding when used wisely.

# In[ ]:





# 8. ChatBots consume text data available on the web or platforms, and thus represents a new way to "search consensensus" that condenses and summarizes mainstream human thought
# 
# 8.1 Start a new ChatBot session and discuss the relevance of learning and adaptability, communication, coding, and statistics and data analysis as skills in the modern world, especially with respect to career opportunities (particularly in the context of the data science industry)
# 
# 
# 8.2 See if ChatBot thinks you could be a statistician or data scientist without coding or doing data analysis, and then transition your ChatBot conversation into a career exploration discussion, using the ChatBot to identify the skills that might be the most valuable for a career that you're interested
# 
# 
# 8.3 Ask for a summary of this ChatBot session and paste it into your homework notebook (including link(s) to chat log histories if you're using ChatBot)
# 
# 
# 8.4 Paraphrase the assessments and conclusions of your conversation in the form of a reflection on your current thoughts regarding your potential future career(s) and how you can go about building the skills you need to pursue it
# 
# 
# 8.5 Give your thoughts regarding the helpfulness or limitations of your conversation with a ChatBot, and describe the next steps you would take to pursue this conversation further if you felt the information the ChatBot provides was somewhat high level and general, and perhaps lacked the depth and detailed knowledge of a dedicated subject matter expert who had really take the time to understand the ins and outs of the industry and career path in question.

# summary: In the previous conversation, you asked about the most valuable skills for computer engineers and project managers. I outlined key skills for each:
# 
# For Computer Engineers, important skills include:
# 
# Proficiency in programming languages (e.g., C++, Python), embedded systems, hardware design, and networking.
# Strong problem-solving and analytical thinking, along with adaptability to evolving technologies.
# Collaboration and communication skills for working with cross-functional teams.
# For Project Managers, critical skills include:
# 
# Leadership, team management, and proficiency in project planning and scheduling tools (e.g., Microsoft Project, Asana).
# Risk management, budget management, and effective communication with stakeholders.
# Knowledge of project management methodologies like Agile and Scrum, and strong problem-solving and time management skills.
# Both roles share the need for problem-solving, communication, and adaptability to succeed in their respective fields.
# 
# link: https://chatgpt.com/share/66ebb185-ea78-800d-95a7-c1d113bc932f

# 8.4 Reflecting on my current thoughts about potential future careers, I realize that I am still exploring various paths, but I’m drawn to roles that combine my technical knowledge with my enthusiasm for teamwork and problem-solving. My studies in computer science offer a strong foundation in logical thinking and technical skills, but I also recognize the importance of developing soft skills, especially in communication, organization, and leadership.
# 
# To build the skills I need, I’m taking steps such as getting involved in student organizations like IEEE, where I can gain experience in logistics and external relations. These roles will help me hone my ability to manage projects, work with diverse teams, and navigate challenges effectively. I believe that by consistently seeking out new experiences, whether through academic courses, extracurricular activities, or internships, I’ll be able to refine both my technical and interpersonal abilities, which are essential for any career I might choose to pursue.

# 8.5 The ChatBot has been helpful for organizing my thoughts and providing general advice, but it's missing the depth and specifics I’d get from an industry expert. If I wanted more detailed guidance, I'd reach out to professionals, attend industry-focused events, and look for specialized resources or forums to get practical, insider advice. This would give me a more grounded understanding of the steps needed for my career.

# In[ ]:





# 9. Have you reviewed the course wiki-textbook and interacted with a ChatBot (or, if that wasn't sufficient, real people in the course piazza discussion board or TA office hours) to help you understand all the material in the tutorial and lecture that you didn't quite follow when you first saw it?
# 
# 
# Yes!!!!!!!!!!
