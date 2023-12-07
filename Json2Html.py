import json
from json2html import json2html

# Function to print color-formatted messages
def print_colored(message, color="white"):
    print("\033[1;{}m{}\033[0m".format(color, message))

# Function for blinking input prompt
def blink_input_prompt(prompt, color="red"):
    while True:
        print_colored(prompt, color)
        user_input = input()
        if user_input:
            return user_input

# Blinking red input prompt for JSON file name
json_file_name = blink_input_prompt("Enter the JSON file name: ", "31")  # "31" corresponds to red

# Load JSON data from the user-provided file
try:
    with open(json_file_name, 'r') as file:
        json_data = json.load(file)
except FileNotFoundError:
    print_colored(f"Error: The file '{json_file_name}' does not exist.", "red")
    exit()

# Blinking blue input prompt for HTML file name
html_file_name = blink_input_prompt("Enter the HTML file name: ", "34")  # "34" corresponds to blue

# Save the HTML to a file
with open(html_file_name, 'w') as html_file:
    html_file.write(json2html.convert(json=json_data))

print_colored(f"Conversion completed. HTML file saved as '{html_file_name}'", "32")  # "32" corresponds to green
