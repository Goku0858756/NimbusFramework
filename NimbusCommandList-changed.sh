## Commands to config the Nimbus-bot [ configuration ]
function  config
          config
          config ?            ## List all configurable nodes]
          config pass         ## Set a Password for your Nimbus Framework
          config pass change  ## Change your password
          config encrypt true ## Default: False Encrypt Framework
          config decrypt      ##

  ##
  ## Commands for the Nimbus System [ settings ]
  ## [ set ] [ setting ] [ to ]
  function  set
            set
            set ?         ## List all Settings for MainThread

  ## [ get ] [ setting ] [ from/of ]
  function  get
            get           ## Do you want to get candy? No .. ? Type: get ? for usage
            get ?         ## What setting do you want to know? || List possible settings

## Commands to use the Services in Nimbus Framework
function  service
          service         ## What do you want to do? Type: service ? for usage
          service ?       ## List al possible commands for usage service
          services        ## List all Services [True/False]

##
## Commands to get Sessions working [ threads && threadPools ]
## [ sessions ]
function  session
          session ?           ## List all commands for use of Session(s)
          sessions            ## List all Sessions [True/False]
          session history

        ## @WEB
        session $web start   ## Start a thread in Web
        session $web stop    ## Stop the Web thread
        session $web use     ## Use/Get into the web session
        session $web del     ## Delete the Session and the records

            ## ~~ Web
            ## Web Session embedded Commands
            $web >
            $web > ?                      ## List all possible commands in $web
            $web > plugins                ## List all possible Plugins in $web ["crawl", "harvest", "sql", "xss"]
                   $crawl    p["target", "depth", "level", "base_url"]
                   $InsecureHTTP   //sslscan
                   $CookieFlags    // Cookie flag Secure, HTTP-Only, etc.
                   $sql      p["--wizard"]    ## @iFace sqlMap
                   $xss      p["--wizard"]
                   $lfirfi
                   $csrf
                   $inputvalidation
                   $dos

            $web > modus ?                ## List available modus @Default: recon ["recon", "attack"]
                   $modus "non-intrusive"
                   $modus "attack"
            $web >
            ## @INFORMATIONGATHERING
            $gathering >
            $gathering > ?
            $gathering> plugins
                  $harvest  p["email"]
                  $SocEng        // set (Social Engineer Toolkit) en recon-ng check in kali
                  $google        // site:target -www
                  $bing        // ip: target
                  $robtex
                  $shodan
                  $ripe
                  $kvk
        ## @TCP
        session $tcp start
        session $tcp stop
        session $tcp use
        session $tcp del

            ## ~~ Tcp
            ## TCP/IP Session embedded Commands
            $tcp >
            $tcp > ?
            $tcp > plugins
                   $Banner        ## Banner Grabbing
                   $ghost         ## Check for Ghost vulnerability
                   $shock         ## Check for ShellShock vulnerability
                   $bleed         ## Check for HeartBleed vulnerability
                   $nmap          ## @iFace :: NMap
                   $nmapscript
                   $masscan       ## @iFace :: MasScan
                   $dig           ## @iFace :: dig dns
            $tcp >

            ## ~~ UDP
            ## UDP/IP Session embedded Commands
            $udp >
            $udp > ?
            $udp > plugins
                   $snmp        ## Banner Grabbing
                   $ntp         ## Check for Ghost vulnerability
                   $dns         ## Check for ShellShock vulnerability
                   $smb         ## Check for HeartBleed vulnerability
                   $nmap        ## @iFace :: NMap
                   $dos
            $udp >


        ## STATiC COMMANDS
        ['--tab']                 ## Start session in a new Tab
        ['--save-output']         ## Save session to File
        ['--use-output']          ## Use a Output file from earlier
