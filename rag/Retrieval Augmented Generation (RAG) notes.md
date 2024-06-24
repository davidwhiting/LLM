# Retrieval Augmented Generation (RAG)

## Resources

### Example RAG Tutorial

Do it yourself in ~20 lines of code with LlamaIndex.

You give it a directory containing documents and ask it to build an index and vector data embeddings over the documents

Then you can use this index with models like ChatGPT

Tutorial here shows the end to end process
[https://gpt-index.readthedocs.io/en/latest/getting_started/starter_example.html](https://gpt-index.readthedocs.io/en/latest/getting_started/starter_example.html)

### Online RAG Description

Most don't train/fine-tune on your data, they stick it into a vector database and perform similarity search. The method is called Retrieval Augmented Generation.
This is the high level algorithm:

1) Sentence segmentation/text splitting. The data is indexed in disparate chunks so the user can look up the specific information they want.

2) The split sentences/text chunks are ran through a cheap LLM/specialized model, usually not state of the art but powerful/big enough to separate and associate the individual concepts in the latent space. Current models being davinci-003 and SentenceTransformers. The embeddings generation is usually the first step in an NLP deep learning model, so it's relatively cheap/lightweight. Essentially you take the first layer or two of a neural network and multiply the weight matrix against the input. This is the simplest type of embedding (see the original word2vec) algorithm. Transformer embeddings are a bit different but functionally they operate similarly.

3) The generated embedding vectors represent the input data in latent space, i.e. abstract representations. The most famous sentence in modern nature language processing being possibly King - Man + Woman = Queen.

4) The vector embeddings are stored somewhere, usually a database, but you can dump them in an excel file too if you want. You want to put it in a dictionary structure, where individual embedding -> original sentence chunk.

5) The user creates a query which is passed to the embeddings generator model and another vector embedding is generated (the query can be anything, so long it's natural language based since that's what the embeddings generator LLM was trained on). This query can also be created by an upstream LLM too, the specifics do not matter so long the sentence is mostly well-formed.

6) We obtain an answer by performing a similarity search (nearest neighbor in the vector latent space, using cosine/Euclidean distance/whatever metric). There are many approaches to do this, you can use kNN, you can use basic linear algebra and do n comparisons against all other vectors, or you can use a graph data structure (the currently preferred method for the fastest libraries).

7) You find the closest vector and the text chunk/sentences it represents and you take these sentences and the original query (the raw natural language text, not the generated embedding) and feed everything into a new LLM prompt. The LLM in this step is usually a state of the art chat model like GPT-4 or Llama 2, not the cheap model used for indexing and generating vectors. You pass a prompt like this:

- Answer the following query: {original query text} with the given context: {text chunks, sentences}.

And that's it. Retrieval augmented generation has a fancy name and langchain's code feels opaque as hell like it was written by enterprise java people but the underlying algorithm is less than 30 lines of code with the standard ML and linear algebra libraries.

Reference: <https://news.ycombinator.com/item?id=36832572>

## LlamaIndex

## Vector Databases

### ChromaDB

### Qdrant

Investigate later. Here are some links:

- https://myscale.com/blog/qdrant-vs-chroma-vector-databases-comparison/
- https://qdrant.tech/pricing/
- https://qdrant.tech/documentation/quick-start/
- https://qdrant.tech/documentation/examples/
- https://qdrant.tech/documentation/tutorials/
- https://github.com/qdrant/qdrant#usage

## Possible Solutions (Software)

- localGPT can parse PDF into embeddings, see <https://github.com/PromtEngineer/localGPT>.
- Try privateGPT


 