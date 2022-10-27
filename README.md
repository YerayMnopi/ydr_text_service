# Text service
A python microservice responsible for managing text (articles, definitions, code, etc.). All the text are independent objects and can be shared between articles.

## Run with docker
`docker build . -t ydr_text_service`
`docker run -p 8000:8000  ydr_text_service`

## Run with pdm
`brew install pdm`
`pdm run server`