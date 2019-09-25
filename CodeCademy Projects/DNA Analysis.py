sample = ['GTA', 'GGG', 'CAC']

# When used, the below method will take in a file, read it, add the file's contents to an empty string, and return the updated string


def read_dna(dna_file):
  dna_data = ""
  with open(dna_file, "r") as f:
    for line in f:
      dna_data += line  # this adds the line in the file folder to new folder
  return dna_data

# Next, we'll need a method that will take a string, create a list of codons from that string, and return the list. This will make the DNA analysis much easier later.


def dna_codons(dna):
  codons = []
  for i in range(0, len(dna), 3):
    if (i + 3) < len(dna):
      codons.append(dna[i:i + 3])
  return codons
  """so for i in range(0, len(dna), 3):
i = 0 for first iteration
(0 + 3) < len(dna) => True
codons.append(dna[0:0+3])
Ani avatar
= "ATC"
now when we do dna[0:3]
it goes 0,1,2
3 is exclusive
Ani avatar
so the first three letters are appended
so it basically makes sure that you only get 3 multiples of 3 and appends them to a list?
"""

  """The next step is to create a method that will iterate through both the sample and a suspect's DNA. The method should count the number of times a codon in the sample matches a codon in the suspect's DNA."""


def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon in sample:
      matches += 1
  return matches


def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3:
    print "# of codons matches: %s. DNA profile matches. Continue investigations." % num_matches
  else:
    print "# of codons matches: %s. DNA profile does not match. The suspect can be freed." % num_matches


is_criminal('suspect1.txt')
is_criminal('suspect2.txt')
is_criminal('suspect3.txt')
