# Overview: All about LLMs

- Updated comparison of popular LLMs [https://chat.lmsys.org/?leaderboard](https://chat.lmsys.org/?leaderboard)



# 1. Vector Databases



# 2. LLM Notes

## Overall

- Look here for Ollama vs. LM Studio [https://www.gpu-mart.com/blog/ollama-vs-lm-studio](https://www.gpu-mart.com/blog/ollama-vs-lm-studio)

## MindsDB

Run this command to create a Docker container with MindsDB:

```
docker run --name mindsdb_container -d -p 47334:47334 -p 47335:47335 mindsdb/mindsdb
```

To persist your models and configurations in the host machine, run

```
mkdir mdb_data
docker run --name mindsdb_container -p 47334:47334 -p 47335:47335 -v mdb_data:/root/mdb_storage mindsdb/mindsdb
```

Now you can access the MindsDB editor by going to `127.0.0.1:47334` in your browser.

## Ollama

Get the readme file [https://github.com/ollama/ollama?tab=readme-ov-file](https://github.com/ollama/ollama?tab=readme-ov-file)

To run with `ollama`:

### Llama3

```
ollama run llama3
```

### Mistral
```
ollama run mistral
```

### Code Llama
```
ollama run codellama
```



## Meta Llama Installation Guide

You’re all set to start building with Meta Llama

The models listed below are now available to you as a commercial license holder. By downloading a model, you are agreeing to the terms and conditions of the License, Acceptable Use Policy and Meta’s privacy policy.

### HOW TO DOWNLOAD THE MODEL

Based on the model you requested, please visit the respective Github repository to run the download.sh script - Llama 3, Llama 2, Code Llama, or Llama Guard. Follow the instructions in the README to run the download.sh scripts. When the script asks for your unique custom URL, please copy and paste one of the following URLs. (Clicking on the URL itself does not access the model):

### Meta Llama 3:
- Meta Llama 3 repository [https://github.com/meta-llama/llama3](https://github.com/meta-llama/llama3)
- [README.md](https://github.com/meta-llama/llama3/blob/main/README.md)
- download.sh
- URL

```
https://download6.llamameta.net/*?Policy=eyJTdGF0ZW1lbnQiOlt7InVuaXF1ZV9oYXNoIjoiMGwxeHBhZW1pYjN4eHJrMmM4eXNreHRrIiwiUmVzb3VyY2UiOiJodHRwczpcL1wvZG93bmxvYWQ2LmxsYW1hbWV0YS5uZXRcLyoiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3MTcyMTYwOTl9fX1dfQ__&Signature=I1ovm4fz0p78NdnI37IM4d8pNvqx3royXFL-Npt9DghI7ak7Y%7EFp1V6lVSmODz9ZUr7zGlfKDPPh%7EcaE8bluBMlhzURQf0mUaCDVXRBqWbm9j-Q%7EE%7Eza2koq7TALlikWvPRjcpJeVhYGUT3Fb4lS9Ia9WgUhQryaM0YYWce05Vpiu66y2LhDiFnZhJGy8xNEWT3mKIcGlTbb19VZeWTzlVxrS7Is9AERM5i-%7EzBXsTbgv1y-SNRjV2pehF1ZkSb1120cl3l1Me2Vg19fk%7EptTkRcUvljBe6j3dzu7bSNrYjBteoqsqPeA5qqY3to4Sxb1Uo-yYCKaF4ILFrFIK-7Xw__&Key-Pair-Id=K15QRJLYKIFSLZ&Download-Request-ID=1160122735299435
```

### Llama Recipes:
- Llama Recipes for Llama3 [https://github.com/meta-llama/llama-recipes](https://github.com/meta-llama/llama-recipes)

### Code Llama:
- Code Llama repository: [https://github.com/meta-llama/codellama](https://github.com/meta-llama/codellama)


### Llama Trust & Safety
- Trust & Safety: [https://llama.meta.com/trust-and-safety/](https://llama.meta.com/trust-and-safety/)