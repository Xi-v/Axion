# Variables
opening_bracket = '('
closing_bracket = ')'
attributes = ['emit', 'synthesise', 'react', 'orbit']
comma = ','
react = 'react'
emit = 'emit'
synthesise = 'synthesise'
characters_to_remove = [')', '(']

# Start Up
print("Welcome to:")
print("  _ _ _     _ _   _ _    _ _  _ _    _ _ _ _    _    _\n /  _  \   \   \ /   /  |__    __|  /  _ _  \  | \  | |\n|  |_|  |   \   v   /      |  |    |  |   |  | |  \ | |\n|   _   |    x     x       |  |    |  |   |  | |   \| |\n|  | |  |   /   ^   \    __|  |__  |  |_ _|  | | |\   |\n|__| |__|  /_ _/ \_ _\  |_ _  _ _|  \_ _ _ _/  |_| \__|\n")
print("Please see the txt file to see the attributes list")
user_input = input("Enter your code here:\n")

start_index = user_input.find(opening_bracket)
end_index = user_input.find(closing_bracket, start_index + 1)

def remove_specific_characters(input_string, characters_to_remove):
    for char in characters_to_remove:
        input_string = input_string.replace(char, "")
    return input_string


# emit function
def emit_function():
    emited_content = user_input[start_index + 1:end_index]
    print(emited_content)
    
# synthesise function
def synthesise_function():
    synthesised_data = user_input[start_index + 1:end_index]
    if comma in synthesised_data:
        synthesised_parts = synthesised_data.split(',')
        if len(synthesised_parts) > 1:
            before_synthesise_comma = synthesised_parts[0].strip()
            after_synthesise_comma = synthesised_parts[1].strip()

            if after_synthesise_comma not in globals():
                globals()[after_synthesise_comma] = before_synthesise_comma
                print(f"Synthesised Variable: {after_synthesise_comma} = {globals()[after_synthesise_comma]}")
            else:
                print(f"Variable '{after_synthesise_comma}' already exists with value: '{globals()[after_synthesise_comma]}'")
    else:
        print("There's no content after the comma.")
    


# react function
def react_function():

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
            if opening_bracket and closing_bracket in before_react_comma:
                if emit in before_react_comma:
                    emit_in_react_parts = before_react_comma.split('(')
                    if len(emit_in_react_parts) > 1:
                        before_emit_react_bracket = emit_in_react_parts[0].strip()
                        after_emit_react_bracket = emit_in_react_parts[1].strip()
                        if closing_bracket in after_emit_react_bracket:
                            cleaned_emit_in_react = remove_specific_characters(after_emit_react_bracket, characters_to_remove)
                            print(cleaned_emit_in_react)
                            
                        else:
                            print("Error: There is no closing bracket for 'emit'") 
                
                if synthesise in before_react_comma:
                    synthesise_in_react_parts = before_react_comma.split('(')
                    if len(synthesise_in_react_parts) > 1:
                        after_synthesise_in_react_parts = synthesise_in_react_parts[1].strip()
                    
                        if comma in after_synthesise_in_react_parts:
                            cleaned_synthesise_in_react = remove_specific_characters(after_synthesise_in_react_parts, characters_to_remove)
                        
                            cleaned_parts = cleaned_synthesise_in_react.split(',')
                            if len(cleaned_parts) > 1:
                                before_synthesise_in_react_cleaned_parts = cleaned_parts[0].strip()
                                after_synthesise_in_react_cleaned_parts = cleaned_parts[1].strip()
                                if after_synthesise_in_react_cleaned_parts not in globals():
                                    globals()[after_synthesise_in_react_cleaned_parts] = before_synthesise_in_react_cleaned_parts
                                    print(f"Synthesised Variable: {after_synthesise_in_react_cleaned_parts} = {globals()[after_synthesise_in_react_cleaned_parts]}")
                                else:
                                    print(f"Variable '{after_synthesise_in_react_cleaned_parts}' already exists with value: '{globals()[after_synthesise_in_react_cleaned_parts]}'")
                                
                        
                       
        else:
            print(f"No valid comma found in react parameters.")
    else:
        print(f"Error: '{react}' not found or brackets not properly formatted.")

# Function to check code
def check_code():

    if start_index != -1 and end_index != -1:
        first_word = user_input[:start_index].strip()
        last_word = first_word.split()[-1] if first_word else ""

        if last_word in attributes:
            # emit attribute
            if last_word == "emit":
                emit_function()
            
            #synthesise attribute    
            elif last_word == "synthesise":
                synthesise_function()
            
            # react attribute        
            elif last_word == "react":
                react_function()
            
        else:
            print(f"Error: There is no attribute called {last_word}")
    else:
        print("Error: Brackets are not properly formatted.")

check_code()
