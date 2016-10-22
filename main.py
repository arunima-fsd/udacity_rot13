import webapp2

import os

import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jina_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
							  autoescape = True)


def test_func(my_str):
        return my_str.swapcase()

def convert_rot(my_char):
    number = my_char + 13
    if((my_char >= 65) and (my_char <= 90)):
        if(number > 90):
            temp = 90 - my_char
            temp = (13 - temp) + 65 - 1
            number = temp
    else:
        if(number > 122):
            temp = 122 - my_char
            temp = (13 - temp) + 97 - 1
            number = temp
        
    return chr(number)



def isAlphabet(num):
    if(((num >= 65) and (num <= 90)) or ((num>=90) and (num <= 122))):
       return True
    else:
       return False

def convert_all(my_str):
    output_str=""
    for letter in my_str:
       letter_ascii = ord(letter)
       if (isAlphabet(letter_ascii)):
           new_char = convert_rot(letter_ascii)
           output_str += new_char

       else:
           output_str += letter


    return output_str

        


class Handler(webapp2.RequestHandler):
	"""docstring for Handler"""
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jina_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))


		


class MainPage(Handler):
        def get(self):
                self.render("index.html")


        def post(self):
                input_str = self.request.get("text")
                input_str = convert_all(input_str)
                self.render("index.html", input_str = input_str)

app = webapp2.WSGIApplication([('/', MainPage),], debug=True)
