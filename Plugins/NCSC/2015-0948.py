__author__ = 'N05F3R4TU'

__CVE__  = "CVE-2015-4852"
__NCSC__ = "NCSC-2015-0948"
__NAME__ = "Deserialisation"
__VULN__ = ["Java", "commons-collection", "HTTP", "RMI", "Tomcat", "JBoss", "JMX", "IMX", "IBM WebSphere", "Jenkins", "WebLogic", "OpenNMS", "Apache", "Groovy", "Spring"]
__PORT__ = ["1099/tcp", "8080/tcp", "7001/tcp", "8009/tcp", "8005/tcp", "33758/tcp", "53289/tcp"]
__PROT__ = ["http"]
__REFS__ = "http://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability/"
__PATCH__ = {"jenkins":["1.638", "1.625.2"]}

