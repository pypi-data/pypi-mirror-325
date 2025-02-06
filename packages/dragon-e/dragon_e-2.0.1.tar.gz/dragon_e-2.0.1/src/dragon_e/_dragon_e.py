class DragonError(Exception):
	"Raised when there is a Dragon Encryption error."
	pass

def encrypt(ome, pke):
	ome = str(ome)
	pke = str(pke)
	if len(ome) == 0: raise DragonError("Cannot encode an empty message")
	if len(pke) == 0: raise DragonError("Cannot encode an empty passkey")
	ume = [ord(i) for i in ome]
	upe = [ord(i) for i in pke]
	ple = len(pke)
	ape = [int(i) + ple for i in upe]
	fne = ':'.join([str(int(ume[i]) + ape[i%ple]) for i in range(len(ume))])
	return fne

def stealthencrypt(ome, pke):
	nme = encrypt(ome, pke).split(':')
	for i in range(len(nme)):
		if len(nme[i]) < 3:
			nme[i] = '0'+nme[i]
	nme = ''.join(nme)
	return nme

def decrypt(ene, pkd):
	ene = str(ene)
	pkd = str(pkd)
	if len(ene) == 0: raise DragonError("Cannot decode an empty message")
	if len(pkd) == 0: raise DragonError("Cannot decode an empty passkey")
	emd = [int(i) for i in ene.split(':')] if ene.count(':') > 0 else [int(ene[i:i+3]) for i in range(0, len(ene), 3)]
	plt = [ord(i) for i in pkd]
	lpt = len(pkd)
	plt = [i + lpt for i in plt]
	emd = [emd[i] - plt[i%lpt] for i in range(len(emd))]
	fnd = ''.join([chr(i) for i in emd])
	return fnd


if __name__ == '__main__':
	print("This isn't supposed to be run as a standalone script. Run this as a module and import its functions.")