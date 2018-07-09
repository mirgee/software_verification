// Potrebne abstraktni signatury
abstract sig Radek { }
abstract sig Sloupec { }
abstract sig Barva { }
abstract sig Symbol { }

// Kazde pole prislusi prave jednomu radku, sloupci, obsahuje prave jeden symbol a je prave jedne barvy
abstract sig Pole { r: one Radek, s: one Sloupec, sym: one Symbol, b: one Barva }

// Definice konkretnich instanci signatur (atomu)
one sig sym1, sym2, sym3, sym4 extends Symbol { }
one sig zel, cer, sed, hne extends Barva { }
one sig r1, r2, r3, r4 extends Radek { }
one sig s1, s2, s3, s4 extends Sloupec { }
one sig p11, p12, p13, p14, p21, p22, p23, p24, p31, p32, p33, p34, p41, p42, p43, p44 extends Pole { }

// Vynuceni spravneho rozdeleni poli do radku
fact radky {
	(p11 + p12 + p13 + p14).r in r1 and
	(p21 + p22 + p23 + p24).r in r2 and
	(p31 + p32 + p33 + p34).r in r3 and
	(p41 + p42 + p43 + p44).r in r4
}

// Vynuceni spravneho rozdeleni poli do sloupcu
fact sloupce {
	(p11 + p21 + p31 + p41).s in s1 and
	(p12 + p22 + p32 + p42).s in s2 and
	(p13 + p23 + p33 + p43).s in s3 and
	(p14 + p24 + p34 + p44).s in s4
}

// Vynuceni spravneho rozdeleni barev do poli podle zadani
fact barvy {
	(p11 + p12 + p13 + p21).b in zel and
	(p14 + p22 + p23 + p24).b in cer and
	(p32 + p33 + p34 + p44).b in sed and
	(p31 + p41 + p42 + p43).b in hne
}

// Prirazeni symbolu polim podle zadani
fact symboly {
	p14.sym in sym3 and
	p23.sym in sym1 and
	p33.sym in sym4 and
	p34.sym in sym2
}

// Pro zadne dve ruzna pole neplati, ze by obsahovala stejny symbol a zaroven nalezela do stejneho radku, sloupce,
// nebo stejne barve
fact pravidla {
	no disj p1, p2 : Pole | p1.sym = p2.sym and (p1.r = p2.r or p1.s = p2.s or p1.b = p2.b)
}

run {} for 4 Symbol, 4 Barva, 4 Radek, 4 Sloupec, 16 Pole


