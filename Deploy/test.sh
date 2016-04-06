virtualenv --python=/usr/local/bin/python2.7 xss
cd xss
source bin/activate
git clone https://github.com/DanMcInerney/xsscrapy.git
cd xsscrapy
cat requirements.txt
pip install -r requirements.txt
./xsscrapy.py -u http://www.qi.nl
