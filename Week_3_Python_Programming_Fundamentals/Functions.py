def add(a):
  """
  add 1 to a
  """
  b=a+1
  print a, "if you add one", b
  return(b)

print add(2)



def type_of_album(artist, album, year_released):
  if year_released > 1980:
    print(artist, album, year_released)
    return "Modern"
  else:
    print (artist, album, year_released)
    return "oldie"

x= type_of_album("MJ", "Thriller", 1980)
print x

def isGoodRating(rating=4):
  if rating < 7:
    print "this album sucks it's rating is", rating
  else:
    print 'this album is good its rating is', rating

isGoodRating()
isGoodRating(10)

artist='MJ'

def printer(artist):
  global internal_var
  internal_var = 'WH'
  print artist, 'is an artist'

printer (artist)
printer (internal_var)
