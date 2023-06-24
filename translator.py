import json
from googletrans import Translator


input_file_name = input('input file name (a.json):  ')
output_file_name= input('output file name (output.json); ')
input_lang =  input('input language key (default:en):   ')
output_lang =  input('input language key (default:fa):  ')
if not input_lang:
    input_lang = 'en'
if not output_lang:
    output_lang = 'fa' 
if not input_file_name:
    input_file_name='a.json'
if not output_file_name:
    output_file_name='output.json'
def translate_dict(d, translator):
    for k, v in d.items():
        if isinstance(v, dict):
            translate_dict(v, translator)
        elif isinstance(v, str):
            if translator.detect(v).lang == input_lang:
                translation = translator.translate(v, dest=output_lang).text
                d[k] = translation
                print(f"text '{v}' Translate to '{translation}' .")



with open(input_file_name, 'r') as f:
    data = json.load(f)


translator = Translator()


try:
    translate_dict(data, translator)
except Exception as e:
    print('\n\nStop and Save ...',e)


with open(output_file_name, 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print('Done.')
