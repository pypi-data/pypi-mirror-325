from setuptools import setup, find_packages

setup(
    name='evoagent',
    version='0.0.1',
    description='A Python package for AI-MultiModal MultiAgents methods and tools.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Bharath4ru/evoagent',
    author='Munakala Bharath',
    author_email='bharathmunakala22@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'groq',
        'wikipedia-api',
        'youtube_transcript_api',
        'PyPDF2',
        'faiss-cpu',
        'langchain_community',
        'requests',
        'beautifulsoup4',
        'pandas',
        'google-api-python-client',
        'sentence-transformers'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
