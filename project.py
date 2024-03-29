import re
import json
import os.path

class Project:
    project_details = {
        "data": {
            "monument_id": 0,
            "site_name": "",
            "thumbnail": "",
            "latitude": 0,
            "longitude": 0,
            "category": "",
            "states": "",
            "criteria": "",
            "danger": "",
            "inscribed_date": 0,
            "extension": 0,
            "historical_description": "",
            "site_url": "https://geobrugg.com",
            "justification": "",
            "location_description": "Location description",
            "long_descsription": "<p>Situation</p>",
            "region": "",
            "revision": 0,
            "short_description": "",
            "transboundary": 0,
            "unique_number": 4,
            "isoCode": "",
            "secondary_dates": 2001
        }
    }
    amount_pics = 0

    pics = {
        "data": []
    }

    #constructor with no. of pics and project name
    def __init__(self, pics, name):
        self.data = []
        self.amount_pics = pics
        self.project_details["data"]["site_name"] = name
        self.pics["data"] = list()
        x = 0
        for x in range(self.amount_pics):
            self.pics["data"].append({
                "picture_id": x + 1,
                "approved": 1,
                "picture_url": "https://projectdetailsjson.netlify.com/picturesjpeg/" + str(self.project_details["data"]["monument_id"]) + "_" + name + "/" + name + "_"  + str(x) + ".jpg",
                "monument_id": self.project_details["data"]["monument_id"]
                })
    
 
    def create_txt_file(self):
        self.file_name = "project" + str(self.project_details["data"]["monument_id"]) + ".txt"
        complete_path_data = "./projectdetails/" + self.file_name
        complete_path_pic = "./projectpictures/pics" + self.file_name
        if os.path.isfile(complete_path_data):
            print("File already exists!")
        else:
            text_file = open(complete_path_data, "w")
            text_file.write(json.dumps(self.project_details))
            text_file.close()
            pic_file = open(complete_path_pic, "w")
            pic_file.write(json.dumps(self.pics))
            pic_file.close()

    def converted_project(self):
        conv = {
            "monument_id": self.project_details["data"]["monument_id"],
            "latitude": self.project_details["data"]["latitude"],
            "longitude": self.project_details["data"]["longitude"],
            "thumbnail": self.project_details["data"]["thumbnail"],
            "site_name": self.project_details["data"]["site_name"],
            "category": self.project_details["data"]["category"],
            "states": self.project_details["data"]["states"],
            "inscribed_date": self.project_details["data"]["inscribed_date"],
            "criteria": self.project_details["data"]["criteria"]
        }
        return(conv)

    def set_thumbnail(self, url):
        url_pattern = re.compile(r"""(?xi)
            \b
            (							# Capture 1: entire matched URL
                (?:
                https?:				# URL protocol and colon
                (?:
                /{1,3}						# 1-3 slashes
                |								#   or
                [a-z0-9%]						# Single letter or digit or '%'
         	    							# (Trying not to match e.g. "URI::Escape")
                )
                |							#   or
    		    					# looks like domain name followed by a slash:
                [a-z0-9.\-]+[.]
                (?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj| Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)
                /
                )
                (?:							# One or more:
                [^\s()<>{}\[\]]+						# Run of non-space, non-()<>{}[]
                |								#   or
                \([^\s()]*?\([^\s()]+\)[^\s()]*?\)  # balanced parens, one level deep: (…(…)…)
                |
                \([^\s]+?\)							# balanced parens, non-recursive: (…)
                )+
                (?:							# End with:
                \([^\s()]*?\([^\s()]+\)[^\s()]*?\)  # balanced parens, one level deep: (…(…)…)
                |
                \([^\s]+?\)							# balanced parens, non-recursive: (…)
                |									#   or
                [^\s`!()\[\]{};:'".,<>?«»“”‘’]		# not a space or one of these punct chars
                )
                |					# OR, the following to match naked domains:
                (?:
  	            (?<!@)			# not preceded by a @, avoid matching foo@_gmail.com_
                [a-z0-9]+
                (?:[.\-][a-z0-9]+)*
                [.]
                (?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj| Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)
                \b
                /?
                (?!@)			# not succeeded by a @, avoid matching "foo.na" in "foo.na@example.com"
                )
            )""")
        if re.match(url_pattern, url):
            self.project_details["data"]["thumbnail"] = url
        else:
            print("Not a valid URL")

    def set_states(self, state):
        self.project_details["data"]["states"] = state
    
    def set_criteria(self, product):
        self.project_details["data"]["criteria"] = product
    
    def set_date(self, year):
        if year in range(1950, 2040):
            self.project_details["data"]["inscribed_date"] = year
        else:
            print("Invalid Year")

    def set_region(self, region):
        self.project_details["data"]["region"] = region

    #Description or Smartbox Number for Smartboxes
    def set_description(self, desc):
        self.project_details["data"]["short_descsription"] = desc

    def set_iso(self, iso):
        self.project_details["data"]["isoCode"] = iso

    def set_coordinates(self, lat, lon):
        if type(lat) == float or type(lon) == float:
            print("Wrong data type")
        elif lat > 180.0 or lat < -180.0 or lon > 85.0 or lon < -85.0:
            print("Invalid Coordinates")
        else:
            self.project_details["data"]["latitude"] = lat
            self.project_details["data"]["longitude"] = lon
 

#subclass for Rockfall projects -- category overwritten -- methods for documents
class Rockfall(Project):
    rockfall_details = dict(Project.project_details)
    rockfall_details["data"]["category"] = "Rockfall"
    def set_acceptance_cert(self, url):
        self.rockfall_details["data"]["historical_description"] = url

    def set_system_drawings(self, url):
        self.rockfall_details["data"]["danger"] = url
    

#subclass for Smartbox projects -- category overwritten -- method for snapshot URL
class Smartbox(Project):
    smartbox_details = dict(Project.project_details)
    smartbox_details["data"]["category"] = "Smartbox"
    def set_snapshot(self, url):
        self.smartbox_details["data"]["site_url"] = url
    

#subclass for Slope projects -- category overwritten
class Slope(Project):
    slope_details = dict(Project.project_details)
    slope_details["data"]["category"] = "Slope"
    

#Subclass for corrosion projects -- category overwritten
class Corrosion(Project):
    corrosion_details = dict(Project.project_details)
    corrosion_details["data"]["category"] = "Corrosion"
    

class InputError():
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression where the error occured
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


#for testing ---  will go into editor.py in some form
