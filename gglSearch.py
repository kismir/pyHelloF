import urllib.parse,urllib.request
import json as m_json

def query(q):
  query = q
  query = urllib.parse.urlencode( { 'q' : query } )
  response = urllib.request.urlopen( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
  json = m_json.loads ( response.decode() )
  results = json [ 'responseData' ] [ 'results' ]
  for result in results:
      title = result['title']
      url = result['url']   # was URL in the original and that threw a name error exception
  return ( title + '; ' + url )
      
  
