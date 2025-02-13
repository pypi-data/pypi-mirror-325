from setuptools import setup, find_packages

setup(
    name='tolstoy_agents',                    
    version='0.1.50',                          # Incremented version number
    packages=find_packages(),                 
    install_requires=[                        
        'langgraph>=0.2.16',                  # Changed to >= to allow newer versions
        'langchain>=0.2.15',                  # Changed to >= to allow newer versions
        'langchain-openai>=0.1.23',           # Changed to >= to allow newer versions
        'langchain-core>=0.2.35'              # Changed to >= to allow newer versions
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
