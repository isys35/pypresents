TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        ...
        'OPTIONS': {
            'context_processors': [
                ...
								"bboard.middlewares.rubrics"
            ],
        },
    },
]