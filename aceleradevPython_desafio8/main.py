
doc = '''
#%RAML 1.0
---
title: Desafio RAML API
version: v1
baseUri: http://api.desafioraml.com/{version}
mediaType: application/json
securitySchemes:
  JWT:
    description: Token JWT é utilizado para autenticaçao
    type: x-jwt
    describedBy:
      headers:
        Authorization:
          type: string
          required: true
      responses:
        401:
          description: |
            Token invalido ou expirado.
        403:
          description: |
            Bad JWT request
    settings:
      signatures : ['HMAC-SHA256']
              
types:
  Auth:
    type: object
    discriminator: token
    properties:
      token: string
  Agent:
    type: object
    discriminator: agent_id
    properties:
      agent_id: number
      name:
        type: string
        maxLength: 50
      status:
        type: boolean
      environment:
        type: string
        maxLength: 20
      version:
        type: string
        maxLength: 5
      address:
        type: string
        maxLength: 39
      user_id: number
    example:
      agent_id: 1
      user_id: 3
      name: NomeDoAgente
      status: true
      environment: TesteDoEnvironment
      version: v1
      address: 11.22.33.44
  Event:
    type: object
    discriminator: event_id
    properties:
      event_id:
        type: number
      level:
        type: string
        maxLength: 20
      payload: 
        type: string
      shelve: 
        type: boolean
      date: 
        type: datetime-only
      agent_id: 
        type: number
    example:
      event_id: 4
      level: debug
      payload: Teste
      shelve: true
      date: 2020-07-04T03:20:39
      agent_id: 5
  User:
    type: object
    discriminator: user_id
    properties:
      name:
        type: string
        maxLength: 50
      password:
        type: string
        maxLength: 50
      email:
        type: string
        maxLength: 254
      last_login: 
        type: date-only
      group_id: 
        type: number
      user_id: 
        type: number
    example:
      name: NomeDoUsuario
      password: senhadificil
      email: julinho@gmail.com
      last_login: 2020-07-04
      group_id: 6
      user_id: 2
  Group:
    type: object
    discriminator: group_id
    properties:
      name: 
        type: string
        maxLength: 20
      group_id:
        type: number
    example:
      name: NomeDoGrupo
      group_id: 8
traits:
  dataValidation:
    responses:
      400:
        description: Quando avalidação falha acontece um BadRequest
        body:
          application/json: |
            {"error": "Bad Request"} 
/auth/token:
  post:
    description: Criar um token
    body:
      application/json:
        properties:
          name: string
          password: string
    responses:
      201:
        body:
          application/json: Auth[]
      400:
        body:
          application/json: |
            {"error": "Bad Request"}
/agents:
  description: Dados dos agentes
  get:
    description: Pega os agentes.
    securedBy: [JWT]
    responses:
      200:
        body: 
          application/json: Agent[]
  post:
    is: [dataValidation]
    securedBy: [JWT]
    description: Adiciona um agente.
    body:
      application/json:
        example: |
          {"user_id": 3,
            "name": "NomeDoAgente",
            "status": true,
            "environment": "TesteDoEnvironment",
            "version": "v1",
            "address": "11.22.33.44"
            }
    responses:
      201:
        description: Retorna o novo agente.
        body: 
          application/json: |
            {"message": "Created"}
      401:
        body:
          application/json: |
            {"message": "Unauthorized"}
      404:
        body:
          application/json: |
            {"error": "Not Found"}
      409:
        description: Esse agente já existe.
        body:
          application/json: |
            {"error": "Not Found"}
  /{id}:
    get:
      securedBy: [JWT]
      description: Pega um agente especifico.
      responses:
        200:
          description: Retorna um agente especifico
          body: 
            application/json: Agent[]
        401:
          body:
            application/json: |
              {"message": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not Found"}
    put:
      is: [dataValidation]
      securedBy: [JWT]
      description: Atualiza um agente já criado.
      responses:
        200:
          description: retorna um agente atualizado
          body: 
            application/json: Agent[]
        401:
          body:
            application/json: |
              {"message": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not Found"}
    delete:
      securedBy: [JWT]
      description: Deleta um agente
      responses:
        200:
          body:
            application/json: |
              {"message": "Ok"}
        204:
          description: deletado.
          body:
            application/json: |
             {"message": "No content"}
        401:
          body:
            application/json: |
              {"message": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not Found"}
  /{id}/events:
    description: Dados dos agentes
    get:
      description: Pega os eventos
      securedBy: [JWT]
      responses:
        200:
          body: 
            application/json: Event[]
        401:
          body:
            application/json: |
              {"message": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not Found"}
    post:
      is: [dataValidation]
      securedBy: [JWT]
      description: Adiciona um Evento
      body:
        application/json: Event[]
      responses:
        201:
          description: Retorna um novo Evento.
          body:
            application/json: |
              {"message": "Created"}
        401:
          body:
            application/json: |
              {"message": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not Found"}
    put:
      securedBy: [JWT]
      description: Atualiza um evento atraves de um agente
      body:
        application/json: Event[]
      responses:
        200:
          body:
            application/json: |
              {"message": "Ok"}
        401:
          body:
            application/json: |
              {"message": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not Found"}
    delete:
      description: Deleta evento
      securedBy: [JWT]
      body:
        application/json: Event[]
      responses:
        200:
          body:
            application/json: |
              {"message": "Ok"}
        401:
          body:
            application/json: |
              {"message": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not Found"}
    /{id}:
      get:
        securedBy: [JWT]
        description: Pega um evento especifico
        responses:
          200:
            description: Retorna um evento especifico
            body: 
               application/json: Event[]
          401:
            body:
               application/json: |
                 {"message": "Unauthorized"}
          404:
            body:
               application/json: |
                 {"error": "Not Found"}
      post:
        description: Gravar um evento atraves de um ID
        securedBy: [JWT]
        responses:
          200:
            body:
              application/json: |
                {"message": "Ok"}
          401:
            body:
              application/json: |
                {"message": "Unauthorized"}
          404:
            body:
              application/json: |
                {"error": "Not Found"}
      put:
        is: [dataValidation]
        securedBy: [JWT]
        body:
          type: Event
        description: Atualiza um evento ja criado.
        responses:
          200:
            description: retorna um evento atualizado
            body: 
              json/application: Event[]
          401:
            body:
              application/json: |
                {"message": "Unauthorized"}
          404:
            body:
              application/json: |
                {"error": "Not Found"}
      delete:
        description: Deleta um evento
        securedBy: [JWT]
        responses:
          200:
            description: deletado
            body:
              application/json: |
                {"message": "Ok"}
          401:
            body:
              application/json: |
                {"error": "Unauthorized"}
          404:
            body:
              application/json: |
                {"error": "Not Found"}
/groups:
  description: Dados dos grupos
  get:
    description: Pega os grupos
    securedBy: [JWT]
    responses:
      200:
        body: 
          application/json: Group[]
      401:
        body:
          application/json: |
            {"error": "Unauthorized"}
      404:
        body:
          application/json: |
            {"error": "Not found"}
  post:
    is: [dataValidation]
    securedBy: [JWT]
    description: Adiciona um grupo
    body:
      application/json:
        properties:
          name:
            type: string
            maxLength: 20
        example:
          name: "NomeDoGrupo"
    responses:
      201:
        description: Retorna o novo grupo
        body: 
          application/json: |
            {"message": "ok"}
      401:
        body:
          application/json: |
            {"error": "não autorizado"}
      409:
        description: Esse grupo já existe
        body:
          application/json: |
            {"error": "Conflict"}
  put:
    description: Alterar um grupo
    securedBy: [JWT]
    responses:
      200:
        body:
          application/json: Group[]
      401:
        body:
          application/json: |
            {"error": "Unauthorized"}
      404:
        body:
          application/json: |
            {"error": "Not found"}
  delete:
    description: Deletar um grupo
    securedBy: [JWT]
    responses:
      200:
        body:
          application/json: Group[]
      401:
        body:
          application/json: |
            {"error": "Unauthorized"}
      404:
        body:
          application/json: |
            {"error": "Not found"}        
  /{id}:
    get:
      securedBy: [JWT]
      description: Pega um grupo especifico.
      responses:
        200:
          description: Retorna um grupo especifico
          body: 
            application/json: Group[]
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not found"}   
    put:
      is: [dataValidation]
      securedBy: [JWT]
      description: Atualiza um grupo já criado.
      responses:
        200:
          description: retorna um grupo atualizado
          body: 
            application/json: |
              {"message": "ok"}
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not found"}
    delete:
      securedBy: [JWT]
      description: Deleta um grupo
      responses:
        204:
          description: deletado.
          body:
            application/json: |
              {"message": "No content"}
        200:
          body:
            application/json: |
              {"message": "Ok"}
        401:  
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not found"}
/users:
  description: Dados dos usuarios
  get:
    description: Pega os usuarios
    securedBy: [JWT]
    responses:
      200:
        body: 
          application/json: User[]
      401:
        body:
          application/json: |
            {"error": "Unauthorized"}
  post:
    is: [dataValidation]
    securedBy: [JWT]
    description: Adiciona um usuario
    body:
      application/json:
        properties:
          name:
            type: string
            maxLength: 50
          password:
            type: string
            maxLength: 50
          email:
            type: string
            maxLength: 254
          last_login:
            type: date-only
        example: |
          {"name": "NomeDoUsuario",
          "password": "senhadificil",
          "email": "julinho@gmail.com",
          "last_login": "2020-07-04",
          "group_id": "6"
          }
    responses:
      201:
        description: Retorna o novo usuario
        body:
          application/json: |
            {"message": "ok"}
      401:
        body:
          application/json: |
            {"error": "Unauthorized"}
      409:
        description: Esse usuário já existe
        body:
          application/json: |
            {"error": "Conflict"}
  /{id}:
    get:
      securedBy: [JWT]
      description: Pega um usuário especifico.
      responses:
        200:
          description: Retorna um usuário especifico
          body:
            application/json: User[]
        401:
          body:
            application/json: |
              {"error": "unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not found"}
    put:
      is: [dataValidation]
      securedBy: [JWT]
      description: Atualiza um usuário já criado.
      responses:
        200:
          description: retorna um usuário atualizado
          body:
            application/json: |
              {"message": "Ok"}
        401:
          body:
            application/json: |
              {"error": "unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not found"}
    delete:
      is: [dataValidation]
      description: Deleta um usuário
      securedBy: [JWT]
      responses:
        200:
          body:
            application/json: |
              {"message": "Ok"}
        204:
          description: deletado. 
          body:
            application/json: |
              {"message": "No content"}
        401:
          body:
            application/json: |
              {"error": "unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not found"}
'''