#This is a filter module
import re
wikilink = re.compile("\s+([A-Z][a-z]+[A-Z][a-z]+)\s*")

from django import template

register= template.Library()

@register.filter
def wikify(value):
	return wikilink.sub(r" <a href='/mywiki/\1/'>\1</a>", value)
