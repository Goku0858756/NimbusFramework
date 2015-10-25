# Nimbus Workflow
    Start server < Start | Stop | Restart | Update | Help >

### Path 01
    use Template/Script to use the Scanner
    
### Path 02
    Hail Mary Style Scanning
    
### Path 03
    Smart Scanning
    
id | Component | Threaded
-- | --------- | --------
00 | IP/DNS Scan | NO
01 | Port Scan | NO
02 | Enumerate | NO
03 | CMS Discover | NO
04 | Crawl     | YES
05 | Path Traversal | NO 

### Path 04
    Sneaky Scanning
    


## Nimbus Integrated Services

id | Service Name | Working | Threaded | PID Controle | Integraded | File Type | Done
-- | ------------ | ------- | -------- | ------------ | ---------- | --------- | ----
01 | Mongo Db     | YES     | NO       | YES          | NO         | JSON      | NO
02 | Fuzz Db      | NO      | NO       | NO           | NO         | JSON      | NO
03 | Nmap         | YES     | NO       | NO           | YES        | JSON/XML  | NO



#### Fase 01: Scan Server
#### Fase 02: Scan per Port
#### Fase 03: Scan OS or CMS
#### Fase 04: Crawl Site
#### Fase 05: Path Traversal
#### Fase 06: 
