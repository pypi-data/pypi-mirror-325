from setuptools import setup, find_packages

setup(
    name='WebhookHandler',  # Replace with your package's name
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'requests',  # Example: requests
    ],
    entry_points={
        'console_scripts': [
            'webhook-sender = webhookhandler.cli:main',  # Optional: if you want to create a command line interface
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',  # Adjust to the license you're using
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
