c={}
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        r="http://tinyurl.com/"+str(len(c))
        if r not in c.keys():
            c[r]=longUrl
        return r
        

    def decode(self, shortUrl: str) -> str:
        return c[shortUrl]
        
        """Decodes a shortened URL to its original URL.
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))