# Absolutely sick logo
print("Welcome to:")
print("  _ _ _     _ _   _ _    _ _  _ _    _ _ _ _    _    _")
print(" /  _  \   \   \ /   /  |__    __|  /  _ _  \  | \  | |")
print("|  |_|  |   \   v   /      |  |    |  |   |  | |  \ | |")
print("|   _   |    x     x       |  |    |  |   |  | |   \| |")
print("|  | |  |   /   ^   \    __|  |__  |  |_ _|  | | |\   |")
print("|__| |__|  /_ _/ \_ _\  |_ _  _ _|  \_ _ _ _/  |_| \__|")
print("This is only the text based version of Axion, please view the other files to see the GUI based version of Axion.")
print("Use the line of code 'guide_to_the_galaxy()' to access all of the current attributes and their properties")

# Variables
opening_bracket = '('
closing_bracket = ')'
attributes = ['emit', 'synthesise', 'react', 'guide_to_the_galaxy', 'orbit']
comma = ','
react = 'react'
emit = 'emit'
synthesise = 'synthesise'
orbit = 'orbit'
characters_to_remove = [')', '(']
synthesised_variables = {}
speech_marks = '"'
near_infinite = 10**1000

# Helper functions
def remove_specific_characters(input_string, characters_to_remove):
    for char in characters_to_remove:
        input_string = input_string.replace(char, "")
    return input_string

# Emit function
def emit_function(content):
    cleaned_content = remove_specific_characters(content, characters_to_remove)
    if cleaned_content in synthesised_variables:
        print(synthesised_variables[cleaned_content])
    elif speech_marks in cleaned_content:
        if cleaned_content not in synthesised_variables:
            print(f"There is no synthesised variable called {cleaned_content}")
    else:
        print(cleaned_content)

# Synthesise Function
def synthesise_function(content, var_name):
    if var_name not in synthesised_variables:
        synthesised_variables[var_name] = content
        print(f"Synthesised Variable: {var_name} = {synthesised_variables[var_name]}")
    else:
        print(f"Variable '{var_name}' already exists with value: '{synthesised_variables[var_name]}'")

# React Function
def react_function(user_input):
    start_index = user_input.find(react + opening_bracket)
    end_index = user_input.rfind(closing_bracket)

    if start_index != -1 and end_index != -1:
        react_information = user_input[start_index + len(react) + 1:end_index]

        current_depth = 0
        split_index = -1
        for i, char in enumerate(react_information):
            if char == opening_bracket:
                current_depth += 1
            elif char == closing_bracket:
                current_depth -= 1
            elif char == comma and current_depth == 0:
                split_index = i
                break

        if split_index != -1:
            before_react_comma = react_information[:split_index].strip()
            after_react_comma = react_information[split_index + 1:].strip()

            # Synthesize before comma part
            if synthesise in before_react_comma:
                synthesise_in_react_parts = before_react_comma.split('(')
                if len(synthesise_in_react_parts) > 1:
                    after_synthesise_in_react_parts = synthesise_in_react_parts[1].strip().rstrip(closing_bracket)
                    if comma in after_synthesise_in_react_parts:
                        content, var_name = after_synthesise_in_react_parts.split(',')
                        content = content.strip()
                        var_name = var_name.strip().strip(speech_marks)
                        synthesise_function(content, var_name)
                        
            # Emit before comma part
            if emit in before_react_comma:
                emit_in_react_parts = before_react_comma.split('(')
                if len(emit_in_react_parts) > 1:
                    before_emit_react_bracket = emit_in_react_parts[1].strip().rstrip(closing_bracket)
                    emit_function(before_emit_react_bracket.strip(speech_marks))            

                        
            # Synthesize after comma part
            if synthesise in after_react_comma:
                synthesise_in_react_parts = after_react_comma.split('(')
                if len(synthesise_in_react_parts) > 1:
                    after_synthesise_in_react_parts = synthesise_in_react_parts[1].strip().rstrip(closing_bracket)
                    if comma in after_synthesise_in_react_parts:
                        content, var_name = after_synthesise_in_react_parts.split(',')
                        content = content.strip()
                        var_name = var_name.strip().strip(speech_marks)
                        synthesise_function(content, var_name)            
            
                        
            # Emit after comma part
            if emit in after_react_comma:
                emit_in_react_parts = after_react_comma.split('(')
                if len(emit_in_react_parts) > 1:
                    after_emit_react_bracket = emit_in_react_parts[1].strip().rstrip(closing_bracket)
                    emit_function(after_emit_react_bracket.strip(speech_marks))
                    
