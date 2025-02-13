from setuptools import setup, find_packages

setup(
    name='tolstoy_agents',                    
    version='0.1.51',                          # Increment version
    packages=find_packages(),                 
    install_requires=[                        
        'langgraph>=0.2.16,<0.3.0',           # Added upper bound
        'langchain>=0.2.15,<0.4.0',           # Added upper bound
        'langchain-openai>=0.1.23,<0.4.0',    # Added upper bound
        'langchain-core>=0.2.35,<0.4.0',      # Added upper bound
        'langchain-community>=0.2.16,<0.3.0'  # Added community package
    ],
    author='Tolstoy',                       
    author_email='tolstoy@gotolstoy.com',    
    description='Framework to create LLM agents',
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown', 
    classifiers=[                             
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',                  
)
