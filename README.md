# Crossref Interview Prep
> Position as Data Scientist

## Problem Statement

> We would like to explore citation trends. Which content types are being cited in the scholarly literature? How is that changing over time? Are there any correlations between the content type of the citing work and the content type of the cited work?

Presentation: [Google Slides](https://docs.google.com/presentation/d/1VXqkr1DvCtK-KipMKI4OMw0-hhemwsps9QdFaCKH0lE/edit?usp=sharing)

## Technical Choices

I chose this more pragmatic approach for a project as I was quite limited in the time I could commit to this task. However, this repository, therefore presents a good example of how I would typically tackle a new data science project in its early phase including exploratory work around broader questions. I am mostly relying on established tools that I am familiar with for data collection, processing, analysis, and results. The key components I do consider to be quite versatile as they can be scaled up as well as easily modularized into a more robust architecture.

### Processing Pipeline

1. **Sampling**

`notebooks/0_get_sample.ipynb`

I chose not to use any advanced sampling methods as I wanted to focus on the processing and analysis that I could achieve on my local machine. I retrieved 10,000 random articles from the Crossref API without any filters.

2. **Preprocessing & enrichment**

`notebooks/1_preprocess_data`

As I wanted to focus my analysis on the two key aspects of content types and time, I only applied some minor processing to these two fields. The year was extracted from the published date as I was not planning to use a smaller time resolution in the analysis. Furthermore, I retrieved a current snapshot of the content type counts from the Crossref API and made sure to match the fields to the ones used in the data.

`notebooks/2_get_ref_types.ipynb`

The analysis also required a further data enrichment step as the content type is not included in the fields that are provided by the API in the list of references for articles. Therefore, I also queried the content type for the referenced DOIs found in the reference lists of the 10,000 articles.

1. **Analysis**

`notebooks/3_analysis.ipynb`

The analysis is fairly simple and I've opted to derive higher-level insights and focussed on visual analysis and context as we are working with a very small sample size which does not bode well for any statistics. Please refer to the analysis notebook and presentation slides for more details. 

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