# EthereumBA Meetups DataSet

This repository contains a public dataset containing information exported from [Ethereum Meetup](https://www.meetup.com/ethereum-ba/) alongside with the attendance information. This can be used to gather some statistics (i.e. RSVP vs attendance, churn) in order to improve the comms, quality of the content, etc.

A python script to regenerate the dataset is also provided alongside with a set of already created queries that can be used to analyze the content of the dataset.

_isclaimer: This is a very first version version with a lot of open `TODOs` and bugs._

## Note about privacy

The main goal is to completely respect users privacy. In order to do so, the dataset that can be found in this repository is de-anonymized before being pushed. To do so, we use a random user id generator (without any link to the original data, no PII hash calculation at all).

## TOC

<!-- toc -->

- [Goal](#goal)
- [Data Sources](#data-sources)
- [Results](#results)
- [Queries](#queries)
  - [List](#list)
  - [Status Description](#status-description)

* [Current Data Set](#current-data-set)
  - [Generating the dataset locally](#generating-the-dataset-locally)
    - [Requirements](#requirements)
    - [Setup](#setup)
    - [Running the import script](#running-the-import-script)
      - [Import files structure](#import-files-structure)
      - [Execution](#execution)
    - [TODO](#todo)
* [Bugs](#bugs)

<!-- tocstop -->

## Goal

The following document proposes a set of queries we can ran against all the information EthBA has collected over the time in order to:

- Analyze subscriptions and assistance information to improve EthBA organization, the talks topics and content creation in order to bring more people to our meetups.
- Open source the anonymized datasets to promote EthBA good practices and openness.

## Data Sources

The following data sources will be used to gather information about the meetups:

- Meetup.com RSVP dumps.
- Attendance lists completed by EthBA team.
- Claimed POAPs.

## Results

- The dataset should be published and shared with the community.
- The dataset should be able to be easily rebuilt or extended if new data is available.
- All the queries must be shared in order to let other people to run or improve them.
- The results should be presented as charts.

## Queries

### List

- **RSVP vs attended by event** `[STARTED]`
  - Goal: to understand if people actually comes to the events. Strange cases can also be analyzed, for example, an big difference between RSVP and attendance could be due to a heavy rain or a sudden change in the agenda.
  - RSVP is already done
  - Data about people attending is not complete and needs manual processing.
- **RSVP by topic** `[PROPOSAL]`
  - Goal: to understand if there are topics that are more attractive to people.
  - Topics will need to be manually assigned to each event (error prone)
- **Amount of people that stopped responding RSVP by event** `[DONE]`
  - Goal: This will help to understand the churn rate and to analyze if there are some event that are not attractive to some people.
- **Amount of people that started responding RSVP by event** `[DONE]`
  - Goal: This might give an idea about which events were more interesting for the community. It's important to note that this will also be affected by comms difussion and the meetup being more mature.
- **Average assistance percentage** `[DONE]`
  - Goal: Determine what's the overall assistance rate to be able analyze possible improvements (for example, implementing something like kickback).
- **Amount of people that claimed POAP by event** `[PROPOSAL]`
  - Goal: Will give an idea of the amount of people that actually came to an event (at least for a couple of mins)
  - We will need to look for POAP info (that is incomplete as it started after some meetups).
  - Some people might have just stayed to claim the POAP and left.
  - Not sure how will this work as the meetups are being done online now.

### Status Description

- `[PROPOSAL]`: Still to be decided if it's worthy to do it or not.
- `[TODO]`: Already defined but not work done yet.
- `[STARTED]`: Some work has been done but not finished yet.
- `[DONE]`: Finisheda already.

# Current Data Set

An updated version of the dataset can be found and downloaded [here](./dataset/ethba-dataset.db). You can use any SQL browser tool to run your queries. Some some sample queries can be found [here](./queries).

| Name                                                                      | Date       |
| ------------------------------------------------------------------------- | ---------- |
| Ethereum Buenos Aires (Panel - 1 meetup juntos)                           | 2018-12-13 |
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
| Uniswap & Balancer Ethereum Chicago & BA meetup                           | 2020-06-25 |

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

- [ ] `CHANGELOG.md`
- [ ] Try to deduplicate people with multiple meetup user ids
- [ ] DB model diagram
- [ ] Proper logging instead of print
- [ ] Error handling. Atm, if an error occurs, it just crashes.
- [ ] Tests
- [ ] cli to execute specific actions:
  - destroy dataset
  - anonymize
  - parse
- [ ] Code review

# Bugs

See the [github issues list](https://github.com/AlanVerbner/ethereum-meetups-dataset/issues?q=is%3Aopen+is%3Aissue+label%3Abug)
