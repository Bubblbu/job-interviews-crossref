Crossref Interview Prep
> Position as Data Scientist

# Problem Statement

> We would like to explore citation trends. Which content types are being cited in the scholarly literature? How is that changing over time? Are there any correlations between the content type of the citing work and the content type of the cited work?

Presentation: [Google Slides](https://docs.google.com/presentation/d/1VXqkr1DvCtK-KipMKI4OMw0-hhemwsps9QdFaCKH0lE/edit?usp=sharing)

## Technical Choices

I chose this more pragmatic approach for a project as I was quite limited in the time I could commit to this task. However, this repository, therefore presents a good example of how I would typically tackle a new data science project in its early phase including exploratory work around broader questions. I am mostly relying on established tools that I am familiar with for data collection, processing, analysis, and results. The key components I do consider to be quite versatile as they can be scaled up as well as easily modularized into a more robust architecture.

## Install & run project

Clone the project

```bash
git clone git@github.com:Bubblbu/job-interviews-crossref.git
cd job-interviews-crossref
```

This analysis requires Python 3.11.6. I recommend using `pyenv` and `poetry` to manage Python version and dependencies.

```bash
pyenv install 3.11.6  # skip if already installed
pyenv local 3.11.6 # Activate the correct Python version
```

Using poetry you can now easily install project dependencies and make the tool available to the local environment as `ccc`

```bash
poetry install  # creates a new virtual environment, install requirements, and this project
poetry shell  # activates the environment
```