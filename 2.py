departments = {'general_office':            #1
    {
    'gen_principal' :
        {
            'name':'Elena',
            'age':50,
            'salary':1200
        },
    'assistant':
        {
            'name':'Alex',
            'age':20,
            'salary':1000
        },
    'clerk':
        {
            'name':'Ethan',
            'age':30,
            'salary':1400
        }
    },'staff managment':                    #2
    {
    'superior':
        {
            'name':'Jeff',
            'age':54,
            'salary':1100
        },
    'staff':
        [
            {'name': 'Mark',
            'age': 45,
            'salary': 700},

            {'name':'Jane',
            'age': 26,
            'salary': 700},

            {'name':'Henry',
            'age': 30,
            'salary': 700}

        ]

    }, 'development department':                #3
    {
        'superior':
            {
                'name': 'Franchesco',
                'age': 54,
                'salary': 1100
            },
        'staff':
            [
                {'name': 'Nick',
                 'age': 26,
                 'salary': 900},

                {'name': 'Leo',
                 'age': 25,
                 'salary': 900},

                {'name': 'Patrik',
                 'age': 3,
                 'salary': 900},

                {'name': 'Mickey',
                 'age': 21,
                 'salary': 900},

                {'name': 'Marissa',
                 'age': 19,
                 'salary': 900},

                {'name': 'Helen',
                 'age': 46,
                 'salary': 700}

            ]

    }, 'management division':               #4
    {
        'superior':
            {
                'name': 'Fiona',
                'age': 24,
                'salary': 1700
            },
        'staff':
            [
                {'name': 'Gabriella',
                 'age': 21,
                 'salary': 500},

                {'name': 'Ien',
                 'age': 48,
                 'salary': 600},

                {'name': 'Martin',
                 'age': 36,
                 'salary': 500},

                {'name': 'Arthur',
                 'age': 34,
                 'salary': 500},

                {'name': 'Melissa',
                 'age': 20,
                 'salary': 500},

            ]

    }, 'testing department':                #5
    {
        'superior':
            {
                'name': 'Rosie',
                'age': 40,
                'salary': 1400
            },
        'staff':
            [

                {'name': 'Alex',
                 'age': 31,
                 'salary': 900},

                {'name': 'Debbie',
                 'age': 24,
                 'salary': 900},

                {'name': 'Frank',
                 'age': 19,
                 'salary': 900},

                {'name': 'Margo',
                 'age': 41,
                 'salary': 700}

            ]

    }, 'sales department':          #6
    {
        'superior':
            {
                'name': 'Kortny',
                'age': 36,
                'salary': 1200
            },
        'staff':
            [
                {'name': 'Nickolas',
                 'age': 29,
                 'salary': 800},

                {'name': 'Wayne',
                 'age': 24,
                 'salary': 800},

                {'name': 'Karoline',
                 'age': 48,
                 'salary': 800},

                {'name': 'Steve',
                 'age': 18,
                 'salary': 800},

                {'name': 'Maggy',
                 'age': 31,
                 'salary': 800},

            ]

    }
}
departments['protection division'] = {
    'superior':
        {
            'name':'Pou',
            'age':34,
            'salary':1300
        },
    'staff':
        [
            {'name': 'Josh',
            'age': 60,
            'salary': 700},

            {'name':'Janett',
            'age': 19,
            'salary': 700},

            {'name':'Kortney',
            'age': 38,
            'salary': 700}

        ]

    }
del departments['testing department']
if 'testing department' in departments:
    print(1)
else:
    print(0)

departments['development department']['staff'].append({ 'name': 'Boris',
                                                        'age': 27,
                                                        'salary': 600})
print(departments)
