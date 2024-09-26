# creazione environment, per evitare che ubuntu non vi faccia installare la libreria di crittografia
# python -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# # Per importare una chiave pubblica
# keyDER = base64.b64decode(pubkey)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# Per iniziare generiamo una coppia di chiavi e le stampiamo
# Generating RSA Key Pair
# Una volta stampate, non serve più
# key_pair = RSA.generate(2048)
# print(key_pair.export_key())
# public_key = key_pair.publickey()
# print(public_key.export_key())
# exit(0)
sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAmyKDdrAJF6jusFf5vHGjNlV1jSf6X/zcL4TTvNffZfqFd7uf\nIQkuiEDDIz8cKUXquPlMY2wQPulHDfI3d1oAvqS7x+jI4vniev4HxdZrmTBnF4Bv\n4ZstRIRRJry21UDop2oRosfof7ZbKGVzUidRNQMAgKVB3jP2/2Hliwn0pCgODPQQ\nFz6nGxonieC0sbuHGuQ+Q08QuOSyRwMmlt7MRqDBq8TjJ7qgjr79rKsoZI3uFgPI\nmMXvr3qXTRyXsyJ45fGpPIhcgtKATeY8XK5yVWfVw4/F+Od/WYFrUZCw6qQY/+pg\nRT90f7s45DifZe3OOY4JCv5fqJJy2PtMe5tdUwIDAQABAoIBAAFe3bB3v6zQ1kMC\nk/dBPcLmIGK93q1oa32T+9boRVX+T52OL8q37QxRHig6j4Ih1wAJW85pDv+vSexq\nnmjUh7snc21BtjyjHogdpG3wBgVVcyO3A8YHe+/mB12DP05FA4kvG7bHc1tlfgqu\nUsWACWyheSipzRosdVsuPzvqO5oTqP3ddTngecBLaUxs6ppR6DGBdcyKCXuHDvjK\nN5PLxiD9joM7KTjuo6c0asqLR6cJNWCsoIHOUMlHx/kLpx26qTYRlRaSxPOK48mv\nL0Ga6spLnCZ/WQKzNFkRfbyaOvL314jtrOV1o+UoIv4JU+bkVmvAOnmJGRajVJFu\nRTpMDVkCgYEAvxBgk4LYcHiLdq8mLtBHCagkyHgg4DAlqah9njjXyHe9vvYBBqV0\n5houqCqF7MqT5RPtlniewY38k3v/16S5VUG0+nRXtkgOEwepGKNo38Uqr1EpgYvE\nfIBM0nztBXbxzO+eD4iH9luAJqPHkuwN3mCB87wijlfq+qoPSA4hDI8CgYEAz9wZ\n2337YS6k+lJ0Nb+geiu3XesWTehzphazWmD3krlcYImx+aYloqYNdj53Yl7Kiwyy\nMQzG+UCiKJdbdn3tzt6w5YnpO4kYutZjodO5PSLaWwOk06i7Fi6cJPK4NN7JghtC\nOT54HBNqUIRjz843yOZ3bIOplGqOLR/15ToQzP0CgYEAh7o+oQumbd90U0+BNGhI\nzpdf6flMgXYyix9ifW+r+oD1jh58BBitvniDBHuQv/H4thc+BFKTlLQk5TCFQs+F\nyQbwZasYVClDtkkO2q3a5nvOItTpQ1nirv8Fk9GjHuqsQwVFp4s56sx9cPWP5NND\n1uF/74GKmsvh5UfBq1I+MAkCgYBL0wuvsPZZji1qj1eLH9tHldjvLsnVI73EUbWd\ne4/0ex/Cq5g77Kr/+Tkh8EmWneOe88Ow9utCk5xT2FrqD6gHdd7r7PIi4LEfvwNb\nTiPdtHAZEWw4Ne4BeoFFTTF7P+YcSxtOTIZ+H2sB8jmC3cQlykS4VhMva+tvdKA7\nvYHRdQKBgFmgNzqswuf3xotBf6orwyEE8Bg2eQ4GW6PBj1fGQRSk/crHK9ZbPBi4\nT03lS75YeMZiGGuWTopaix3fdL7ML2EmbPnitPE9WBsjfhJU1x78HDgfEGC2NPyS\nhL9LXgTQXnzy0V5MPH1wWbPmXUIBqHF5LQzrJe4p7WrMZNOsPeRQ\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmyKDdrAJF6jusFf5vHGj\nNlV1jSf6X/zcL4TTvNffZfqFd7ufIQkuiEDDIz8cKUXquPlMY2wQPulHDfI3d1oA\nvqS7x+jI4vniev4HxdZrmTBnF4Bv4ZstRIRRJry21UDop2oRosfof7ZbKGVzUidR\nNQMAgKVB3jP2/2Hliwn0pCgODPQQFz6nGxonieC0sbuHGuQ+Q08QuOSyRwMmlt7M\nRqDBq8TjJ7qgjr79rKsoZI3uFgPImMXvr3qXTRyXsyJ45fGpPIhcgtKATeY8XK5y\nVWfVw4/F+Od/WYFrUZCw6qQY/+pgRT90f7s45DifZe3OOY4JCv5fqJJy2PtMe5td\nUwIDAQAB\n-----END PUBLIC KEY-----"
# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)


# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# Example usage
#message = ""
#encrypted_message = encrypt_message(message, public_key)
decrypted_message = decrypt_message("DoBWphql7MkndcHk70b5qHI6ZlIIO5QbkiPGly4ac6nPvrkXnR62xWwjIMgO2GlTP3MNmOe3UwoWYqjCGXEpSo4NAd5Fltr9keduYOCTEgyoSBolbufmNX7DNhSQbrtgtNCYRwIeVE2v0+sxabCXVH+k0CkfcmM129aKUFhvyrg+xllZIVaGRNrGtTZqFzDQshCN3A90tlMjtdZkVRIuak/6ZShjIr+Ik8f6/07hIOXP3D1OM81qfGFGL6cTCJ94pHvWOhAgKSCojlrjO8hZ3Lxp0yFnjCGqxYtLX/rDz1hxHmvTaGLh/RPHckEPdpDnutR6+Z1FTpKSR3ydUAkpQw==", key_pair)

#print("Original Message:", message)
#print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
