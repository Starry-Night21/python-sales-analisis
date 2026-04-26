import pandas as pd
import matplotlib.pyplot as plt

# load data 
df = pd.read_csv("data.csv")

# tambah kolom total
df["Total"] = df["Harga"] * df["Jumlah"]

# total penjualan
total_penjualan = df["Total"].sum()

print("Total Penjualan: ", total_penjualan)

# penjualan per kategori
per_kategori = df.groupby("Kategori")["Total"].sum()

print("\nPenjualan per Kategori: ")
print(per_kategori)

# kategori tertinggi
kategori_tertinggi = per_kategori.idxmax()
nilai_tertinggi = per_kategori.max()

print("\nKategori Terlaris: ")
print(kategori_tertinggi, "-", nilai_tertinggi)

# penjualan per hari
df["Tanggal"] = pd.to_datetime(df["Tanggal"])
per_hari = df.groupby("Tanggal")["Total"].sum()

hari_tertinggi = per_hari.idxmax()
nilai_hari = per_hari.max()

print("\nHari dengan penjualan tertinggi")
print(hari_tertinggi.date(), "-", nilai_hari)

# grafik kategori 
per_kategori.plot(kind="bar", title="Penjualan per Kategori")
plt.show()

# grafik harian
per_hari.plot(kind="line", title="Tren Penjualan Harian")
plt.show()

# RINGKASAN
print("\n=== RINGKASAN ANALISIS ===")
print(f"Total Penjualan: Rp {total_penjualan:,.0f}")

print("\nPenjualan per Kategori: ")
for kategori, nilai in per_kategori.items():
    print(f"- {kategori}: Rp {nilai:,.0f}")

print(f"\nKategori Terlaris: {kategori_tertinggi} (Rp {nilai_tertinggi:,.0f})")
print(f"Hari Terbaik: {hari_tertinggi.date()} (Rp {nilai_hari:,.0f})")

# simpan per kategori
per_kategori.to_csv("hasil_per_kategori.csv")
# simpan per hari
per_hari.to_csv("hasil_per_hari.csv")

# summary file
with open("summary.txt", "w") as f:
    f.write("RINGKASAN ANALISIS PENJUALAN\n\n")
    f.write(f"Total Penjualan: Rp {total_penjualan:,.0f}\n")
    f.write(f"Kategori Terlaris: {kategori_tertinggi}\n")
    f.write(f"Hari Terbaik: {hari_tertinggi.date()}\n")

# simpan grafik
# grafik kategori
per_kategori.plot(kind="bar", title="Penjualan per Kategori")
plt.savefig("chart_kategori.png")
plt.clf()

# grafik harian
per_hari.plot(kind="line", title="Tren Penjualan Harian")
plt.savefig("chart_harian.png")
plt.clf()