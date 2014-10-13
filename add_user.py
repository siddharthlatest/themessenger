import web
import email_me
import urlparse
import json

urls = (
   '/email', 'Email_Add',
)

app = web.application(urls, globals())

class Email_Add:
   def GET(self):
      return "OK"
   def POST(self):
      web.header('Access-Control-Allow-Origin', '*')
      try:
         request = json.loads(web.data())
         email_me.email(request['toaddress'], request['subject'], request['body'])
      except Exception as ex:
         print ex.message
         raise ex
if __name__ == '__main__':
   app.run()
