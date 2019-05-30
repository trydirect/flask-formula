define({ "api": [
  {
    "type": "get",
    "url": "/api/v1/hello/",
    "title": "Hello",
    "version": "0.1.0",
    "name": "GetHello",
    "group": "Hello",
    "description": "<p>Returns simple string <code>Hello World!</code></p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"Hello World!\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "500 Internal Server Error": [
          {
            "group": "500 Internal Server Error",
            "optional": false,
            "field": "InternalServerError",
            "description": "<p>The server encountered an internal error</p>"
          }
        ],
        "404 Not Found": [
          {
            "group": "404 Not Found",
            "optional": false,
            "field": "Not",
            "description": "<p>Found</p>"
          }
        ]
      }
    },
    "filename": "apps/hello/views.py",
    "groupTitle": "Hello"
  },
  {
    "type": "post",
    "url": "/api/v1/hello/positive_rate/",
    "title": "Predict positive rate",
    "version": "0.1.0",
    "name": "List",
    "group": "Predict",
    "description": "<p>Returns the predicted positive rate</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"success\": true,\n    \"result\":{\n        \"number\": 2389\n    }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200\n{\n    \"success\": false,\n    \"errors\":{\n        \"global_error\":{\n            \"code\": 3066431594,\n            \"message\": \"Not found\"\n        }\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "apps/hello/views.py",
    "groupTitle": "Predict"
  },
  {
    "type": "post",
    "url": "/api/v1/auth/",
    "title": "Authenticate",
    "version": "0.1.0",
    "name": "auth",
    "group": "auth",
    "description": "<p>Authenticate a customer and returns a token that should be used in header as <code>Authentication-Token</code></p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Customer's email.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>Customer's password.</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"success\": true,\n    \"response\":\n        {\n            \"auth_token\": \"token_string_goes_here\"\n        }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 401\n{\n  \"errors\": {\n    \"global_error\": {\n      \"code\": 186976853,\n      \"message\": \"Incorrect credentials\"\n    }\n  },\n  \"success\": false\n}",
          "type": "json"
        },
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 401\n{\n  \"errors\": {\n    \"fields\": {\n      \"password\": {\n        \"code\": 663292517,\n        \"message\": \"This field is required.\"\n      }\n    },\n    \"global_error\": {\n      \"code\": 805898986,\n      \"message\": \"Fields validation error\"\n    }\n  },\n  \"success\": false\n}",
          "type": "json"
        }
      ]
    },
    "filename": "apps/user/views.py",
    "groupTitle": "auth"
  },
  {
    "type": "get",
    "url": "/api/v1/mail",
    "title": "Send of Mail",
    "version": "0.1.0",
    "name": "mail",
    "group": "mail",
    "description": "<p>Checking was send messages or not</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"success\": \"true\",\n    \"response\": \"Mail sent!\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "500 Internal Server Error": [
          {
            "group": "500 Internal Server Error",
            "optional": false,
            "field": "InternalServerError",
            "description": "<p>The server encountered an internal error</p>"
          }
        ],
        "404 Not Found": [
          {
            "group": "404 Not Found",
            "optional": false,
            "field": "Not",
            "description": "<p>Found</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 400\n{\n    \"success\": false,\n    \"response\": \"Something went wrong!\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "apps/hello/views.py",
    "groupTitle": "mail"
  },
  {
    "type": "get",
    "url": "/api/v1/rabbit/send",
    "title": "RabbitMQ",
    "version": "0.1.0",
    "name": "rabbit",
    "group": "rabbit",
    "description": "<p>Checks connecting to RabbitMQ and then create queue named <code>hello</code></p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"success\": true,\n    \"response\": \"Created queue name `hello` and saved value\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "500 Internal Server Error": [
          {
            "group": "500 Internal Server Error",
            "optional": false,
            "field": "InternalServerError",
            "description": "<p>The server encountered an internal error</p>"
          }
        ],
        "404 Not Found": [
          {
            "group": "404 Not Found",
            "optional": false,
            "field": "Not",
            "description": "<p>Found</p>"
          }
        ]
      }
    },
    "filename": "apps/rabbitmq/views.py",
    "groupTitle": "rabbit"
  },
  {
    "type": "get",
    "url": "/api/v1/rabbit/send",
    "title": "RabbitMQ",
    "version": "0.1.0",
    "name": "rabbit",
    "group": "rabbit",
    "description": "<p>Connecting to RabbitMQ and then create queue named <code>hello</code></p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n     \"success\": true,\n     \"response\": \"We have got value from queue `hello`\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "500 Internal Server Error": [
          {
            "group": "500 Internal Server Error",
            "optional": false,
            "field": "InternalServerError",
            "description": "<p>The server encountered an internal error</p>"
          }
        ],
        "404 Not Found": [
          {
            "group": "404 Not Found",
            "optional": false,
            "field": "Not",
            "description": "<p>Found</p>"
          }
        ]
      }
    },
    "filename": "apps/rabbitmq/views.py",
    "groupTitle": "rabbit"
  },
  {
    "type": "get",
    "url": "/api/v1/redis",
    "title": "Test Redis",
    "version": "0.1.0",
    "name": "redis",
    "group": "redis",
    "description": "<p>Checks connecting to Redis and create key with value</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"success\": True,\n    \"response\": \"Connected!\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "500 Internal Server Error": [
          {
            "group": "500 Internal Server Error",
            "optional": false,
            "field": "InternalServerError",
            "description": "<p>The server encountered an internal error</p>"
          }
        ],
        "404 Not Found": [
          {
            "group": "404 Not Found",
            "optional": false,
            "field": "Not",
            "description": "<p>Found</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 400\n{\n    \"success\": false,\n    \"response\": \"Something went wrong!\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "apps/hello/views.py",
    "groupTitle": "redis"
  }
] });
