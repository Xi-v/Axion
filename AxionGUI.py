import tkinter as tk
from tkinter import scrolledtext, messagebox

# Variables
opening_bracket = '('
closing_bracket = ')'
attributes = ['emit', 'synthesise', 'react', 'guide_to_the_galaxy']
comma = ','
react = 'react'
emit = 'emit'
synthesise = 'synthesise'
characters_to_remove = [')', '(']
synthesised_variables = {}
speech_marks = '"'

# Helper functions
def remove_specific_characters(input_string, characters_to_remove):
    for char in characters_to_remove:
        input_string = input_string.replace(char, "")
    return input_string

# Emit function
def emit_function(content):
    cleaned_content = remove_specific_characters(content, characters_to_remove)
    if cleaned_content in synthesised_variables:
        output_display.insert(tk.END, synthesised_variables[cleaned_content] + "\n")
    elif speech_marks in cleaned_content:
        output_display.insert(tk.END, f"There is no synthesised variable called {cleaned_content}\n")
    else:
        output_display.insert(tk.END, cleaned_content + "\n")

# Synthesise function
def synthesise_function(content, var_name):
    if var_name not in synthesised_variables:
        synthesised_variables[var_name] = content
        output_display.insert(tk.END, f"Synthesised Variable: {var_name} = {synthesised_variables[var_name]}\n")
    else:
        output_display.insert(tk.END, f"Variable '{var_name}' already exists with value: '{synthesised_variables[var_name]}'\n")

# React function
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

            if synthesise in before_react_comma:
                synthesise_in_react_parts = before_react_comma.split('(')
                if len(synthesise_in_react_parts) > 1:
                    after_synthesise_in_react_parts = synthesise_in_react_parts[1].strip().rstrip(closing_bracket)
                    if comma in after_synthesise_in_react_parts:
                        content, var_name = after_synthesise_in_react_parts.split(',')
                        content = content.strip()
                        var_name = var_name.strip().strip(speech_marks)
                        synthesise_function(content, var_name)
                        
            if emit in before_react_comma:
                emit_in_react_parts = before_react_comma.split('(')
                if len(emit_in_react_parts) > 1:
                    before_emit_react_bracket = emit_in_react_parts[1].strip().rstrip(closing_bracket)
                    emit_function(before_emit_react_bracket.strip(speech_marks))            

            if synthesise in after_react_comma:
                synthesise_in_react_parts = after_react_comma.split('(')
                if len(synthesise_in_react_parts) > 1:
                    after_synthesise_in_react_parts = synthesise_in_react_parts[1].strip().rstrip(closing_bracket)
                    if comma in after_synthesise_in_react_parts:
                        content, var_name = after_synthesise_in_react_parts.split(',')
                        content = content.strip()
                        var_name = var_name.strip().strip(speech_marks)
                        synthesise_function(content, var_name)            
                    
            if emit in after_react_comma:
                emit_in_react_parts = after_react_comma.split('(')
                if len(emit_in_react_parts) > 1:
                    after_emit_react_bracket = emit_in_react_parts[1].strip().rstrip(closing_bracket)
                    emit_function(after_emit_react_bracket.strip(speech_marks))

# Guide to the Galaxy                    
def guide_to_the_galaxy():
    guide_info = """
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
Usage - orbit around earth(5):
        emit(*What you want to print*)
Outcome:
What you want to print
What you want to print
What you want to print
What you want to print
What you want to print

When stating an orbit, you must say, "orbit around earth(*how many times to loop, leave empty for an infinite amount of times*):"

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
"""
    output_display.insert(tk.END, guide_info)

def run_code():
    user_input = input_field.get("1.0", tk.END).strip()
    input_field.delete("1.0", tk.END)

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
        else:
            output_display.insert(tk.END, f"Error: There is no attribute called {last_word}\n")
    else:
        output_display.insert(tk.END, "Error: Brackets are not properly formatted.\n")
        
window = tk.Tk()
window.title("Axion Code Interpreter")
window.geometry("800x600")
window.configure(bg="#2e2e2e")

logo_label = tk.Label(window, text="  Axion Coding Language  ", font=("Consolas", 20), bg="#2e2e2e", fg="#ffcc00")
logo_label.pack(pady=10)

input_field = scrolledtext.ScrolledText(window, height=5, font=("Consolas", 14), bg="#1e1e1e", fg="#ffffff")
input_field.pack(pady=10, padx=20, fill=tk.X)

run_button = tk.Button(window, text="Run Code", command=run_code, font=("Consolas", 14), bg="darkblue", fg="#ffffff")
run_button.pack(pady=10)

output_display = scrolledtext.ScrolledText(window, height=15, font=("Consolas", 14), bg="#1e1e1e", fg="#ffffff")
output_display.pack(pady=10, padx=20, fill=tk.BOTH)

window.mainloop()