# Guide function
def guide_to_the_galaxy():
    print("""
Axion Script:

Emit: print() 
Usage - emit(what you want to print) 
To declare a synthesised variable, put speech marks and then the name of that variable for emit to print it.

Synthesise: Create a variable 
Usage - synthesise(What will be in the variable, "What the variable name is")
When synthesising the variable, you must put "" when declaring the name.

React: React can be used to do several things with one command.
Usage - react(emit(*first variable*, *second variable*))
Another Usage - react(synthesise(*Inside the variable*, *Variable name*), emit(*Name of the variable created*))
React at the moment only has two possible uses, more will come 

Orbit: Loop 
Usage - orbit(what type of attribute you want to orbit, number of times to orbit it.)
e.g: orbit(emit(Hello), 5)) 

Priorities:
Axion uses a priority list. If you were to do the line of code:

react(emit("variable"), synthesise(Variable inside, "variable"))

Because synthesise is higher in the priority list, the synthesised variable would be created, and therefore emit would have a variable to print.
In the react function. the higheracy would look something like this:
 - First Synthesise Function
 - First Emit Function
 - Second Synthesise Function
 - Second Emit Function
This is due to how the code is set out.

Characters:
Axion heavily requires you to use '()' and ',' and ':', almost like python, which it is made out of.
""")

# Orbit function
def orbit(user_input, start_index, end_index):
    start_orbit = user_input.find("(") + 1
    end_orbit = user_input.find(")")

    if start_orbit > 0 and end_orbit > 0 and end_orbit > start_orbit:
        orbit_content = user_input[start_orbit:end_orbit].strip()  
        if comma in orbit_content: 
            orbit_split = orbit_content.split(',')
            if len(orbit_split) == 2:
                message = orbit_split[0].strip().strip(speech_marks)  
                repetitions = orbit_split[1].strip()

                if repetitions == "infinity":
                    while True: 
                        print(message)
                        
                elif repetitions.isdigit(): 
                    loop_count = int(repetitions)
                    for _ in range(loop_count): 
                        print(message)
                        
                else:
                    print("Error: Invalid number of repetitions.")
            else:
                print("Error: Incorrect number of arguments provided for orbit.")
        else:
            print("Error: Missing comma in orbit function arguments.")
            
# Main processing function
def axion():
    while True:
        user_input = input("Enter your code here:\n")
        start_index = user_input.find(opening_bracket)
        end_index = user_input.find(closing_bracket, start_index + 1)

        if start_index != -1 and end_index != -1:
            first_word = user_input[:start_index].strip()
            last_word = first_word.split()[-1] if first_word else ""

            if last_word in attributes:
                if last_word == "emit":
                    emit_function(user_input[start_index + 1:end_index])
                    
                elif last_word == "synthesise":
                    parts = user_input[start_index + 1:end_index].split(',')
                    if len(parts) == 2:
                        content, var_name = parts[0].strip(), parts[1].strip().strip(speech_marks)
                        synthesise_function(content, var_name)
                        
                elif last_word == "react":
                    react_function(user_input)
                
                elif last_word == "guide_to_the_galaxy":
                    guide_to_the_galaxy()  
                    
                elif last_word == "orbit":
                    orbit(user_input, start_index, end_index)  
                                    
            else:
                print(f"Error: There is no attribute called {last_word}")

        else:
            print("Error: Brackets are not properly formatted.")
        
        y_n = input("Would you like to run another line of code [y/n]:\n")
        if y_n.lower() != "y":
            print("Exiting Axion.")
            break

# Start the script
axion()
