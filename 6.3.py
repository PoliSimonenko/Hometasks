import json

evidence = {
    '45368465':
        ('Boris', '29'),
    '59624817':
        ('Helga', '25'),
    '26435124':
        ('Valentin', '36'),
    '18689542':
        ('Lora', '18'),
    '52364625':
        ('Toby', '45')
}

with open('evidence.json', 'w') as file:
    json.dump(evidence, file, indent=4)