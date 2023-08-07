from jinja2 import Environment, FileSystemLoader
from graphing import total_time

# Create an environment with the loader pointing to the directory of your HTML template file
env = Environment(loader=FileSystemLoader('./'))

def modify_html():
    # Load the HTML template
    template = env.get_template('fitness-tracker/pre_index.html')

    # Define variables to be passed to the template
    time = total_time

    # Render the template with the variables
    output = template.render(total_t=time)

    # Write the rendered template to a new file
    with open('fitness-tracker/index.html', 'w') as file:
        file.write(output)

    
    template = env.get_template('fitness-tracker/pre_page1.html')

    # Define variables to be passed to the template
    time = total_time

    # Render the template with the variables
    output = template.render(nothing=time)

    # Write the rendered template to a new file
    with open('fitness-tracker/page1.html', 'w') as file:
        file.write(output)
    
    template = env.get_template('fitness-tracker/pre_page2.html')

    # Define variables to be passed to the template
    time = total_time

    # Render the template with the variables
    output = template.render(nothing=time)

    # Write the rendered template to a new file
    with open('fitness-tracker/page2.html', 'w') as file:
        file.write(output)



if __name__ == '__main__':
    modify_html()
