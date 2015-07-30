
# all the imports
from flask import Flask, abort, render_template,session
import time

#Create the application
application = Flask(__name__)

application.secret_key = '3v\x8c\\\xab\x9f\xda\x10\xd5\x8eB\xc0q1\xc1n\x90\xf6\xa7=[\xdd\x1a\x04'

#Application version string
sVersion = 'Version 1.2'

@application.route('/')
def home_work(spath='default'):
    return render_template('index.html')

@application.route('/landingpage1.html')
def landingpage1_work():
    return render_template('landingpage1.html')

@application.route('/cart.html')
def cart_work():
    session['order'] = int(time.time())
    return render_template('cart.html')

@application.route('/checkout.html')
def checkout_work():
    if 'order' not in session:
        session['order'] = int(time.time())
    return render_template('checkout.html')

@application.route('/confirmation.html')
def confirmation_work():
    return render_template('confirmation.html')

@application.route('/prodlist.html')
def prodlist_work():
    return render_template('prodlist.html')

@application.route('/prodpage1.html')
def prodpage1_work():
    return render_template('prodpage1.html')

@application.route('/prodpage2.html')
def prodpage2_work():
    return render_template('prodpage2.html')

@application.route('/upsell1.html')
def upsell1_work():
    return render_template('upsell1.html')

@application.route('/upsell2.html')
def upsell2_work():
    return render_template('upsell2.html')

@application.route('/upsell3.html')
def upsell3_work():
    return render_template('upsell3.html')

@application.route('/version')
#@application.route('/version/')
def version_work():
    
    #URL to return the current version of the app
    application.logger.info('Version route - ' + sVersion)
    return sVersion

@application.route('/favicon.ico')
def favicon_work():
    abort(404)

if __name__ == '__main__':
    application.run(debug=True) 
