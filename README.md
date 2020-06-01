# EthereumBA Meetups DataSet

This repository contains a public dataset containing information exported from [Ethereum Meetup](https://www.meetup.com/ethereum-ba/) alongside with the attendance information. This can be used to gather some statistics (i.e. RSVP vs attendance, churn) in order to improve the comms, quality of the content, etc.

A python script to regenerate the dataset is also provided alongside with a set of already created queries that can be used to analyze the content of the dataset.

 _isclaimer: This is a very first version version with a lot of open `TODOs` and bugs._

## Note about privacy

The main goal is to completely respect users privacy. In order to do so, the dataset that can be found in this repository is de-anonymized before being pushed. To do so, we use a random user id generator (without any link to the original data, no PII hash calculation at all). 

## TOC

<!-- toc -->

- [Current Data Set](#current-data-set)
- [Generating the dataset locally](#generating-the-dataset-locally)
  * [Requirements](#requirements)
  * [Setup](#setup)
  * [Running the import script](#running-the-import-script)
    + [Import files structure](#import-files-structure)
    + [Execution](#execution)
- [TODO](#todo)
- [Bugs](#bugs)

<!-- tocstop -->

## Current Data Set

An updated version of the dataset can be found and downloaded [here](./dataset/ethba-dataset.db). You can use any SQL browser tool to run your queries. Some some sample queries can be found [here](./queries).

| Name                                                                      | Date       |
|---------------------------------------------------------------------------|------------|
| Ethereum  Buenos Aires (Panel - 1 meetup juntos)                          | 2018-12-13 |
| Seguridad en Smart Contracts                                              | 2019-01-31 |
| Buidler Marmo SDK Zerion                                                  | 2019-02-28 |
| RadicalxChange 1 a 1 How Dai is pegged to USD                             | 2019-03-29 |
| Smart Contracts Upgrades & DeFi                                           | 2019-05-02 |
| Escalando un mercado basado en blockchain                                 | 2019-05-30 |
| Lightning DeFi                                                            | 2019-06-27 |
| Escalando blockchain intro a Celo                                         | 2019-07-25 |
| xDAI Experimental                                                         | 2019-08-29 |
| DeFi (Ch. 3) Intro a POAP                                                 | 2019-09-26 |
| Diaspore Wibson reward marketplace                                        | 2019-10-24 |
| Meet & greet                                                              | 2019-11-22 |
| Aragon                                                                    | 2019-12-02 |
| Ultimo del año!! Multi Collateral DAI y LocalCryptos                      | 2019-12-19 |
| console.log en Solidity Contratos no tan inmutables                       | 2020-01-16 |
| DeFi Loans                                                                | 2020-02-27 |
| Black Thursday MakerDAO Backstop Syndicate                                | 2020-03-26 |
| MakerDAO's Black Thursday Survival + Decentraland's Metaverse Release     | 2020-04-30 |
| Ethereum BA Privacidad con Wibson Wrapped Tokens Pagos DeFi con StablePay | 2020-05-28 |


## Generating the dataset locally

### Requirements

- Python3
- pip3

### Setup

1. Install pipenv

```
pip3 install pipenv
```

2. Install the dependencies

```
pipenv install
```

### Running the import script

#### Import files structure

The scripts require two files in order to process the data:

```
./import
├── meetup dump.csv
└── meetups list.csv
```

- `meetup users.csv` is exported from [Meetup](https://meetup.com):

```
Nombre,Identificador del usuario,Título,Identificación del miembro,Ubicación,Se unió al grupo el,Última visita al grupo el,Último evento presenciado,RSVP totales,Respondió «Sí»,Respondió «Quizás»,Respondió «No»,Meetups a los que ha asistido,Ausencias,Presentación,Foto,Organizador asistente,Lista de correo,URL del perfil del miembro
Some Name,user 1111,,1111,Buenos Aires,14 de month de 2055,13 de month de 2055,,0,0,0,0,0,0,No,Sí,No,Sí,https://www.meetup.com/es/EthereumBA/members/1111/
```

- `meetup dump.csv` is exported from [Meetup](https://meeetup.com):

```
Meetup Name,Nombre,Identificador del usuario,Título,Anfitrión del evento,Inscribirse,Invitados,Respondió el,Se unió al grupo el,URL del perfil del miembro,Attended?
Ethereumm Buenos Aires (Panel - 1 meetap juntos),XXXXXXXX,XXXXXXXX,Organizador,Sí,Sí,,7 de diciembre de 2018 20:48,25 de julio de 2018,https://www.meetup.com/es/EthereumBA/members/XXXXXXXXX/,
Ethereumm Buenos Aires (Panel - 1 meetap juntos),XXXXXX,XXXXXXX,,,Sí,,7 de diciembre de 2018 21:04,18 de noviembre de 2018,https://www.meetup.com/es/EthereumBA/members/XXXXXXXX/,
```

- `meetups list.csv` contains all the meetups with the event date, for example:

```
ID,Date
Ethereumm Buenos Aires (Panel - 1 meetap juntos),2018-12-13
 Seguridad en Smart Contracts,2019-01-31
```

**Important: `Charla` and `ID` are the same field and are used to match records.**

#### Execution

```
pipenv run python main.py
```

### TODO

- [ ] `LICENSE.md`, `CONTRIBUTING.md`, `CHANGELOG.md` docs + Roadmap section
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

See the [github issues list](https://github.com/AlanVerbner/ethereum-meetups-dataset/issues?q=is%3Aopen+is%3Aissue+label%3Abug)
