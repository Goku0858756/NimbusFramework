## ------------------------------
Core
  [overall]
    save    (saves state framework)
    load    (load session state)
            ->  last    (loads last session)
            ->  ?       (are there sessions?)
            ->  [name]  (load session by name)
            ->  [date]  (load session by date)
            ->  [nr]    (load session by number)

    config  (config file)
            (config proxy with file)
            (config vpn with file)

    user    (add, edit, remove users)
            ->  add
                [parser]
                  name passwd   (create user and add to the database)
            ->  edit
                [parser]
                  'username'
            ->  remove
                [parser]
                  'username'
            ->  update
                [parser]
                  'username' passwd   (update password for username)
                  'username' name     (update username for username)
    sys     ()
    exit    (exit framework)

## ------------------------------
Database (CLiDL)
  [overall]
    db        (call Database Object by putting 'db' as first keyword)

  [shell]
    create    ->  save
    read      ->  find
    update    ->  edit
    delete    ->  remove

                  [parser]
                    limit   -> ##
                    order   -> TOP.NR               ("top10")
                            -> BOT.NR               ("bot10")
                            -> MIN.NR               ("min10")
                            -> MAX.NR               ("max10")

Vulnerability.Parser
                  [parser]
                    cms     ->  CMS.NAME            ("wordpress", "joomla", "...")
                    port    ->  PORT.NR             ("21", "443", "...")
                    geo     ->  GEO.NAME            ("NL", "Netherlands", "...")
                    ip      ->  IP.RANGE            ("00.00.00.000-255")
                    prot    ->  PROTOCOL.NAME       ("ftp", "ssh", "...")
                    server  ->  SERVER.NAME         ("iis", "apache", "...")
                    vuln    ->  VULNERABILITY.TYPE  ("xss", "sqli", "...")
                    type    ->  TYPE.HOST           ("Modem", "Webhost")


## ------------------------------
Crawler
  [overall]
    crawl       (call Crawler Object by putting 'crawl' as first keyword)

  [shell]
    save
    queue

## ------------------------------
Target
  [overall]
    target      (call Target Object by putting 'target' as first keyword)

  [shell]
    find
    save
    edit
    remove

## ------------------------------
Domotica
    [overall]
      dom       (call Domotica Object by putting 'dom' as first keyword)

    [shell]
      lights    (PHILIPS Hue Connection)
      music     (SONOS Connection)
      doors     (DOOR Connection)
      bell      (DOORBEL Connection)
      cam       (CAMERA Connection)

## ------------------------------
Scanner
  [overall]
    scan        (call Scanner Object by putting 'scan' as first keyword)

  [shell]
    cms         (CMS discovery Plugin)
                [parser]
                  target    (scans the current target if has URL)
                  url       (scans the given url)
    dns         (DNS Vulnerability Scan)
                [parser]
                  ...
    whois       (do a Whois Scan)
                [parser]
                  target    (...)
