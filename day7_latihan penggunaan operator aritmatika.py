# meghitung volume dan luas permukaan prisma segitiga


luas_alas     = int(input( "masukkan luas alas prisma:"))
tinggi        = int(input("masukkan tinggi prisma:"))
keliling_alas = int(input("masukkan keliling alas prisma:"))

volume        = luas_alas * tinggi
lp_prisma   = (2 * luas_alas) + ( keliling_alas * tinggi )

print ("volume prisma",volume, "Cm3  dan luas prisma", lp_prisma,"cm3")


 
