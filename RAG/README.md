# Building a RAG

## Libraries

### Langchain

### LlamaIndex

## Recipes:

- Ollama + Llama 3 + LlamaIndex + ChromaDB + snowflake-arctic-embed 

- pgvector instead?

## Vector Database Options

### Chromadb

### 


## Embeddings Options

- snowflake-arctic-embed


## Option 1: PrivateGPT

## Components: Vector Database

### Qdrant

- See qdrant-client https://github.com/qdrant/qdrant-client

Install the client:

```
pip install qdrant-client
```

#### Local mode (w/o using server)

```
from qdrant_client import QdrantClient

client = QdrantClient(":memory:")
# or
client = QdrantClient(path="path/to/db")  # Persists changes to disk
```

- Can be used for prototyping or testing
- Can run in Jupyter Notebook

#### Fast Embeddings + Simpler API

```
#pip install qdrant-client[fastembed]
pip install fastembed
```

Qdrant Client can use FastEmbed to create embeddings and upload them to Qdrant. This allows to simplify API and make it more intuitive.

```
from qdrant_client import QdrantClient

# Initialize the client
client = QdrantClient(":memory:")  # or QdrantClient(path="path/to/db")

# Prepare your documents, metadata, and IDs
docs = ["Qdrant has Langchain integrations", "Qdrant also has Llama Index integrations"]
metadata = [
    {"source": "Langchain-docs"},
    {"source": "Linkedin-docs"},
]
ids = [42, 2]

# Use the new add method
client.add(
    collection_name="demo_collection",
    documents=docs,
    metadata=metadata,
    ids=ids
)

search_result = client.query(
    collection_name="demo_collection",
    query_text="This is a query document"
)
print(search_result)
```

### Connect to Qdrant server

To connect to Qdrant server, simply specify host and port:

```
from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", port=6333)
# or
client = QdrantClient(url="http://localhost:6333")
```

Run a local Qdrant server with docker:

```
docker run -p 6333:6333 qdrant/qdrant:latest
```

### Connect to Qdrant cloud

Register to use Qdrant Cloud and get a free tier account with 1GB RAM:

```
from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    url="https://xxxxxx-xxxxx-xxxxx-xxxx-xxxxxxxxx.us-east.aws.cloud.qdrant.io:6333",
    api_key="<your-api-key>",
)
```

## Example

Create a new collection

```
from qdrant_client.models import Distance, VectorParams

client.recreate_collection(
    collection_name="my_collection",
    vectors_config=VectorParams(size=100, distance=Distance.COSINE),
)
````

Insert vectors into a collection

```
import numpy as np
from qdrant_client.models import PointStruct

vectors = np.random.rand(100, 100)
# NOTE: consider splitting the data into chunks to avoid hitting the server's payload size limit
# or use `upload_collection` or `upload_points` methods which handle this for you
# WARNING: uploading points one-by-one is not recommended due to requests overhead
client.upsert(
    collection_name="my_collection",
    points=[
        PointStruct(
            id=idx,
            vector=vector.tolist(),
            payload={"color": "red", "rand_number": idx % 10}
        )
        for idx, vector in enumerate(vectors)
    ]
)
```

Search for similar vectors

```
query_vector = np.random.rand(100)
hits = client.search(
    collection_name="my_collection",
    query_vector=query_vector,
    limit=5  # Return 5 closest points
)
```

Search for similar vectors with filtering condition

```
from qdrant_client.models import Filter, FieldCondition, Range

hits = client.search(
    collection_name="my_collection",
    query_vector=query_vector,
    query_filter=Filter(
        must=[  # These conditions are required for search results
            FieldCondition(
                key='rand_number',  # Condition based on values of `rand_number` field.
                range=Range(
                    gte=3  # Select only those results where `rand_number` >= 3
                )
            )
        ]
    ),
    limit=5  # Return 5 closest points
)
```

#### gRPC

```
from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", grpc_port=6334, prefer_grpc=True)
```

### Async client

```
from qdrant_client import AsyncQdrantClient, models
import numpy as np
import asyncio

async def main():
    # Your async code using QdrantClient might be put here
    client = AsyncQdrantClient(url="http://localhost:6333")

    await client.create_collection(
        collection_name="my_collection",
        vectors_config=models.VectorParams(size=10, distance=models.Distance.COSINE),
    )

    await client.upsert(
        collection_name="my_collection",
        points=[
            models.PointStruct(
                id=i,
                vector=np.random.rand(10).tolist(),
            )
            for i in range(100)
        ],
    )

    res = await client.search(
        collection_name="my_collection",
        query_vector=np.random.rand(10).tolist(),  # type: ignore
        limit=10,
    )

    print(res)

asyncio.run(main())
```
