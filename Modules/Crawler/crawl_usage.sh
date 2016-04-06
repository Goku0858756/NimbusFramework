#!/usr/bin/env bash

    [!] ************************************************************************
    [!] *   Command Value       Description                                    *
    [!] ************************************************************************
    [!] *   crawl   ?           - Help command for the crawl command           *
    [!] *   crawl   help        - Also help to show all crawl commands         *
    [!] *                                                                      *
    [!] ************************************************************************
    [!] *   crawl   ...:...     - key:value                                    *
    [!] *   crawl   url:...     - Crawl the given URL                          *
    [!] *   crawl   name:...    - Check in DB for targets by given Name        *
    [!] *   crawl   id:...      - Check in DB for targets by given id          *
    [!] *   crawl   ip:...      - Check in DB for targets by given ip          *
    [!] *                                                                      *
    [!] ************************************************************************
    [!] *   crawl   file:...    - Give a path for a parsing crawl.yaml file    *
    [!] *   crawl   config:...  - Give a path for a parsing config.yaml file   *
    [!] *   crawl   algo:...    - Give a path for a parsing algo.yaml file     *
    [!] *                                                                      *
    [!] ************************************************************************
    [!] *   start               - Start Crawling                               *
    [!] *   pause               - Pause Crawling                               *
    [!] *   stop                - Stop Crawling                                *
    [!] *                                                                      *
    [!] ************************************************************************
    [!] * Extra information                                                    *
    [!] ************************************************************************
    [!] * The soul purpose of the crawler is to find possible injection points *
    [!] * These points can be URLs, HTML5, Javascript, CSS, Flash or other     *
    [!] * possible points to inject XSS or SQL to penetrate into a website.    *
    [!] * The Nimbus Crawler is in heavy development, so please keep in mind   *
    [!] * that there can be some codes that will give an Error Exception       *
    [!] *                                                                      *
    [!] * The Data, Crawler Shell, Spiders, Algorithms, Config and Plugins     *
    [!] * are all seperate so one can adjust the crawl session as pleased      *
    [!] *                                                                      *
    [!] *                                                                      *
    [!] ************************************************************************
    [!] *  Data                                                                *
    [!] * ******************************************************************** *
    [!] * The Data Object can be used to choose to push the data into the      *
    [!] * database, or dump it into a given file                               *
    [!] *                                                                      *
    [!] ************************************************************************
    [!] *  Plugin                                                              *
    [!] * ******************************************************************** *
    [!] * The Plugin command can be used to see which plugins are available    *
    [!] * for the current session. Also these Plugins can be individually      *
    [!] * set to True or False                                                 *
    [!] *                                                                      *
    [!] ************************************************************************
    [!] *  Config                                                              *
    [!] * ******************************************************************** *
    [!] * With a config.yaml file one can supply a template for the current    *
    [!] * session. In the config.yaml file you can specify what plugins to use *
    [!] * and also you can specify a target                                    *
    [!] *                                                                      *
    [!] ************************************************************************
    [!] *  Algorithm                                                           *
    [!] * ******************************************************************** *
    [!] * By providing an algo.yaml file, you can give command as a            *
    [!] * chain of commands. The crawler will follow the given function one    *
    [!] * after another. This can be done by giving an extra argument to the   *
    [!] * crawler like so: argo:path_to_file.yaml                              *
    [!] *                                                                      *
    [!] ************************************************************************

