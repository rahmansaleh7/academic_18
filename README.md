# Academic Information System — Odoo 18

Addon ini dibuat **untuk kebutuhan training pengembangan modul Odoo versi 18**.
Isinya adalah studi kasus sistem informasi akademik sederhana (Course, Session,
dan Attendee) yang dipakai sebagai bahan latihan untuk mengenal konsep-konsep
dasar hingga menengah dalam membuat addon Odoo.

> ⚠️ Addon ini ditujukan sebagai materi pembelajaran, bukan untuk dipakai di
> lingkungan produksi.

## Materi yang Dicakup

| Topik | Implementasi di addon |
| --- | --- |
| Model & field dasar | `academic.course`, `academic.session`, `academic.attendee` |
| Relasi | Many2one, One2many, Many2many, field `related` |
| Inheritance | `res.partner` ditambah field `is_instructor` |
| Computed field & onchange | `end_date`, `taken_seats`, peringatan jumlah kursi |
| Constraint | `_sql_constraints` dan `@api.constrains` (instruktur tidak boleh jadi peserta) |
| Override method | `copy_data` pada Course ("Copy of ...") |
| Workflow / status | Draft → Confirmed → Done pada Session |
| View | List, form, calendar, search, graph, pivot, kanban |
| Security | Group User/Manager, access rights (`ir.model.access.csv`), record rules |
| Wizard | Menambahkan peserta ke banyak session sekaligus (`TransientModel`) |
| Report | Laporan PDF Session (QWeb) |
| Terjemahan | File `i18n/id.po` untuk Bahasa Indonesia |

## Struktur Direktori

```
academic_18/
├── __manifest__.py
├── models/          # course, session, attendee, partner (inherit)
├── views/           # tampilan dan menu
├── wizard/          # wizard tambah peserta
├── report/          # laporan PDF session
├── security/        # group, record rule, access rights
├── i18n/            # template & terjemahan Bahasa Indonesia
└── static/description/icon.png
```

## Kebutuhan

- Odoo **18.0** (Community atau Enterprise)
- Python 3.10+
- Dependensi modul: `base`, `web`

## Instalasi

1. Clone repository ini ke salah satu direktori di `addons_path` Odoo Anda:
   ```bash
   cd /path/ke/custom-addons
   git clone <url-repository> academic_18
   ```
2. Restart server Odoo, lalu aktifkan **Developer Mode**.
3. Buka **Apps → Update Apps List**.
4. Cari **Academic Information System**, lalu klik **Install**.

Atau melalui command line:

```bash
./odoo-bin -c odoo.conf -d <nama_database> -i academic_18
```

## Penggunaan Singkat

1. Buat **Course** dan tentukan penanggung jawab (Responsible).
2. Tandai kontak sebagai instruktur melalui field **Is Instructor** di Contact.
3. Buat **Session** untuk Course tersebut, isi tanggal, durasi, jumlah kursi, dan instruktur.
4. Tambahkan peserta langsung dari Session, atau pilih beberapa Session di list
   view lalu gunakan wizard **Add Attendees**.
5. Ubah status Session (Confirm / Done) dan cetak laporan PDF-nya.

## Hak Akses

- **Academic / User** — dapat melihat semua Course, tetapi hanya dapat mengubah
  Course yang menjadi tanggung jawabnya (atau yang belum memiliki Responsible).
- **Academic / Manager** — dapat mengubah semua data. User admin otomatis masuk grup ini.

## Penulis

Iqbalasaleh — materi training Odoo 18 ([vitraining.com](http://www.vitraining.com))

## Lisensi

[LGPL-3](https://www.gnu.org/licenses/lgpl-3.0.html)
