Halo Pak Burhanudin Yahya,

Menindaklanjuti rekomendasi kemarin, kami memutuskan untuk memberi Pak Burhanudin Yahya tugas yang harus diselesaikan.

Tugas yang diajukan yaitu membuat REST API untuk beberapa endpoint.

Untuk keperluan pengerjaan tugas ini, dilampirkan juga data yang bisa digunakan. Data tersebut berupa file JSON, yang masing-masing barisnya mewakili satu objek JSON dengan field:

1. ***text*** => field ini berupa text tulisan yang diposting oleh user
2. ***fromuser*** => field ini mewakili user yang mengirimkan posting
3. ***mentions*** => field ini berisi daftar user yang disebut di dalam text yang dikirim oleh user lain
4. ***createdat*** => field ini berupa integer unix timestamp

Sedangkan endpoint yang diinginkan antara lain:

1. ***/topwords***

Endpoint ini akan mengembalikan nilai berupa satu objek JSON, di mana key objek tersebut mewakili satu kata dan value-nya berupa berapa banyak kata itu disebut. Jumlah kata yang dihitung berasal dari field text. Hasil dari endpoint harus terurut dari yang terbanyak sampai terendah.
```text
field: text
```
Contoh hasil:
```json
{
    "makan": 163,
    "ngga": 152,
    "haha": 15
}
```

2. ***/popular/users***

Endpoint ini mengembalikan nilai berupa objek JSON yang berisi daftar user yang paling sering posting tulisan. Hasil dari endpoint harus terurut dari yang terbanyak sampai tersedikit.
```text
field: fromuser
```
Contoh hasil:
```json
{
    "jono": 142,
    "paijo": 123,
    "john": 93
}
```

1. ***/popular/mentions***

Endpoint ini mengembalikan nilai berupa objek JSON yang berisi daftar user yang paling sering disebut dalam tulisan. Hasil dari endpoint harus terurut dari yang terbanyak sampai tersedikit.
```text
field: mentions
```
Contoh hasil:
```json
{
    "anto": 234,
    "arum": 12,
    "dahlia": 9
}
```

1. ***/hourly***

Endpoint ini mengembalikan nilai berupa objek JSON yang berisi distribusi tulisan setiap jam. Distribusi setiap jam ini tidak terbatas 24 jam dalam satu hari. Misal:
```text
- tanggal 2016-12-11 jam 10:00 - 10:59 ada 100 tulisan.
- tanggal 2016-11-15 jam 10:00 - 10:59 ada 20 tulisan.
```
Maka di data hasilnya key "10" berupa jumlah dari kedua data tersebut. Jadi nantinya key "10" akan memiliki nilai 120.
```text
field: createdat
```
Contoh hasil:
```json
{
    "00": 1,
    "01": 0,
    "02": 2,
    "03": 4,
    "04": 2,
    "05": 9,
    "06": 12,
    "07": 23,
    "08": 89,
    "09": 213,
    "10": 120,
    "11": 21,
    "12": 23,
    "13": 13,
    "14": 2,
    "15": 3,
    "16": 1,
    "17": 22,
    "18": 33,
    "19": 53,
    "20": 5,
    "21": 32,
    "22": 6,
    "23": 0
}
```

Ketentuan pengerjaan:
1. Menggunakan bahasa Python atau PHP
2. Menggunakan database MongoDB atau MySQL

Poin Plus:
1. Menggunakan bahasa Python
2. Menggunakan database MongoDB
3. Menggunakan Git
4. Mengimplementasikan Unit Test
5. Deployment ke public internet

Tugas ini bersifat rahasia, jadi untuk source code ada baiknya disimpan di folder lokal.

Pekerjaan tugas ini harus dikirimkan paling lambat tanggal ***22 Maret 2021***.

Jika ada yang ingin ditanyakan, didiskusikan, atau dikonsultasikan, feel free ya buat menghubungi saya via email ini.

Selamat mengerjakan! 😊