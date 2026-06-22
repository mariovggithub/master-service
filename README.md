# Master Service - SIAKAD System

**Master Service** adalah core microservice dalam arsitektur Sistem Informasi Akademik (SIAKAD).
Layanan ini berfungsi sebagai **Single Source of Truth (SSOT)** yang mengelola seluruh data induk untuk ekosistem layanan SIAKAD.

---

## Fitur Utama

Master Service bertanggung jawab atas pengelolaan data dasar yang menjadi fondasi bagi layanan lain:

* **Manajemen Unit Akademik**
  Mengelola hierarki Fakultas dan Program Studi.

* **Manajemen Pengguna**
  Mengelola data Dosen, Mahasiswa, serta Role-Based Access Control (RBAC).

* **Kurikulum & Semester**
  Mengatur data kurikulum dan siklus akademik (semester aktif/non-aktif).

* **Mata Kuliah**
  Menyediakan katalog mata kuliah dan aturan SKS.

* **Aturan Akademik**
  Mengelola prasyarat pengambilan mata kuliah.

---

## 🛠 Tech Stack

* **Language**: Python 3.10+
* **Framework**: Nameko (Microservices RPC Framework)
* **Database**: PostgreSQL
* **ORM**: SQLAlchemy
* **Containerization**: Docker & Docker Compose
* **Communication**: RabbitMQ (Message Broker)

---

## Konfigurasi

Layanan ini menggunakan environment variables untuk konfigurasi:

| Variable         | Deskripsi                        |
| ---------------- | -------------------------------- |
| `DB_HOST`        | Host database                    |
| `DB_USER`        | Username database                |
| `DB_PASS`        | Password database                |
| `DB_NAME`        | Nama database                    |
| `JWT_SECRET_KEY` | Secret key untuk autentikasi JWT |
| `NAMEKO_CONFIG`  | Path ke file `config.yml`        |

---

## Cara Menjalankan

Pastikan Docker sudah terinstall, lalu jalankan:

```bash
docker compose up -d --build
```

---

## Arsitektur & Interaksi Layanan

Master Service menerapkan prinsip **Loose Coupling**:

* **Zero Outbound Dependency**
  Tidak bergantung pada service lain.

* **Inbound Interaction**
  Service lain (seperti Penawaran dan Perwalian) memanggil Master Service melalui **Nameko RPC** untuk validasi data.

Contoh:

* Validasi NIP dosen
* Validasi NRP mahasiswa

---

## API Documentation

Akses melalui **API Gateway**.

### Endpoint contoh:

```http
GET /master/lecturers
POST /master/students
PUT /master/courses/<course_id>
```

---

## Authentication

Gunakan JWT Token pada setiap request:

```http
Authorization: Bearer <JWT_TOKEN>
```

---

## Contoh Penggunaan

### Request

```http
GET /master/students
```

Header:

```http
Authorization: Bearer <JWT_TOKEN>
```

---

### Response

```json
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "name": "Budi Santoso",
      "nrp": "12345678"
    }
  ]
}
```

---

## Tips

* Gunakan **YARC** atau **Postman** untuk testing endpoint
* Pastikan token JWT masih valid
* Pastikan service dan database sudah running

---

## Catatan

* Master Service adalah pusat data utama dalam sistem
* Perubahan data di service lain harus mengacu ke Master Service
* Database menggunakan pendekatan **service-per-database**

---
