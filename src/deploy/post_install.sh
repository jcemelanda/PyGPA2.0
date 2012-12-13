touch /usr/bin/pygpa
chmod +w /usr/bin/pygpa
echo "#!/bin/bash" >> /usr/bin/pygpa
echo "python /usr/lib/python2.7/site-packages/PyGPA/main.py" >> /usr/bin/pygpa
chmod a+x /usr/bin/pygpa