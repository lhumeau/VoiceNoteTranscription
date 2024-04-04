# VoiceNoteTranscription

VoiceNoteTranscription es una API desarrollada con FastAPI para transcribir notas de voz. Permite a los usuarios cargar archivos de audio y recibir una transcripción de texto de los mismos, facilitando así la conversión de contenido hablado a texto.

## Características

- **Transcripción de voz a texto:** Carga archivos de voz y recibe transcripciones precisas.
- **Fácil de usar:** Interfaz de API sencilla y documentada.
- **Soporte para múltiples formatos de audio:** Compatible con los formatos de audio más comunes.

## Tecnologías utilizadas

- FastAPI
- Uvicorn
- SpeechRecognition
- PyDub
- Python-Multipart

## Instalación y uso

Este proyecto está contenerizado usando Docker, facilitando su despliegue y ejecución. A continuación, se detallan los pasos para instalar y ejecutar el proyecto localmente.

### Requisitos previos

Asegúrate de tener Docker y Docker Compose instalados en tu sistema. Para más información sobre cómo instalar Docker, visita [la página oficial de Docker](https://docs.docker.com/get-docker/).

### Pasos para la ejecución

1. **Clonar el repositorio:**

```bash
git clone https://github.com/lhumeau/VoiceNoteTranscription.git
cd VoiceNoteTranscription
```

## Construir y ejecutar el contenedor:

Utiliza Docker Compose para construir y ejecutar la aplicación:

`docker-compose up --build`

Esto iniciará la aplicación y estará accesible desde http://localhost:8000.

## Uso de la API

Para transcribir notas de voz, puedes usar herramientas como Postman o realizar una solicitud curl desde la línea de comandos. Aquí tienes un ejemplo de cómo hacerlo:

```curl -X 'POST' \
  'http://localhost:8000/transcripcion' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'archivo=@tu_archivo_de_audio.aac;type=audio/aac'
```


Reemplaza tu_archivo_de_audio.aac con el camino a tu archivo de audio o Formatos m4a,3gp...etc 

## Contribuir

Si deseas contribuir al proyecto, por favor considera lo siguiente:

- Realiza un fork del repositorio.

- Crea una rama para tu característica o corrección.

- Envía un pull request con tus cambios.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT, lo que permite un uso amplio y modificación bajo los términos específicos de la licencia.

