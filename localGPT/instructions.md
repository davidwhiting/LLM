# Installing localGPT to work with Ollama

```
git clone git@github.com:PromtEngineer/localGPT.git
cd localGPT
conda create -n localGPT python=3.10
pip install -r requirements.txt
```

Perhaps I should use venv instead of conda here?

```
python ingest.py
```

We assume that ollama is already installed.

```
ollama run mistral
```
