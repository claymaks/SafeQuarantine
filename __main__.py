import sys
from app import app

if len(sys.argv) > 1 and sys.argv[1] == "local":
    app.run(ssl_context='adhoc')
else:
    app.run()