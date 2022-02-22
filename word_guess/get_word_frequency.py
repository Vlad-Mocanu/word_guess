#/bin/python3

from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wlexpr
import yaml

word_length = 5

session = WolframLanguageSession("/opt/Wolfram/WolframEngine/12.2/Executables/WolframKernel")

with open('words_alpha.txt') as word_file:
	english_words = word_file.read().split()

print('Loaded %d words from file' % (len(english_words)))
fixed_length_words = [x for x in english_words if len(x) == word_length]
print('Extract words with length %0d, there are %d words' % (word_length, len(fixed_length_words)))

frequencies = dict()

for word_index in range(0,int(len(fixed_length_words))):
	print(fixed_length_words[word_index])
	temp_freq = session.evaluate(wlexpr("WordFrequencyData[\"%s\", IgnoreCase->True]" % (fixed_length_words[word_index])))
	
	# if mathematica cound not find it frequency = 0
	if type(temp_freq) is not float:
		temp_freq = float(0)
	frequencies[fixed_length_words[word_index]] = temp_freq

session.terminate()

with open('words_frequencies.yaml', 'w') as f:
	data = yaml.dump(frequencies, f)
