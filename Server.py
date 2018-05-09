from aiohttp import web
import spacy
import json

nlp = spacy.load('en')

async def handle(request):
    q = request.query['q']
    doc = nlp(q)
    text = json.dumps(doc.print_tree())
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/dependency', handle)])
web.run_app(app, port=9001, )
