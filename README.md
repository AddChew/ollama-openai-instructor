# Ollama, OpenAI and Instructor

Playground repository to explore Ollama, OpenAI and Instructor libraries.

### Useful commands

1) Run ollama with docker

```shell
# First run
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

# Subsequent runs
docker start ollama
```

2) Enter ollama docker container and run model

```shell
docker exec -it ollama ollama run llama2:chat
docker exec -it ollama ollama run tinyllama:chat
```

3) Stop ollama docker container

```shell
docker stop ollama
```

### How to interact with Ollama REST API

#### Ollama API

Generate a response

```shell
curl http://localhost:11434/api/generate -d '{
  "model": "llama2:chat",
  "prompt":"Why is the sky blue?"
}'
```

Chat with a model

```shell
curl http://localhost:11434/api/chat -d '{
  "model": "llama2:chat",
  "messages": [
    { "role": "user", "content": "why is the sky blue?" }
  ]
}'
```

#### OpenAI API

```shell
curl http://localhost:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "llama2:chat",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Why is the sky blue?"
            }
        ]
    }'
```