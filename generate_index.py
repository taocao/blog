import os

html_files = [f for f in os.listdir('html_output') if f.endswith('.html') and f != 'index.html']
print("HTML Files found:", html_files)  # Debug line to list the found HTML files

with open('site_template/index.html', 'r') as file:
    data = file.read()

new_data = data.replace(
    '<!-- Blog links will be inserted here by the script -->',
    '\n'.join([f'<li><a href="{f}">{f}</a></li>' for f in html_files])
)

print("Generated index content:", new_data)  # Debug line to show the generated index content

# Copy CSS file
os.system('cp site_template/style.css html_output/style.css')

with open('html_output/index.html', 'w') as file:
    file.write(new_data)
