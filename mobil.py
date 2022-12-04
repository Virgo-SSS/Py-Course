class HargaMobil:
	def __init__(self):
		self.HargaJual = 10000

class PenjualanMobil(HargaMobil):
	nm = ['J', 'K', 'L', 'M']
	jk = ['Laki-Laki', 'Perempuan', 'Laki-Laki', 'Laki-Laki']
	dscjk = [0.05, 0.1, 0.05, 0.1]
	bk = ['November', 'Januari', 'Februari', 'September']
	dscbk = [0.1, 0.1, 0.1, 0.03]

	def __init__(self):
		super().__init__()
		self.nama = self.nm
		self.jeniskelamin = self.jk
		self.diskonjeniskelamin = self.dscjk
		self.bulankelahiran = self.bk
		self.diskonbulankelahiran = self.dscbk
		

	def Rumus(self,index):
		hargaakhir = self.HargaJual * (1 - self.diskonjeniskelamin[index]) * (1 - self.diskonbulankelahiran[index])
		return hargaakhir

	def main(self) :
		# a = 0
		for a in range(0,3):
			print ("Untuk anak", self.nm[a], "dengan harga awal Rp. 10000, diskon jenis kelamin", self.dscjk[a], 
			"dan diskon bulan ulang tahun", self.dscbk[a], "diberikan harga akhir", self.Rumus(a))
		


obj = PenjualanMobil()
print(obj.main())


# Origimal punya

# class HargaMobil:
# 	def __init__(self):
# 		self.HargaJual = 10000

# class PenjualanMobil(HargaMobil):
# 	def __init__(self, nm, jk, dscjk, bk, dscbk):
# 		super().__init__()
# 		self.nama = nm
# 		self.jeniskelamin = jk
# 		self.diskonjeniskelamin = dscjk
# 		self.bulankelahiran = bk
# 		self.diskonbulankelahiran = dscbk
# 		self.hargaakhir = None

# 	def Rumus(self):
# 		self.hargaakhir = self.HargaJual * (1 - self.diskonjeniskelamin) * (1 - self.diskonbulankelahiran)
# 		print(self.hargaakhir)
# 		return self.hargaakhir

# Mobil1 = PenjualanMobil("J", "laki-laki", 0.05, "november", 0.1)
# Mobil2 = PenjualanMobil("K", "perempuan", 0.1, "januari", 0.1)
# Mobil3 = PenjualanMobil("L", "laki-laki", 0.05, "februari", 0.1)
# Mobil4 = PenjualanMobil("M", "laki-laki", 0.1, "september", 0.03)

# print("Untuk anak ", Mobil1.HargaJual, "diskon jenis kelamin ", Mobil1.diskonjeniskelamin, "dan diskon bulan kelahiran ", Mobil1.diskonbulankelahiran, "diberikan harga akhir Rp ", Mobil1.Rumus())
# print("Untuk anak ", Mobil2.HargaJual, "diskon jenis kelamin ", Mobil2.diskonjeniskelamin, "dan diskon bulan kelahiran ", Mobil2.diskonbulankelahiran, "diberikan harga akhir Rp ", Mobil2.Rumus())
# print("Untuk anak ", Mobil3.HargaJual, "diskon jenis kelamin ", Mobil3.diskonjeniskelamin, "dan diskon bulan kelahiran ", Mobil3.diskonbulankelahiran, "diberikan harga akhir Rp ", Mobil3.Rumus())
# print("Untuk anak ", Mobil4.HargaJual, "diskon jenis kelamin ", Mobil4.diskonjeniskelamin, "dan diskon bulan kelahiran ", Mobil4.diskonbulankelahiran, "diberikan harga akhir Rp ", Mobil4.Rumus())