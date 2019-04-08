


data = {}

### Add info
info = {'description': 'CUB-200-2011 Dataset',
        'url': 'http://www.vision.caltech.edu/visipedia/CUB-200-2011.html', 
        'version': '1.0',
        'year': 2011,
        'contributor': 'Caltech',
        'date_created': '2011/01/01'}

data['info'] = info

### Add licences
licenses = {'url': 'http://creativecommons.org/licenses/by-nc-sa/2.0/',
            'id': 1,
            'name': 'Attribution-NonCommercial-ShareAlike License'}

data['licenses'] = licenses

### Add annotations
annotations = {}

data['annotations'] = annotations

### Add images
images = {}

#filename
# license, cub_url, height, width, date_captured, flickr_url, id (nummers uit .jpg)

data['images'] = images
# image_id, id, caption

# SAVE