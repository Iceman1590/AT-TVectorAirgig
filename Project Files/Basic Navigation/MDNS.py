import anki_vector
vector_mdns = anki_vector.mdns.VectorMdns.find_vector(None)

if vector_mdns is not None:
  print(vector_mdns['ipv4'])
else:
  print("No Vector found on your local network!")