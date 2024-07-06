from pinecone import Pinecone, ServerlessSpec

# initialize the client
pc = Pinecone(api_key="2da63e35-be7e-42e5-8716-78fe1462cd4b")


# create a serverless index named "quickstart" to perform nearest-neighbor
# search using the Euclidean distance metric for 8-dimensional vectors:
pc.create_index(
    name="quickstart",
    dimension=8, # Replace with your model dimensions
    metric="euclidean", # Replace with your model metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)
