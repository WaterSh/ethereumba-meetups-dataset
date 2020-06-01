# EthereumBA Meetups DataSet

This repository contains a public dataset containing information exported from [Ethereum Meetup](https://www.meetup.com/ethereum-ba/) alongside with the attendance information. This can be used to gather some statistics (i.e. RSVP vs attendance, churn) in order to improve the comms, quality of the content, etc.

A python script to regenerate the dataset is also provided alongside with a set of already created queries that can be used to analyze the content of the dataset.

_Disclaimer: This is a very first version version with a lot of open `TODOs` and bugs._

## Note about privacy

The main goal is to completely respect users privacy. In order to do so, the dataset that can be found in this repository is de-anonymized before being pushed. To do so, we use a random name generator (without any link to the original data, no PII hash calculation at all). **All the names published here are completely faked but can correspond to a 1-to-1 real person mapping.**

# TOC

<!-- toc -->

- [Generating the dataset locally](#generating-the-dataset-locally)
  * [Requirements](#requirements)
  * [Setup](#setup)
  * [Running the import script](#running-the-import-script)
    + [Import files structure](#import-files-structure)
    + [Execution](#execution)
- [TODO](#todo)
- [Bugs](#bugs)

<!-- tocstop -->

# Generating the dataset locally

## Requirements

- Python3
- pip3

## Setup

1. Install pipenv

```
pip3 install pipenv
```

2. Install the dependencies

```
pipenv install
```

## Running the import script

### Import files structure

The scripts require two files in order to process the data:

```
./import
├── meetup_dump.csv
└── meetups_list.csv
```

- `meetup_users.csv` is exported from [Meetup](https://meetup.com):

```
Nombre,Identificador del usuario,Título,Identificación del miembro,Ubicación,Se unió al grupo el,Última visita al grupo el,Último evento presenciado,RSVP totales,Respondió «Sí»,Respondió «Quizás»,Respondió «No»,Meetups a los que ha asistido,Ausencias,Presentación,Foto,Organizador asistente,Lista de correo,URL del perfil del miembro
Some Name,user 1111,,1111,Buenos Aires,14 de month de 2055,13 de month de 2055,,0,0,0,0,0,0,No,Sí,No,Sí,https://www.meetup.com/es/EthereumBA/members/1111/
```

- `meetup_dump.csv` is exported from [Meetup](https://meeetup.com):

```
Meetup Name,Nombre,Identificador del usuario,Título,Anfitrión del evento,Inscribirse,Invitados,Respondió el,Se unió al grupo el,URL del perfil del miembro,Attended?
Ethereumm Buenos Aires (Panel - 1 meetap juntos),XXXXXXXX,XXXXXXXX,Organizador,Sí,Sí,,7 de diciembre de 2018 20:48,25 de julio de 2018,https://www.meetup.com/es/EthereumBA/members/XXXXXXXXX/,
Ethereumm Buenos Aires (Panel - 1 meetap juntos),XXXXXX,XXXXXXX,,,Sí,,7 de diciembre de 2018 21:04,18 de noviembre de 2018,https://www.meetup.com/es/EthereumBA/members/XXXXXXXX/,
```

- `meetups_list.csv` contains all the meetups with the event date, for example:

```
ID,Date
Ethereumm Buenos Aires (Panel - 1 meetap juntos),2018-12-13
Ethereum_Buenos_Aires_Seguridad_en_Smart_Contracts,2019-01-31
```

**Important: `Charla` and `ID` are the same field and are used to match records.**

### Execution

```
pipenv run python main.py
```

# TODO

- [ ] `LICENSE.md` & `CONTRIBUTING.md` and goal docs
- [ ] Try to deduplicate people with multiple meetup user ids
- [ ] DB model diagram
- [ ] Proper logging instead of print
- [ ] Error handling. Atm, if an error occurs, it just crashes.
- [ ] Remove duplicated code
  - csv file iteration
  - cursor creation and commiting data
- [ ] Tests
- [ ] cli to execute specific actions:
  - destroy dataset
  - anonymize
  - parse
- [ ] Code review

# Bugs

No bugs found yet
