basic_run:
	docker run -p 8080:8080 -p 50051:50051 cr.weaviate.io/semitechnologies/weaviate:1.26.1

get_config:
	curl -o docker-compose.yml "https://configuration.weaviate.io/v2/docker-compose/docker-compose.yml?clip_model=sentence-transformers-clip-ViT-B-32&generative_anthropic=true&generative_anthropic_key_approval=yes&generative_anyscale=false&generative_aws=false&generative_cohere=false&generative_mistral=true&generative_mistral_key_approval=yes&generative_octoai=false&generative_ollama=true&generative_openai=true&generative_openai_key_approval=yes&generative_palm=false&gpu_support=false&media_type=clip&modules=modules&ner_module=true&ner_module_model=dbmdz-bert-large-cased-finetuned-conll03-english&qna_module=true&qna_module_model=distilbert-base-uncased-distilled-squad&ref2vec_centroid=false&reranker_cohere=false&reranker_transformers=false&runtime=docker-compose&spellcheck_module=false&sum_module=true&sum_module_model=facebook-bart-large-cnn-1.0.0&weaviate_version=v1.26.1&weaviate_volume=host-binding"

